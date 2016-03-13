====
Ceph
====

The future of Storage!

Ceph Intro
==========
==========

Ceph can uniquely deliver object, block and file storage in one unified system.

- start since Jun 2004, write w/ C++, now adopted by RedHat
- provide block storage other than gluster
- applications: OpenStack/CloudStack/OpenNebula/Hadoop/Mesos
- urls : `home <http://ceph.com>`_ / `get ceph <http://ceph.com/get>`_ / `quick start <http://ceph.com/qsg>`_ / `docs <http://ceph.com/docs>`_ / `mailing list <http://ceph.com/list>`_ / `irc <http://ceph.com/irc>`_ / `git repo <http://github.com/ceph>`_ /
- peopele are mostly build ceph within private cloud using debian servers [#]_

- advantages
    - CRUSH make sure the consistency
    - Unified storage architecture
    - other features: scalability/replication/balance/rolling upgrade/multi-pool/snapshots

- disadvantages
    - c++ & python, slower and simpler than **c**
    - doubel input, long IO path and bad support for fast storage deviecs(SSD/PCIe SSD/NVRAM)
    - bad cephfs
    - write-all-read-one will cause bad performance when writing w/ disk failure
    - supervised by redhat and contributed mostly by them


ceph releases
-------------

Ceph starts at UCSC, OpenSrc at 2006, Developed by InkTank


.. image:: /images/ceph/ceph_chronicles.png




=============== ============ ======== =========== ======== ========== ==========
Times           Dumpling LTS Emperor  Firefly LTS Giant    Hammer LTS Infernalis
=============== ============ ======== =========== ======== ========== ==========
First release   Aug 2013     Nov 2013 May 2014    Oct 2014 Apr 2015   Nov 2015
Est. retirement Mar 2015              Jan 2016             Nov 2016   Jun 2016
Act. retirement May 2015     May 2014             Apr 2015
=============== ============ ======== =========== ======== ========== ==========

features
--------

- thin provisioning
- copy on read for librbd
- clustered MDS -- diff MDS will cover diff subtree of CephFS
- health check -- MON will ping osd nodes periodly, and OSDs also can report it's and peer's status to MON
- scrubing -- daily light check file zize & attr. weekly deep check with checksum
- no centralize access point -- client contact Primary OSD directly


Architecture
============
============





Glossariy
=========
=========

=========================================== =========== ===================================================================
name                                        abbr.       description
=========================================== =========== ===================================================================
Reliable Autonomic Distributed Object Store RADOS       self-healing,self-managing, inteligence storage include(OSD&MON)
RADOS Gateway                               RADOSGW/RGW manage object store
RADOS Block Device                          RBD         include KRBD for CephFS, and LIBRBD for dirct use of block device
Ceph FileSystem                             CephFS      a shared filesystem
Ceph Release Candidate                      Ceph RC     will be released but under testing and debuging
Monitor                                     MON         
Object Storage Device                       OSD         
Metadata Server                             MDS         
Controlled Replication Under Scalable Hash  CRUSH       Core Algorithm of Ceph
Paxos/Quorum                                            algorithm make sure the consistency of distribution system
Cephx                                                   authentication protocol, operates like kerberos, w/o SPoF
Pool                                                    logical partitions for storing objs
Placement Group                             PG          
Primary OSD                                             OSD in a PG, that client will talk w/
=========================================== =========== ===================================================================


Architecture
============
============

Cephx
-----



Erasure Coding
--------------


Scrubbing
---------



CRUSH
-----








References
==========
==========


.. [#] http://ceph.com/community/results-from-the-ceph-census/
.. [#] https://www.ustack.com/blog/ceph_infra/
.. [#] https://www.ustack.com/blog/ceph-distributed-block-storage/#2_Ceph
