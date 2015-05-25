
================
KVM Optimization
================

Normally kvm instances are managed by virsh, in which instance is called domain. virsh can be used to create, pause, and shutdown domains.

Disk
====

Asynchronous IO
---------------

AIO is not enabled by defalut, default value is io='threads', when AIO enabled, io='native'.
There is no available option to enable AIO, cause 'threads' mode will improve network storage(cinder)'s performance [#]_.
So we need to change nova's libvirt config file manually.

.. code-block:: python
    :linenos:

    class LibvirtConfigGuestDisk(LibvirtConfigGuestDevice):
    
        def __init__(self, **kwargs):
            super(LibvirtConfigGuestDisk, self).__init__(root_name="disk",
                                                         **kwargs)
            .
            .
            self.snapshot = None
            self.backing_store = None
            self.io = "native"    #add
        def format_dom(self):
            dev = super(LibvirtConfigGuestDisk, self).format_dom()
            .
            .
            if (self.driver_name is not None or
                self.driver_format is not None or
                self.driver_cache is not None or
                    self.driver_discard is not None):
                drv = etree.Element("driver")
                if self.driver_name is not None:
                    drv.set("name", self.driver_name)
                .
                .
                if self.io is not None:  #add
                    drv.set("io", self.io)   #add
                dev.append(drv)

Here's the location of configuration file.

.. code-block:: shell

    # vi /usr/lib/python2.7/dist-packages/nova/virt/libvirt/config.py
    vi /opt/stack/nova/nova/virt/libvirt/config.py



Disk Cache Mode
---------------
disk_cachemodes: ``writethrough`` ``writeback`` ``none(default)`` ``directsync`` ``unsafe`` ::

    [libvirt]
    vif_driver = nova.virt.libvirt.vif.LibvirtGenericVIFDriver inject_partition = -2
    live_migration_uri = qemu+ssh://stack@%s/system use_usb_tablet = False
    cpu_mode = none
    virt_type = kvm
    disk_cachemodes = file=writeback,block=none

Storage Backend
---------------

**block backend** performs better than **file backend**.
qcow2 belongs to *file backend*.

**2 ways to realize block backend**

* cinder volume
* local lvm

Memory
======

Drop Memory Cache
-----------------

.. code-block:: shell

    echo 3 > /proc/sys/vm/drop_caches

HugePages
---------

.. sidebar:: Note

    There are two types of Hugepages, **Anonymous** and **Transparent**. Without hugepage, disk I/O drop drastically.
    
    **AnonHugePages** stands for the total space of Anonymous Hugepage.
    It can be divided by *Hugepagesize*
    
    **HugePages_Total** stands for the total space of Transparent Hugepages.
    Equals to *vm.nr_hugepages* * *Hugepagesize*


Check HugePage status
^^^^^^^^^^^^^^^^^^^^^


* ``sudo sysctl -a | grep -i huge`` ::

    vm.hugepages_treat_as_movable = 0
    vm.hugetlb_shm_group = 0
    vm.nr_hugepages = 0
    vm.nr_hugepages_mempolicy = 0
    vm.nr_overcommit_hugepages = 0

* ``cat /proc/meminfo | grep -i huge`` ::

    AnonHugePages:      8192 kB
    HugePages_Total:       0
    HugePages_Free:        0
    HugePages_Rsvd:        0
    HugePages_Surp:        0
    Hugepagesize:       2048 kB


Enable 1GB HugePage
^^^^^^^^^^^^^^^^^^^

Currently, this size only support rhel & centos.
*Restarting Host OS* is required after the step 1.
After that, hugepage number cannot be changed.

#. kernel options: ``default_hugepagesz=1G hugepagesz=1G hugepages=80 hugepagesz=2M hugepages=1024`` ::

    sudo vi /etc/default/grub
    grub2-mkconfig


