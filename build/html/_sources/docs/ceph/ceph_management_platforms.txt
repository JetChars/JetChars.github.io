=========================
Ceph Management Platforms
=========================


Intro
=====


Comparion
---------
    

========== =========== ============= ========== ============= ========== ======== 
Item       Calamari    ceph-dash      VSM       inkscope      krakendash ceph-web
========== =========== ============= ========== ============= ========== ======== 
hotness    66,175,116  36,128,46      50,82,57   38,82,36      20,54,23   2,9,2
license    LGPL2.1     MIT-           Apache v2  Apache v2     MIT        MIT
language   python      python/JS      python     python        python     go
web_engine django                     django     Apache/flask  django     smarty
DB         postgreSQL                 MySQL      mongoDB       sqlite3    N/A
dashboard  yes
Vis. OSD   yes
Vis. Host  yes
Vis. PG    yes
Vis. CMap  no
Vis. Objs  no
Gra. Clst  yes
Gra. P IO  yes
Gra. Host  yes
feature                                                                   docker
========== =========== ============= ========== ============= ========== ======== 


- Monitoring

========== =========== ============= ========== ============= ========== ======== 
Item       Calamari    ceph-dash      VSM       inkscope      krakendash ceph-web
========== =========== ============= ========== ============= ========== ======== 
========== =========== ============= ========== ============= ========== ======== 

- Monitoring

========== =========== ============= ========== ============= ========== ======== 
Item       Calamari    ceph-dash      VSM       inkscope      krakendash ceph-web
========== =========== ============= ========== ============= ========== ======== 
========== =========== ============= ========== ============= ========== ======== 






- Notice
    - hotness include watch,star,fork of 2016/3/9
    - krakendash has modified the MIT license
    - these comp infos derived from internet, not up to date.



Calamari
--------

`gitrepo <https://github.com/ceph/calamari>`_

- start by inktank
- opensrc since May 2014
- present as diagnostic tool
- 4 modules
    - calemari-web
    - cthulhu
    - salt-master
    - rest-api




Virtual Storage Manager
-----------------------

`gitrepo <https://github.com/01org/virtual-storage-manager>`_


Inkscope
--------

`gitrepo <https://github.com/inkscope/inkscope>`_

- Ceph visualiztion and operation through CLI [#]_
- Open Source
- Use Ceph RESTful API
- Modularity and simplicity

Modules
^^^^^^^

Functions
^^^^^^^^^






Krakendash
----------

`gitrepo <https://github.com/01org/virtual-storage-manager>`_


Ceph-web
--------

`gitrepo <https://github.com/tobegit3hub/ceph-web>`_



.. [#] http://www.slideshare.net/alaindechorgnat/inkscope-ceph-day-paris-final?qid=24a1a418-b01c-4f91-b718-f26cffe920b7&v=&b=&from_search=1
