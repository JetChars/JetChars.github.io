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
    - bad cephfs no big move recently
    - write-all-read-one will cause bad performance when writing w/ disk failure
    - supervised by redhat and contributed mostly by them
    - multiple OSDs in a single host, if host down, tons of PG will be affecte
    - upper limited of single cluster
    - rgw index pool bad performance, even w/ SSD


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


pg states
---------

- creating -- pg under creating
- active -- can process r/w or other operations
- clean -- make the full reps of objs
- down -- the pg is offline
- replay -- waiting for client to replay op after an OSD crashed
- splitting -- splitting 1 pg into multi pg
- scrubbing -- cheking for inconsistencies
- degraded -- not have enough reps
- inconsistent -- wrong size, missing, etc.
- peering -- OSDs not reached a consensus
- repair -- repairing inconsistencies
- recovering -- migrating/synchronizing objs and their reps
- backfill -- scanning and synchronizing the entire pg from the logs for recent op. (special recovering)
- wait-backfill -- wait for backfill
- backfill-toofull -- waiting because the dest OSD is over full ratio
- incomplete -- have unhealthy copies, can solve by start failed OSD to temporary meet the condition of **min_size**.
- stale -- pg is in an unknow state
- remapped -- pg is temporarily mapped to a diff set of OSDs
- undersized -- pg have fewer copies than configured pool rep level
- peered -- pg has peered, but not reach **min_size**





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
Acting Set                                              Ceph OSD Daemons that are currently responsible for the PG
Up Set                                                  OSDs in the Acting Set is up
Primary OSD                                             OSD in a PG, that client will talk w/
Cache Tier                                              provides ceph clients w/ better I/O performance
=========================================== =========== ===================================================================


Architecture
============
============

Cephx
-----

It helps ceph to authenticate users and daemons, but not address data encription in transport.

- both client and monitors have a copy of clients's key
- 

.. image:: /images/ceph/cephx_1.png
    :align: right
    :width: 310px

- user creation
    - client.admin user invokes ``ceph auth get-or-crete-key`` from cli, to generate a username and secret key.
    - ceph's auth subsystem gen the uname&key, store them in MONs and transmit back to client.admin




.. image:: /images/ceph/cephx_2.png
    :align: right
    :width: 310px


- auth w/ MON
    - client passes in the uname to MON
    - MON gen a session key and encrypts it w/ client's key.
    - MON sent session key to client
    - client request a ticket signed w/ previous session key
    - MON gen a ticket encrypts w/ client's key.
    - client decrypts encrypted ticket




.. image:: /images/ceph/cephx_3.png
    :align: right

- ticket will can be expired
- this ticket will be shared w/ OSDs, MDSs and MONs
- client comm w/ ceph nodes by signing this ticket on each msg.




Erasure Coding
--------------


Interrupted Full Writes
^^^^^^^^^^^^^^^^^^^^^^^

- last_compelete -- a pointer to locate data positions
- Data chunck -- stroage 1/k part of data
- Coding chunck -- storage erasure coding data
- WRITE FULL -- payload is to replace the object entirely instead of overwriting a portion of it.
- Primary OSD -- responsible for storing chunks in addition to handling write operations and maintaining an authoritative verion of PG log to reflect the changes.

In the following diagram, k=2 and m=1, D1v1 means Data chunck 1 version 1, similarily C1v1 means Coding chunck number 1 version 1.


.. image:: /images/ceph/interrupted_full_write_1.png
    :align: left
    :width: 208px

.. image:: /images/ceph/interrupted_full_write_2.png
    :align: left
    :width: 208px

.. image:: /images/ceph/interrupted_full_write_3.png
    :align: left
    :width: 208px


|
|
| OSD1 is the primary and receives a **WRITE FULL** from a client (pic2,3)
| v2 of obj is created to override v1 (pic2,3,4,5,6)
| OSDs will create an entry (i.e. epoch1, v2) to its logs as soon as data chunck stored. (pic2)
|


.. image:: /images/ceph/interrupted_full_write_4.png
    :align: left
    :width: 208px

.. image:: /images/ceph/interrupted_full_write_5.png
    :align: left
    :width: 208px

.. image:: /images/ceph/interrupted_full_write_6.png
    :align: left
    :width: 208px


|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| If all goes well, last_compelte will be pointed to new version of data (1,1 --> 1,2), and erase old version of data. (pic4)
| If OSD1 goes down and ther is only one chunck of verion 2 is written, OSD4 will take over OSD1's job, find **last_complete** log entry, will restore object to latest edition(1,1). mean while discard data chunck of v2 at OSD3. (pic5,6)
|
|
|
|



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
