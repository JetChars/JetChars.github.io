=========
OpenStack
=========

`wiki <https://wiki.openstack.org/wiki/Main_Page>`_


`nova-docker <https://wiki.openstack.org/wiki/Docker>`_
-----------


`Cinder <https://wiki.openstack.org/wiki/Cinder>`_
======

1. Overview

Program Team Leader: Mike Perez

Since Folsom, Cinder has replaced Nova-Volume as default block storage service.


2. Storage backend

- Local: lvm
- Network: NFS, ceph RBD (RADOS), sheepdog

3. Terminologies

| **volume type** -- a type or label can be selected at vol creation time, maps to a set of capabilities of the storage back-end driver to be used for this vol
| **sheepdog** -- opensourcs project, developed by NTT, design for vm's storage.
|


