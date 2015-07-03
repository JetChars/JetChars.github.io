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


AWS -- Amazon Web Services
==========================


Data Pipeline
-------------

* **Pipeline** -- specifies the business logic for data processing(graphical, more complex situation can be edit w/ sdk)
    * can be export as a json file
    * status -- Active/Pending
    * need a task runner(ec2?)
* **Activities** -- the work to perform (HadoopActivity, PigActivity, EmrActivity,ShellCommandActivity...)
* **Data nodes** -- the locations and type of data (input/output)
* **Scheduler** -- time & frequency to run a job(Activity)
* **Resources** -- ec2resources, emrcluster
* **Precondiction**  -- if file exist or any other situation mathches will run disgnated job.



EMR -- Managed Hadoop Framework
-------------------------------


.. sidebar:: Terms

    * Nodes
        * Master Node -- N&J
        * Core Nodes -- C&D
        * Task Nodes(optional) -- C
    * Cluster
    * Steps -- EMR's working logic

* **EMR** -- Elastic MapReduce, managed hadoop framework
    * can integration w/ other amazon services
    * can be scale up
    * use mins to provisioning cluster




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
=========================

.. image:: images/ceph.png
    :align: right

Ceph is a free software storage platform designed to present object, block, and file storage from a single distributed computer cluster [#]_

`doc <http://docs.ceph.com/docs/master/>`_

.. image:: images/ceph_components.svg


- rbd -- utility for manipulating rados block device(RBD) images.
- osd -- Object Storage Device, a physical or logical storage unit(eg. LUN), ceph use 'OSD' to refer to Ceph OSD Daemon
- radosgw -- HTTP_REST gateway for RADOS object store



Mesos
=====


DCOS -- One command control of data center services
---------------------------------------------------

Mesosphere Data Center Operating System (DCOS), A new kind of operating system that spans all the servers in a physical or cloud-based data center, and runs on top of any Linux distribution [#]_

`docs <https://docs.mesosphere.com/>`_

Data-center management systems, which is what most data centers now use, focus on controlling physical systems. DCOSs are the next evolutionary step, in that DCOSs can control a data center's logical and physical systems. The University of California, Berkeley research paper `The Datacenter Needs an Operating System (PDF) <http://people.csail.mit.edu/matei/papers/2011/hotcloud_datacenter_os.pdf#ftag=YHF87e0214>`_ describes what a DCOS brings to the table.
- Resource sharing: DCOS can multiplex resources between users of an application and across applications.
- Data sharing: Besides resources, DCOSs traffic data between the necessary applications.
- Programming abstractions: DCOSs provide user interfaces that hide the intricacies of hardware and simplify application development.
- Debugging: Figuring out what massively parallel applications are doing remains one of the hardest challenges in cluster computing: DCOSs use correctness and performance debugging to address the challenges.


.. code-block:: guess
    :linenos:

    dcos   # show available cmds
    dcos marathon start ./demo/rails-app.json
    dcos marathon scale rails-app 15
    docs install hdfs   # other options are kafca, cassandra, spark...
    dcos kafka add 10
    dcos cassandra add 7
    dcos spark run ./demo/spark-job.json    # job in json format
    dcos chaos 5   # kill 5 nodes
    dcos resize 50   # resize cluster to specified size, add nodes in real time




- can run python jave or even container.
- Website is mix w/ cmd lines.
- self healing
- easy to resize
- application can be drag to cmdline(More Services)
- marathon & chronos are preinstalled
    - marathon is netservice, have restful api
    - chronos is shedule service
- kafca -- distributed message queue









Terminologies
=============

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
| **mesos** -- distributed system **for running and building** other distributed system(spark hadoop chronos marathon K8s)
| **ML as a Service** -- Training a model first(input csv files), then predict.

| `aliyun <http://www.aliyun.com>`_
|
|
|

.. [#] http://www.emc.com/collateral/analyst-reports/idc-extracting-value-from-chaos-ar.pdf
.. [#] http://en.wikipedia.org/wiki/Ceph_(software)
.. [#] https://in.news.yahoo.com/mesosphere-dcos-one-command-control-140004850.html
