====
Nova
====


.. sidebar:: Terms

    | **BM, BareMetal** -- Physical Machine

`nova-docker <https://wiki.openstack.org/wiki/Docker>`_
-----------


nova-rootwrap
-------------

Root wrapper, provide nova an option other than sudo, make sure nova can only able run cmds matches specified filters::

    nova-rootwrap conf-file cmd


- conf file:
    - ``/etc/nova/rootwrap.conf``
    - ``/etc/sudoers.d/nova-rootwrap``
    - ``/etc/nova/nova.conf``
        - enable **lvm backend** (block) instead of **file backend** by add ``images_type`` & ``images_volume_group``
        - diable dd remove block device -- ``volume_clear = none``

.. code-block:: ini

    [default]
    default_ephemeral_format = ext4

    [libvirt]
    images_type = lvm
    images_volume_group = vgname
    volume_clear = none
        
- policies: ``/etc/nova/policy.json``

.. code-block:: json

    # "compute:create:forced_host": "is_admin:True",
    "compute:create:forced_host": "",


- filters: ``/etc/nova/rootwrap.d/*.filters
    - take effect as soon as imported to this folder

.. sidebar:: `Storage <http://docs.openstack.org/openstack-ops/content/storage_decision.html>`_

    - **Ephemeral Storage** -- meaning that (from the user's point of view) they effectively disappear when a virtual machine is terminated.
    - **Persistent Storage** --  means that the storage resource outlives any other resource and is always available, regardless of the state of a running instance.
        - Object Storage --  users access binary objects through a REST API
        - Block Storage --  provides users with access to block-storage devices

Management
----------

SecGroup
^^^^^^^^

* check infos

.. code-block:: bash
    :linenos:

    nova secgroup-list
    nova secgroup-list-rules <name/id>

* add a rule

.. code-block:: bash
    :linenos:

    nova secgroup-add-rule <secgroup> <ip-proto> <from-port> <to-port> <cidr>
    nova secgroup-add-rule default icmp -1 -1 0.0.0.0/0
    nova secgroup-add-rule default tcp 1 65535 0.0.0.0/0
    nova secgroup-add-rule default udp 1 65535 0.0.0.0/0

.. image:: images/secgroup.png

KeyPair
^^^^^^^

.. code-block:: bash
    :linenos:

    nova keypair-add --pub_key=file <keyname>

Flavor
^^^^^^

.. code-block:: bash
    :linenos:

    flavor-create <name> <id> <ram> <disk> <vcpus>
    flavor-create testflavor 6 128 0 1

Instances
^^^^^^^^^

.. sidebar:: Note

    --min/max-count : start multiple instances
    --poll : will show progress, only for 1st instance, not for multiple instances


.. code-block:: bash
    :linenos:

    nova boot [--poll] [--min-count <num>] [--max-count <num>] --flavor <flavor> --image <image> <instance name>
    # boot from cinder
    nova volume-create 40 --image-id=<image_id>
    nova boot --flavor <flavor> --block-device-mapping vda=<volume_uuid>:::0 <instance name>
    nova boot --flavor <flavor> --block-device source=image,id=<image_id>,dest=volume,size=<disk_size,unit G>,shutdown=preserve,bootindex=0 <instance name>
    # check failure instances
    for i in `nova list | grep bootbench | awk '{print $2}'`;do nova console-log $i | grep login: 1>/dev/null || echo $i;done
    # boot instance at specified host
    nova boot --image <uuid/name> --flavor <uuid/name> --key-name <kname> --availability-zone nova:server2

Services
^^^^^^^^

- multiple nova compute backends need multiple n-cpu daemons
    - https://blueprints.launchpad.net/nova/+spec/multi-back-ends-for-nova-compute

.. code-block:: bash
    :linenos:

    # disable services
    for i in `seq 10 15`;do nova service-disable --reason=testboot r16s$i nova-compute;done


issues
======

1. user xxx is unauthorized for tenent yyy

.. code-block:: console

    stack@r16s01:~/devstack$ nova boot --image ${IMAGE} --flavor m1.tiny ${INSTANCE} --    availability-zone nova:r16s03
    ERROR (Unauthorized): User d8b90ec35da147ac8ca608253504a089 is unauthorized for tenant     2638cc4008a149a58c7a23df282af954 (Disable debug mode to suppress these details.) (HTTP 401) (Request-ID: req-32404359-fb4b-414f-b635-2f5451d1ebe0)

- Solution: add **demo** to project **admin**


