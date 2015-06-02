=========
OpenStack
=========

`wiki <https://wiki.openstack.org/wiki/Main_Page>`_


Nova
====

`nova-docker <https://wiki.openstack.org/wiki/Docker>`_
-----------

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

.. sidebar:: Overview

    - PTL: Mike Perez
    - Since Folsom, Cinder has replaced Nova-Volume as default block storage service.
    - compare to swift, cinder could provide real time read/write, like a mobile disk
    - it's much cheaper to create a volume than an instance
    - severely rely on RabbitMQ



Architecture
============

Components
----------

- **API node** -- provide RESTful API
- **Schedule node** -- communicate between API node & volume node, API node & schedule node normally in same host
- **Volume node** -- provede storage space

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


Terminologies
=============

| **volume type** -- a type or label can be selected at vol creation time, maps to a set of capabilities of the storage back-end driver to be used for this vol
| **sheepdog** -- opensourcs project, developed by NTT, design for vm's storage.
| **fuel** -- auto deploy openstack enviroment
| **murano**-- auto install openstack plugin
|


Resources
=========

`OpenStack useage statistics <http://superuser.openstack.org/articles/openstack-users-share-how-their-deployments-stack-up>`_


.. [#] https://wiki.openstack.org/wiki/Heat
