=================
Ceph 管理监控平台
=================


介绍
====

到目前为止，在网上一共找到了6款开源的Ceph管理平台，为了节约我们的时间，为将挑出其中的3款进行比较。通过对比这三款管理平台我们基本上能够大体了解目前Ceph管理平台的现状。

- 这6个Ceph管理平台按在github上面的热度排序（watch+star+fork）： 
    - Calamari，Ceph-dash，VSM，InkScope，krakendash以及Ceph-web。
    - 其中Ceph-dash仅支持Ceph集群的监控，并不支持管理。在后文中将用作监控指标的对比。


Calamari
--------

- Repos
    - 服务端： https://github.com/ceph/calamari
    - 客户端： https://github.com/ceph/calamari-clients

- 这个项目是由InkTank发起的
- 在2014年5月被开源
- 主要被用来当做Ceph的诊断工具
- 提供了以一个相对高级的REST API，而不是使用Ceph-rest-api
    - 简化了ceph系统的管理
- 目前仅提供debian Trusty版本的软件，替他版本需要用户自行编译。


.. image:: /images/ceph/calamari/summary.jpeg

- 仪表板
    - 可以查看系统的健康信息：集群的健康信息、OSD、MON、POOLs、PG、
    - 可以查看系统资源的使用：实时的IOPS、存储容量及其使用率。（IOPS、USAGE目前无法正常显示）

.. image:: /images/ceph/calamari/Main_Dashboard.png

- workbench shows PG & OSD stats, can sort by OSD or HOST

.. image:: /images/ceph/calamari/workbench_with_pg_state_filtering.png

- graph shows

.. image:: /images/ceph/calamari/Graph_UI.png


- default mgmt view can tag cluster stats

.. image:: /images/ceph/calamari/manage_default_view.png

- OSDs grouped into diff HOSTs

.. image:: /images/ceph/calamari/manage_OSD_hosts_view.png

- manage OSD
    - scrubbing -- scrub, deep scrub
    - tagging OSDs -- tag down/out

.. image:: /images/ceph/calamari/manage_OSDS_by_host.png

- manage pool
    - change name
    - change reps
    - change PG number
    - switch crush-rule
    - del pool

.. image:: /images/ceph/calamari/manage_pool_view.png


- server side (backend)
    - composed of:  Apache, salt-master , supervisord , cthulhu , carbon-cache
    - newer version provide a compelte new REST API(old based on Ceph REST API), abstract the ops of CEPH API, convient for people not know CEPH deeply.
- client side (frontend)
    - Web UI primary in JS uses the Calamari REST API
- ceph nodes
    - composed of -- salt-minion , diamond
    - diamond -- collect monitoring datas, support over 90 kinds of info. report to graphite.
- manage cluster using cthulhu and saltstack
- monitoring using graphite and diamond

.. image:: /images/ceph/calamari/calamari_architecture.jpg






installation
^^^^^^^^^^^^

- Requirements: ceph-deploy and it's env



.. code-block:: shell

    # add repo, install dependency and install calamari
    # =================================================
    echo "deb http://download.ceph.com/calamari/1.3.1/ubuntu/trusty/ trusty main" >> /etc/apt/source.list.d/ceph.list
    sudo apt-get update && sudo apt-get install -y apache2 libapache2-mod-wsgi libcairo2 supervisor python-cairo libpq5 postgresql
    sudo apt-get install calamari-* -y
    sudo chmod a+w /var/log/calamari/cthulhu.log   # can't access by default

    # install ceph nodes
    # ==================
    sudo apt-get install python-dev python-pip git -y  # prerequsite to install diamond
    git clone -b calamari https://github.com/ceph/diamond/
    sudo pip install diamond/

    # initialize calamari and conn to ceph nodes
    sudo calamari-ctl initialize
    echo ``auto_accept: True`` >> /etc/salt/master   # make sure salt master auto accept the conn request
    ceph-deploy calamari connect <ceph nodes>

    # kill all salts
    kill `ps aux | grep salt | awk '{print $2}'`   # kill all salt in a single server



.. code-block:: console

    $ sudo calamari-ctl initialize
    [INFO] Loading configuration..
    [INFO] Starting/enabling salt...
    [INFO] Starting/enabling postgres...
    [INFO] Updating database...
    [INFO] Initializing web interface...
    [INFO] Starting/enabling services...
    [INFO] Updating already connected nodes.
    [INFO] Restarting services...
    [INFO] Complete.

    $ 


