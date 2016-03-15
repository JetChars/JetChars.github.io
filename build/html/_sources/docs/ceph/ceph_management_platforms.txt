=========================
Ceph Management Platforms
=========================


Intro
=====

Till now I've found 6 opensrc Ceph Mangement Platforms, I'll pick up 3 of them to compare, in order to save our precious time. cause I think w/ these 3 management platform we can tell what do we want.

Management Paltforms: Calamari, ceph-dash, VSM, inkscope, krakendash, ceph-web
(ranked by watch+star+fork numbers).

notice ceph-dash only support monitoring, added here for the comparisonof monitoring.






Calamari
--------

https://github.com/ceph/calamari
https://github.com/ceph/calamari-clients

- start by inktank
- opensrc since May 2014
- present as diagnostic tool
- exposing a high level REST API
- precompiled pkgs not available(in ubuntu vagrant)
- server side (backend)
    - composed of:  Apache, salt-master , supervisord , cthulhu , carbon-cache
    - newer version provide a compelte new REST API(old based on Ceph REST API)
- client side (frontend)
    - Web UI primary in JS uses the Calamari REST API
- ceph clients
    - composed of: salt-minion , diamond

``deb http://download.ceph.com/calamari/1.3.1/ubuntu/trusty/ trusty main``



.. image:: /images/ceph/ceph_calamari_summary.png
.. image:: /images/ceph/ceph_calamari_osds.png





Virtual Storage Manager
-----------------------

https://github.com/01org/virtual-storage-manager

- Intel VSM v0.5.1 [#]_
    - WebUI for cluster management, monitoring and troubleshooting
    - Server management -- Organize servers and disks
    - Cluster management -- Manages cluster/pool creation
    - OpenStack interface -- conn pools to OpenStack
    - VSM administration -- User/Passwd

.. image:: /images/ceph/vsm_arch.png

- VSM Controller -- WebUI, API, conn to Agents and NovaCtrl
- VSM Agent -- runs on every ceph node, pass conf&stats info to controller

.. image:: /images/ceph/vsm_net.png

- nothing special

.. image:: /images/ceph/vsm_disks.png


- VSM concepts
    - Storage Class -- Drivers w/ similar performance characteristics
    - Storage Group -- Drivers w/ same Storage Class grouped together

.. image:: /images/ceph/vsm_fd.png

- Servers can grouped into failure domains(call **Zone** in VSM)


.. image:: /images/ceph/vsm_nav_bar.png

- Monitoring
    - using ceph client
        - ``ceph -s``
        - ``ceph pg dump osds``
        - ``ceph pg dump pgs_brief``
        - ``ceph osd pool stats``
        - ``ceph osd dump``
        - ``ceph osd tree``
        - ``ceph mds dump``
        - ``rbd ls -l {pool name}``
    - status: StorageGroup, RBD, OSD, MON, PG, MDS, Capacity, IOPS, throughput, ERR, WRN
        - detect OSDs not running, near full or full
        - identifying ntp latency err
- Managing
    - create pools,add/rm/stop/start OSDs, add/rm MON
        - stop w/o rebalancing
    - ssh2nova_ctrl, expose pools to OpenStack
    - vsm account mgt





Inkscope
--------

https://github.com/inkscope/inkscope

- Ceph visualiztion and operation through CLI [#]_
- Open Source
- Use Ceph RESTful API
- Modularity and simplicity

.. image:: /images/ceph/ceph_inkscope.png


Ceph-dash
---------

https://github.com/Crapworks/ceph-dash

.. image:: /images/ceph/ceph_dash.png



Krakendash
----------

https://github.com/01org/virtual-storage-manager


Ceph-web
--------

https://github.com/tobegit3hub/ceph-web


Comparison
==========
==========



============== ============= =========== ========== ============  
Item           Calamari      ceph-dash   VSM        inkscope      
============== ============= =========== ========== ============  
hotness        66,175,116    36,128,46   50,82,57   38,82,36     
license        LGPL2.1       MIT-        Apache v2  Apache v2    
language       python/JS     python/JS   python     python       
web_engine     Apache/django Apache      django     Apache/flask 
DB             postgreSQL    InfluxDB    MySQL      mongoDB      
Backing        RedHat        Chri./Eich. Intel      Orange Labs
Capabilities   Mon & LConf   Mon         Mon & Conf Mon & LConf
Compatability  wide          wide        limited    wide
============== ============= =========== ========== ============  


============== =========== ============= ========== ============  
Item           Calamari    ceph-dash     VSM        inkscope      
============== =========== ============= ========== ============  
MON Stats      Y           Y             Y          Y
OSD Stats      Y           Y             Y          Y
MDS Stats      N           N             Y          Y
PG Stats       Y           Y             Y          Y
Host Stats     Y           Y             Y          Y
OSD-host-M     Y           Y             Y          Y
PG-OSD-M       N           N             N          Y
Capacity       Y           Y             via Groups Y
Throughput     N           Y             Y          Y
IOPS           Y           Y             Y          Y
ERR/WRN        Y           Y             Y          Y
view logs      Y           N             N          N
send email     N           w/ nagios     N          N
charts/G       Y           w/ nagios     N          N
============== =========== ============= ========== ============  


============== =========== ========== ============  
Item           Calamari    VSM        inkscope      
============== =========== ========== ============  
Deploy Cluster N           Y          N
Deploy Hosts   N           Y          N
D. Storage G.  N           Y          N
set Daemons    OSD only    Y          N
set ops flags  Y           N          Y
set parametrs  Y           N          view
set crush      N           partial    view
set EC         N           Y          Y
OSD            partial     Y          Y
Pools(Rep)     limited     Y          Y
Pools(EC&Teir) N           Y          partial
RBDs           N           partial    N
S3/Swift/...   N           N          Y
link to Nova   N           Y          N
============== =========== ========== ============  




- Notice
    - hotness include watch,star,fork of 2016/3/9
    - krakendash has modified the MIT license
    - these comp infos derived from internet, not up to date.



References
==========
==========



.. [#] https://01.org/virtual-storage-manager/documentation/vsm-0.5.1-training-slides
.. [#] http://www.slideshare.net/alaindechorgnat/inkscope-ceph-day-paris-final?qid=24a1a418-b01c-4f91-b718-f26cffe920b7&v=&b=&from_search=1
.. [#] http://www.slideshare.net/DaystromTech/ceph-days-sf2015-paul-evans-static?qid=4398eec4-e73a-4483-8e47-61f9875872d3&v=&b=&from_search=2
.. [#] http://calamari.readthedocs.org/en/latest/operations/index.html
.. [#] http://ceph.com/category/calamari/
.. [#] http://ceph.com/planet/ceph-calamari-the-survival-guide/
