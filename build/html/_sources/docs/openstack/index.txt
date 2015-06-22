=========
OpenStack
=========

`wiki <https://wiki.openstack.org/wiki/Main_Page>`_
`Developer's Guide <http://docs.openstack.org/infra/manual/developers.html>`_

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


- conf file: ``/etc/nova/rootwrap.conf`` ``/etc/sudoers.d/nova-rootwrap``
- filters: ``/etc/nova/rootwrap.d/*.filters

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


Heat
====

Heat is the main project in the OpenStack Orchestration program. It implements an orchestration engine to launch multiple composite cloud applications based on templates in the form of text files that can be treated like code. A native Heat template format is evolving, but Heat also endeavours to provide compatibility with the AWS CloudFormation template format, so that many existing CloudFormation templates can be launched on OpenStack. Heat provides both an OpenStack-native ReST API and a CloudFormation-compatible Query API. [#]_


Horizon
=======

.. sidebar:: Overview

    - PTL: Gabriel Hurley (Nebula)
    - OpenStack web dashboard service
    - horizon can't detect how big volume group is
      

Dependency
----------

- **apache2** -- apache web server
- **memcache** -- mem-cache-d，is a free memory caching system, speed up dynamic database-driven website by caching data in RAM
- **django** -- python based web framework

Congiure file
-------------

- **/opt/stack/horizon/openstack_dashboard/settings.py**
    - ``SESSION_TIMEOUT`` make this val bigger, no need enter password frequently.
- **/opt/stack/horizon/openstack_dashboard/local/local_settings**
    - ``TIME_ZONE`` change defaut time_zone *UTC* to *Asia/Shanghai*


Refresh horizon
---------------
   
.. code-block:: bash

   sudo service {apache2,memcached} restart

`Cinder <https://wiki.openstack.org/wiki/Cinder>`_
==================================================

.. image:: images/cinder_locations.png

.. sidebar:: Overview

    - PTL: Mike Perez
    - Since Folsom, Cinder has replaced Nova-Volume as default block storage service.
    - compare to swift, cinder could provide real time read/write, like a mobile disk
    - it's much cheaper to create a volume than an instance
    - severely rely on RabbitMQ
    - **volume type** -- a type or label can be selected at vol creation time, maps to a set of capabilities of the storage back-end driver to be used for this vol

Components
----------

- **API node** -- provide RESTful API
- **Schedule node** -- communicate between API node & volume node, API node & schedule node normally in same host
- **Volume node** -- provide detachable block storage

Storage backend
---------------

- Local: lvm
- Network: NFS, ceph RBD (RADOS), sheepdog

work flow
---------

create cinder volume
^^^^^^^^^^^^^^^^^^^^

.. image:: images/cinder_create_vol.png
    :align: right

1. client send a create volume request to API node
2. will check whether request is legal, then send request to a schedule node randomly
3. pick up one node from health volume node
4. create volume, then return volume status
5. scheduler return volume status to api node
6. api return volume status to client

.. code-block:: bash
    
    cinder create --hint local_to_instance=instance_uuid --display_name=instance_name SIZE

delete cinder volume
^^^^^^^^^^^^^^^^^^^^

It will cost lots of time, since wipe data permanently is required before remove a volume.
If change volume size manually (not w/ cinder) will cause error deleting.


Glance
======

.. image:: images/glance_image_status_transition.png
    :width: 350px

.. code-block:: bash
    :linenos:

    glance image-create --name=<NAME> --store=<STORE> --disk-format=<DISK_FORMAT> \
        --container-format=<CONTAINER_FORMAT> --file=<FILE> --is-public=True [--min-disk=<DISK_GB>]
    glance image-download --file=<OUTPUT_FILE> [--progress] <ImageID>


Sahara
======
 

Neutron
=======

.. sidebar:: Terms

    * **dnsmasq** -- Daemon that provides DNS, DHCP, BOOTP, and TFTP services for virtual networks.

Congiuration Files
------------------

* **/etc/neutron/dhcp_agent.ini** -- configuation file for dhcp_agent service
    * ``dnsmasq_config_file = /etc/neutron/dnsmasq-neutron.conf``
* **/etc/neutron/dnsmasq-neutron.conf** -- self assigned dnsmasq conf file
    * ``dhcp-option-force=26,1400``    # this change will not affect cirros instance's mtu size




Developers
==========

Launchpad bug status
--------------------

================== ================================
Name               Description
================== ================================
New                Not looked at yet.
Incomplete         Cannot be verified, the reporter needs to give more info.
Opinion            Doesn't fit with the project, but can be discussed.
Invalid            Not a bug. May be a support request or spam.
Won't Fix          Doesn't fit with the project plans, sorry.
Confirmed          Verified by someone other than the reporter.
Triaged            Verified by the bug supervisor.
In Progress        The assigned person is working on it.
Fix Committed      Fixed, but not available until next release.
Fix Released       The fix was released.
================== ================================


Terminologies
=============

| **sheepdog** -- opensourcs project, developed by NTT, design for vm's storage.
| **fuel** -- auto deploy openstack enviroment
| **murano**-- auto install openstack plugin
| `ceilometer quick start <https://www.rdoproject.org/CeilometerQuickStart>`_
|


Resources
=========

`OpenStack useage statistics <http://superuser.openstack.org/articles/openstack-users-share-how-their-deployments-stack-up>`_


.. [#] https://wiki.openstack.org/wiki/Heat
