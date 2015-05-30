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


1. Dependency

- **apache2** -- apache web server
- **memcache** -- mem-cache-d，is a free memory caching system, speed up dynamic database-driven website by caching data in RAM
- **django** -- python based web framework

2. Refresh horizon
   
.. code-block:: bash

   sudo service {apache2,memcached} restart

`Cinder <https://wiki.openstack.org/wiki/Cinder>`_
======

.. sidebar:: Overview

    - PTL: Mike Perez
    - Since Folsom, Cinder has replaced Nova-Volume as default block storage service.


1. Storage backend

- Local: lvm
- Network: NFS, ceph RBD (RADOS), sheepdog

2. Terminologies

| **volume type** -- a type or label can be selected at vol creation time, maps to a set of capabilities of the storage back-end driver to be used for this vol
| **sheepdog** -- opensourcs project, developed by NTT, design for vm's storage.
|



.. [#] https://wiki.openstack.org/wiki/Heat
