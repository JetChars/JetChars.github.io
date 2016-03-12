=========================
Ceph Management Platforms
=========================


Intro
=====

Till now I've found 6 opensrc Ceph Mangement Platforms, I'll pick up 3 of them to compare, in order to save our precious time. cause I think w/ these 3 management platform we can tell what do we want.

they are: Calamari, ceph-dash, VSM, inkscope, krakendash, ceph-web
ranked by watch+star+fork numbers.


notice ceph-dash only support monitoring, added here for comparison.





Comparion
---------




============== =========== ============= ========== ============  
Item           Calamari    ceph-dash     VSM        inkscope      
============== =========== ============= ========== ============  
hotness        66,175,116  36,128,46     50,82,57   38,82,36     
license        LGPL2.1     MIT-          Apache v2  Apache v2    
language       python      python/JS     python     python       
web_engine     django                    django     Apache/flask 
DB             postgreSQL                MySQL      mongoDB      
Backing        RedHat      Chri./Eich.   Intel      Orange Labs
Latest V.
Release D.     Sep 2014    Dec 2014      Jan 2015   Feb 2015
Capabilities   Mon & LConf Mon           Mon & Conf Mon & LConf
Compatability  wide        wide          limited    wide
============== =========== ============= ========== ============  


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
Daemons        OSD only    Y          N
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
