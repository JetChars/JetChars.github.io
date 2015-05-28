===============
Cloud Computing
===============

* High value data must be structured data, can be transfer from low value data
* Data stored worldwide has been exploded, growing by a factor of 9 in five years (2006~2011) [#]_
* Classification
    * Saas, Software as a Service
    * Paas, Software as a Service
    * Iaas, Software as a Service (old name HaaS)


+-----+---------------+
|Type |Implementations|
+=====+===============+
|SaaS |               |
+-----+---------------+
|PaaS |Docker, GAE    |
+-----+---------------+
|IaaS |OpenStack      |
+-----+---------------+


Docker
======

* Use go language
* Use native cpu/syscall/kernel
* Use ``namespace/capabilities/ctrl group/apparmor/netfilter``
* Use ipc namespace communicate between containers
* Require ``libcontainer/lxc/libvirt/systemd-nspawn``
* Managed by DGAB (Docker Governance Advisory Board)
* Advangtages
    * compare to kvm use virtio, docker use AUFS, which is better.
    * light weight 'vm', use less mem than kvm, closer to BM
* Constrains
    * must have same OS kernel
    * kernel 3.8 is minimal, except rhel 2.6.32, 3.10 or higher is recommended
    * can't over commitment
    * v1.10 can't modify files under /etc, v1.20 solved this issue (mount | grep etc)

Install Docker::

    $ wget -qO- https://get.docker.com/ | sh

* `Kubernetes <http://kubernetes.io>`_ is an open source orchestration system for Docker containers

`Ceph <http://ceph.com>`_
====

.. image:: images/ceph.png
    :align: right

Ceph is a free software storage platform designed to present object, block, and file storage from a single distributed computer cluster [#]_

.. image:: images/ceph_components.svg


Terminologies
=============

| **BM** -- BareMetal == Physical Machine
| **UX** -- User Experence
| **repo** -- Repository
| **ETL** -- Extract Transfer Load
| **BI** -- Business Intelligent
| **JBOD** -- Just a Bunch of Disks
| **i18n** -- internationalization
| **l10n** -- localization
| **k8s** -- kubernetes
| **HBA** -- Host Bus Adapter, HBA card opposite to RAID card
| **IMGO** --In My Humble Opinion
| **volume** -- detachable block storage device

|
|
|
|

.. [#] http://www.emc.com/collateral/analyst-reports/idc-extracting-value-from-chaos-ar.pdf
.. [#] http://en.wikipedia.org/wiki/Ceph_(software)