- issues
    - errors can be shown in /var/log/calamari/calamari.log
    - query calamari issuses (some function not realized)-- http://tracker.ceph.com/projects/calamari/issues
    - **can't open log/config file** -- ``sudo chmod 777 /var/log/calamari/ -R``
    -  **Master hostname: salt not found**  -- debug w/ ``salt-minion -l debug``
    - **Cluster Updates Are Stale. The Cluster isn't updating Calamari. Please contact Administrator** -- solution can't access from redhat website!
    - **diamond can't start** -- default conf call the path of diamond ``/usr/bin/diamond``, real path is ``/usr/local/bin/diamond``, create a link file to solve this issue
        - ``mkdir /usr/share/diamond/collectors/ -p``
        - ``mkdir /var/log/calamari/``
        - ``scp /etc/diamond/* root@192.168.56.111:/etc/diamond``
        - ``scp /usr/share/diamond/* root@192.168.56.111:/usr/share/diamond``
        - ``ln -sf /usr/local/bin/diamond /usr/bin/diamond``
        - ``nohup /usr/bin/python /usr/local/bin/diamond --foreground --skip-change-user --skip-fork --skip-pidfile &``
    - **diamond not report** -- ``/var/lib/graphite/index`` in thisfile we can tell all observation entries
        - ``netstat -tunpla | grep `ps aux | grep diamond | awk '{print $2}' | head -n1```  -- all nodes connected
    - **salt.loaded.int.module.cmdmod**
    - dump whisper data -- ``/opt/calamari/venv/bin/whisper-dump.py /var/lib/graphite/whisper/servers/ceph-osd2/diskspace/root/byte_used.wsp | less``




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
.. image:: /images/ceph/vsm_architecture.png

- VSM Controller -- conn to Agents and NovaCtrl
    - WebUI, REST API
    - mariadb, rabbitmq
- VSM Agent -- runs on every ceph node, pass conf&stats info to controller

.. image:: /images/ceph/vsm_net.png

- nothing special
    - mgmt network
    - ceph pub network
    - ceph cluster network

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



Installation
^^^^^^^^^^^^

- requirements
    - OS: Ubuntu Server 14.04.2/CentOS 7 Server Basic
    - Ceph: Firefly/Giant/Hammer/Infernalis
    - OpenStack: Havana/Icehouse/Juno/Kilo/Liberty
    - at least 3 storage nodes
    - passwd-less ssh
    - will sync ``/etc/hosts`` on each nodes

- note
    - will disable selinux





Inkscope
--------

https://github.com/inkscope/inkscope

- Ceph visualiztion and operation through CLI [#]_
- Open Source
- Use Ceph RESTful API
- Modularity and simplicity

.. image:: /images/ceph/ceph_inkscope.png

- inkscopeViz 
    - Web client 
- inkscopeCtrl
    - Server part 
    - Provides an advanced REST API
- inkscopeProbe
    - Collects system and ceph infos 
    - Feeds a mongoDB database
- inkscopeMonitor (not developed)
    - Monitoring of Ceph metrics stored in db
    - Feeds monitoring tools like Nagios


.. image:: /images/ceph/inkscope_architecture.png





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



============= ============= =========== ============= ============ 
Item          Calamari      ceph-dash   VSM           inkscope     
============= ============= =========== ============= ============ 
hotness       66,175,116    36,128,46   50,82,57      38,82,36     
license       LGPL2.1       MIT-        Apache v2     Apache v2    
language      python/JS     python/JS   python        python       
web_engine    Apache/django Apache      Apache/django Apache/flask 
js_lib        AngularJS                               AngularJS
css           bootstrap                               bootstrap
DB            postgreSQL    InfluxDB    MySQL         mongoDB
Backing       RedHat        Chri./Eich. Intel         Orange Labs
Capabilities  Mon & LConf   Mon         Mon & Conf    Mon & LConf
Compatability wide          wide        limited       wide
============= ============= =========== ============= ============

============== =========== ============= ========== ========  
Item           Calamari    ceph-dash     VSM        inkscope  
============== =========== ============= ========== ========  
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
============== =========== ============= ========== ========  


============== =========== ========== ========  
Item           Calamari    VSM        inkscope  
============== =========== ========== ========  
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
============== =========== ========== ========  




- Notice
    - hotness include watch,star,fork of 2016/3/9
    - krakendash has modified the MIT license
    - these comp infos derived from internet, not up to date.



参考文献
========
========



.. [#] https://01.org/virtual-storage-manager/documentation/vsm-0.5.1-training-slides
.. [#] http://www.slideshare.net/alaindechorgnat/inkscope-ceph-day-paris-final?qid=24a1a418-b01c-4f91-b718-f26cffe920b7&v=&b=&from_search=1
.. [#] http://www.slideshare.net/DaystromTech/ceph-days-sf2015-paul-evans-static?qid=4398eec4-e73a-4483-8e47-61f9875872d3&v=&b=&from_search=2
.. [#] http://calamari.readthedocs.org/en/latest/operations/index.html
.. [#] http://ceph.com/category/calamari/
.. [#] http://ceph.com/planet/ceph-calamari-the-survival-guide/
.. [#] http://www.openstack.cn/?p=2708