#. Mount 1GB huge pages ::

    mkdir /dev/hugepages1G
    mount -t hugetlbfs -o pagesize=1G none /dev/hugepages1G
    mkdir /dev/hugepages2M
    mount -t hugetlbfs -o pagesize=2M none /dev/hugepages2M

#. Restart libvirtd ::

    systemctl restart libvirtd


Anonymous HugePages (AHP)
^^^^^^^^^^^^^^^^^^^^^^^^^

kvm instance will use anonymous hugepages by default. AHPs were allocated dynamically, once hugepages are allocated to an instance, they will not be recycled until the instance is destroyed.

**Check which process use AHP**

.. code-block:: shell

    ps -fp `grep AnonHugePages /proc/*/smaps | grep -v 'AnonHugePages:         0 kB' | cut -d/ -f3`

**Enable anonymous hugepage**

.. code-block:: shell

    sudo echo always > /sys/kernel/mm/transparent_hugepage/enabled
    sudo echo madvise > /sys/kernel/mm/transparent_hugepage/defrag


Transparent HugePages(THP)
^^^^^^^^^^^^^^^^^^^^^^^^^^

THP is kind of static Hugepage, once its number changed, memory useage goes with it.

.. sidebar:: Warning !

    * If Nova-Compute Service is not disabled, any changes to libvirt.xml will not take effect.
    * THPs are known to cause  unexpected node reboots and performance problem with Oracle RAC & JDK

#. Disable Nova-Compute Service
#. ``virsh destroy <instance>``
#. ``virsh edit <instance>`` ::

    <memoryBacking>
      <hugepages/>
    </memoryBacking>

#. Allocate THP (2 methods)
    * ``sudo sysctl -w vm.nr_hugepages=val``
    * ``sudo echo val > /proc/sys/vm/nr_hugepages``
#. ``virsh start <instance>``
#. Start Nova-Compute Service


Network
=======

MTU Size
--------
When using tunnel network (GRE, vxlan) , set the MTU in the Guest to 1400, this will allow for the GRE/vxlan header and no packet fragmentation.

* change default dnsmasq conf file at **/etc/neutron/dhcp_agent.ini** ::

.. code-block:: guess

    dnsmasq_config_file = /etc/neutron/dnsmasq-neutron.conf

* add dhcp option to **/etc/neutron/dnsmasq-neutron.conf** ::

.. code-block:: guess

    dhcp-option-force=26,1400

* restart Neutron-DHCP service

.. code-block:: shell

    # sudo pkill -1 neutron-dhcp-agent
    service neutron-dhcp-agent restart
    

Turn off NIC's offloads
-----------------------

Turn **TSO/LRO** and **GRO/GSO** off on the instance physical machine for traffic to work, will help improve instance's performance greatly, especially **GRO** . [#]_

* Check offloads' status ::

    $ ethtool -k enp6s0f1
    tcp-segmentation-offload: on
            tx-tcp-segmentation: on
            tx-tcp-ecn-segmentation: off [fixed]
            tx-tcp6-segmentation: on
    udp-fragmentation-offload: off [fixed]
    generic-segmentation-offload: on
    generic-receive-offload: off
    large-receive-offload: off

* Turn offloads off ::

    $ sudo ethtool -K enp6s0f1 tso off lro off gro off gso off

::


Improve Instance's Launch Speed
===============================

* Resize qcow2 image's disk size to fit target flavor's disk size

.. code-block:: shell
    :linenos:

    # guestfish - the libguestfs Filesystem Interactive SHell
    sudo apt-get install libguestfs-tools -y --force-yes 2>/dev/null || sudo yum install -y libguestfs-tools
    # create an empty qcow2 image with target size
    qemu-img create -f qcow2 image_name image_size
    # use guestfish to resize it
    virt-resize -d --expand /dev/sda1 src_image dst_image
    qemu-img info dst_image


.. [#] https://blueprints.launchpad.net/nova/+spec/improve-nova-kvm-io-support
.. [#] https://www.rdoproject.org/Using_GRE_tenant_networks
