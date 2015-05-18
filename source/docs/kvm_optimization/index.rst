
================
KVM Optimization
================

Normally kvm instances are managed by virsh, in which instance is called domain. virsh can be used to create, pause, and shutdown domains.

Disk Optimization
=================

Asynchronous IO
---------------

Disk Cache Mode
---------------
disk_cachemodes: ``writethrough`` ``writeback`` ``none(default)`` ``directsync``

Memory Optimization
===================

Check HugePage status
---------------------

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
-------------------

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


Anonymous HugePages
-------------------

kvm instance will use anonymous hugepages by default. Once hugepages are allocated to an instance, they will not be recycled until the instance is destroyed.

.. code-block:: shell

    ps -fp `grep AnonHugePages /proc/*/smaps | grep -v 'AnonHugePages: 0 kB' | cut -d/ -f3`


Transparent HugePages(THP)
--------------------------

Start to use THP
^^^^^^^^^^^^^^^^

.. raw:: html

    <div class="sidebar">

**Warning!**

If Nova-Compute Service is not disabled, any changes to libvirt.xml will not take effect.

.. raw:: html

    </div>

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


Network Optimization
====================

MTU Size
--------

Enhance Launch Speed
====================

resize qcow2 image's disk size to fit target flavor's disk size
