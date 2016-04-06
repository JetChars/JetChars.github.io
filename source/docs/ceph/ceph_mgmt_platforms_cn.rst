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


图形界面
^^^^^^^^

.. image:: /images/ceph/calamari/summary.jpeg

- 仪表板
    - 可以查看系统的健康信息：集群的健康信息、OSD、MON、POOLs、PG、
    - 可以查看系统资源的使用：实时的IOPS、存储容量及其使用率。（IOPS、USAGE目前无法正常显示）

.. image:: /images/ceph/calamari/Main_Dashboard.png

- 工作台
    - 以田字格的样式展示了OSD的状态汇总信息
    - 可以按OSD或者其宿主机进行分类
    - 可以通过OSD或PG的状态对OSD进行过滤

.. image:: /images/ceph/calamari/workbench_with_pg_state_filtering.png

- 集群性能实时监控
    - 显示CPU、磁盘、网络的监控信息
    - 按集群、pool分类的综合监控信息无法正常显示

.. image:: /images/ceph/calamari/Graph_UI.png

- 集群管理
    - 集群配置文件的查询
    - 集群tag管理

.. image:: /images/ceph/calamari/manage_default_view.png

- OSD管理
    - OSD按宿主机进行分组
    - 查看OSD信息
    - Scrub、Deep Scrub
    - 设置为down或out

.. image:: /images/ceph/calamari/manage_OSD_hosts_view.png
.. image:: /images/ceph/calamari/manage_OSDS_by_host.png

- Pool管理
    - 添加、删除pool
    - 修改pool配置：name、reps、PGs、选择Ruleset

.. image:: /images/ceph/calamari/manage_pool_view.png


系统介绍及架构
^^^^^^^^^^^^^^

- Calamri服务端
    - 包含组件：Apache、Salt-master、supervisord、cthulhu、carbon-cache、graphite、whisper
    - carbon-cache将ceph node传来的数据存入顺序存储数据库whisper
    - graphite-web将whisper中接受到的数据进行绘图
    - 通过cthulhu对saltstack进行管理，但是主要还是通过直接调用salt-master
    - 基于Ceph REST API提供了以一个相对高级的REST API，对其操作进行了抽象
    - 对ceph node提供yum源
- Calamari客户端
    - 提供web图形化界面
    - 基于bootstrap的响应式布局
    - 由AngularJS编写的多个SAPs组成
    - JS通过调用Calamari REST API对服务端进行管理
- ceph节点
    - ceph集群中的每一个节点都包含：salt-minion以及diamond
    - salt-minion用于ceph节点的管理
    - diamiond用于ceph节点的监控，并将监控信息汇报给控制节点的Carbon-cache

.. image:: /images/ceph/calamari/calamari_architecture.jpg


安装
^^^^

- 环境需求: 使用Ceph-deploy安装配置好的Ceph集群。



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


- issues
    - log文档位置 -- ``var/log/calamari/calamari.log``
    - 追踪calamari isues -- http://tracker.ceph.com/projects/calamari/issues
    - 可能需要手动配置的部分
        - **can't open log/config file** -- ``sudo chmod 777 /var/log/calamari/ -R``
        -  **Master hostname: salt not found**  -- debug w/ ``salt-minion -l debug``
        - **Cluster Updates Are Stale. The Cluster isn't updating Calamari. Please contact Administrator** -- 与宿主机同步时间（在宿主机中启动ntp server）
        - **diamond can't start** -- diamond的执行路径不正确 ``/usr/bin/diamond``, 实际的路径 ``/usr/local/bin/diamond`` -- 通过创建一个软连接解决这个问题 ``ln -sf /usr/local/bin/diamond /usr/bin/diamond``
        - 手动创建collector所在的路径 -- ``mkdir /usr/share/diamond/collectors/ -p``
        - 手动从创建calamari的日志文件夹 -- ``mkdir /var/log/calamari/``
        - 拷贝diamond配置文件到ceph节点 -- ``scp /etc/diamond/* root@192.168.56.111:/etc/diamond`` ``scp /usr/share/diamond/* root@192.168.56.111:/usr/share/diamond``
        - 手动启动diamond守护进程 -- ``nohup /usr/bin/python /usr/local/bin/diamond --foreground --skip-change-user --skip-fork --skip-pidfile &``
    - **diamond not report** -- 同过查看这个文档判断diamond的传输到whisper数据库中的数据列表 ``/var/lib/graphite/index``
    - 查看whisper中存储的数据 -- ``/opt/calamari/venv/bin/whisper-dump.py /var/lib/graphite/whisper/servers/ceph-osd2/diskspace/root/byte_used.wsp | less``




Virtual Storage Manager
-----------------------

https://github.com/01org/virtual-storage-manager

- Intel VSM v2.0



图形化界面
^^^^^^^^^^


- 仪表盘
    - 查看vsm、cluster、storage group、OSD、MON、MDS、PG的状态统计信息
        - 可以判断OSD是否正常运作，空间是否满
    - 查看IOPS、latency、bandwidth、CPU实时监控信息(通过diamond实现数据的收集)
        - 可以用来发现ntp延迟的问题

.. image:: /images/ceph/vsm/vsm_dashboard.PNG


- vsm管理工具
    - 所有的宿主节点都需要在安装vsm的时候写在配置文件中
    - 添加删除MON/OSD 守护进程
    - OSD 增删、重启、恢复（N/A）
    - osd pool的管理 -- 支持cache tier的增删、replicated/EC pool的创建
    - StorageGroup的管理 -- 添加新的SG，存储资源将以SG为单位进行统计
    - 支持ceph系统的升级功能，通过github下载源码实现
    - 将通过ssh配置openstack的控制节点把**rbd pool** present给cinder
    - 管理系统的临界值，将在dashboard中得到体现
    - vsm 账户管理
      


.. image:: /images/ceph/vsm/vsm_mgmt_devices.PNG
.. image:: /images/ceph/vsm/vsm_mgmt_servers.PNG
.. image:: /images/ceph/vsm/vsm_mgmt_pools.PNG
.. image:: /images/ceph/vsm/vsm_mgmt_sg.PNG
.. image:: /images/ceph/vsm/vsm_mgmt_upgrade.PNG
.. image:: /images/ceph/vsm/vsm_openstack.PNG
.. image:: /images/ceph/vsm/vsm_mgmt_thresholds.PNG

- vsm监控工具
    - 实现的功能非常的简单，通过使用ceph client实现
        - ``ceph -s``
        - ``ceph pg dump osds``
        - ``ceph pg dump pgs_brief``
        - ``ceph osd pool stats``
        - ``ceph osd dump``
        - ``ceph osd tree``
        - ``ceph mds dump``
        - ``rbd ls -l {pool name}``  
 

.. image:: /images/ceph/vsm/vsm_mon.PNG


系统介绍及架构
^^^^^^^^^^^^^^


.. image:: /images/ceph/vsm/vsm_arch.png
    :width: 300px
    :align: right

- VSM 控制节点
    - WebUI -- 通过访问VSM REST API用于集群的管理、监控
    - REST API -- 供vsm client访问
    - mariadb, rabbitmq
- VSM 代理节点
    - 使用diamond收集ceph节点的监控信息
    - vsm-agent工具对ceph节点进行管理
    
.. image:: /images/ceph/vsm/vsm_architecture.png


- VSM推荐使用三个分别的子网进行管理
    - mgmt network
    - ceph pub network
    - ceph cluster network

.. image:: /images/ceph/vsm/vsm_net.png


- VSM 概念
    - Storage Class -- 具有类似存储性能的磁盘分类
    - Storage Group -- 用同一种Storage Class组成的磁盘集合

.. image:: /images/ceph/vsm/vsm_disks.png


- 书主机可以按失效域啊（failure domain）进行划归(在VSM中层位zone)

.. image:: /images/ceph/vsm/vsm_fd.png



安装
^^^^

- 环境需求
    - debian trusty/centos 7 (master branch仅支持centos)
    - ceph版本目前仅支持hammer
    - 安装时需要至少三个空白的宿主机
    - 需要配置无密码登陆ssh

- 提示
    - vsm将同步控制节点的``/etc/hosts``文件到所有的节点
    - vsm将关闭系统的selinux

- ceph节点的准备工作

.. code-block:: shell

    sudo mkdir /loop
    for i in {0..5}; do
        sudo truncate -s 5G /loop/loop$i.img
        sudo losetup /dev/loop$i /loop/loop$i.img
        sudo parted /dev/loop$i -- mklabel gpt
        sudo parted -a optimal /dev/loop$i -- mkpart primary 1MB 100%
    done
    git clone -b http://github.com/01org/vsm-dependencies
    cp vsm-dependencies/ubuntu/* vsm-dep-repo/
    ./install.sh -v 2.0 -u vsm


- vsm控制节点的安装

.. code-block:: shell

    # ceph repo should be added manually
    wget -q -O- 'https://download.ceph.com/keys/release.asc' | sudo apt-key add -
    echo deb http://download.ceph.com/debian-hammer/ $(lsb_release -sc) main | sudo tee /etc/apt/sources.list.d/ceph.list
    git clone -b 2.0 http://github.com/01org/virtual-storage-manager
    cd virtual-storage-manager
    ./buildvsm.sh
    cd release
    tar -xvzf 2.0.0-216.tar.gz
    cd 2.0.0-216     # enter the vsm package
    mkdir manifest/192.168.56.12{0..3}
    cp manifest/{cluster.manifest.sample,192.168.56.120/cluster.manifest}   # then edit it
    cp manifest/{server.manifest.sample,192.168.56.121/server.manifest}   # then edit it
    cp manifest/192.168.56.12{1,2}/server.manifest
    cp manifest/192.168.56.12{1,3}/server.manifest
    ./install.sh -u vsm -v 2.0   # vsm is the username of ceph-nodes
    ./get_pass.sh                # generate admin password, username *admin*
    cat /etc/vsmdeploy/deployrc | grep -i admin_password | cut -d'=' -f2


- issues
    - 依赖包被托管在github上面，且无法通过脚本完成下载。（2015年1月停止更新）
    - ``install.sh -k <path/to/key/file>`` -- keyfile即使使用完整路径也无法找到，需要手动输入cpeh节点的密码几十次（ssh-copy-id也无效）
    - Apache端口80需要手动开启
    - osd 无法启动
        - can't start osd w/ directory or  loopback device.
        - ``ERROR: error creating empty object store in /data11/osd.11: (21) Is a directory``
        - ``ERROR: unable to open OSD superblock on /data11/osd.11: (2) No such file or directory``
        - ``ERROR: osd init failed: (22) Invalid argument``


Inkscope
--------

https://github.com/inkscope/inkscope

- 模块化管理
- 提供REST API
- 通过访问Inkscope REST API提供Ceph的web图形化界面 [#]_

.. image:: /images/ceph/ceph_inkscope.png

- inkscopeViz 
    - Web客户端 
- inkscopeCtrl
    - 是inkscope的服务器端
    - 提供了REST API
- inkscopeProbe
    - 收集ceph节点的系统信息
    - 收集到的数据将传输到MongoDB
- inkscopeMonitor (开发中)


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


总结
====
====

对比
----

============= ============= =========== ============= ============ 
Item          Calamari      ceph-dash   VSM           inkscope     
============= ============= =========== ============= ============ 
hotness       66,175,116    36,128,46   50,82,57      38,82,36     
license       LGPL2.1       MIT-        Apache v2     Apache v2    
language      python/JS     python/JS   python        python       
web_engine    Apache/django Apache      Apache/django Apache/flask 
js_lib        AngularJS     TBD         N/A           AngularJS
css           bootstrap     TBD         bootstrap     bootstrap
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
link to cinder N           Y          N
============== =========== ========== ========  


- 注意
    - 热度是按github上2016/3/9，watch+star+fork的数量进行排序的
    - krakendash使用的是修改过的MIT license
    - 部分数据来自互联网


Calamari与VSM
-------------

Calamari在程序的设计上较为合理，有相对更强的MicroServices属性，不仅提供了对ceph集群的监控，同时也提供了宿主机的监控；管理功能不足，主要实现一些属性方面的配置修改。
VSM实现的管理功能很多，但是局限于对VSM创建的Ceph集群进行管理。监控功能不足，主要实现了ceph客户端的一些监控指令的简单汇总。


- Calamari
    - 亮点
        - 支持响应式布局（material design）
        - diamond收集ceph节点的监控信息，用户可以通过添加collecter实现不同维度数据的收集
        - carbon-cache配合whisper存储，由supervisord确保这两个工具的正常运行，具有较好的容错性
        - graphite生成集群监控视图，支持区间显示
        - Ceph开源社区管理
    - 不足
        - 需要借助saltstack对集群进行管理，或许会与其他运维工具（ansible、puppet、chef）冲突
        - 管理功能偏弱 
            - web界面中主要能实现一些tagging操作
        - 控制添加新节点的命令集成在ceph-deploy中（仅此而已）

- VSM
    - 亮点
        - 支持将rbd pool与openstack/cinder关联
        - 支持EC/replicated pool的管理以及cache tier的管理
        - 支持ntp latency的监控
        - vsm控制节点实现所有安装包及依赖包的预下载，便于ceph节点的安装
    - 不足
        - 监控功能偏弱
            - 大部分监控功能通过ceph client实现数据的收集
            - 实时监控的功能局限于IOPS、ntp latency、bandwidth、CPU使用率
        - 功能缺失
            - 在图形化界面中无法添加新的主机（仅支持对现有的主机进行管理）
            - 仅支持存储空间按StorageGroup进行统计
            - 仅支持对vsm创建的集群进行管理，不支持添加新的节点
        - 维护缺失
            - 用户使用文档无法找到（404）
            - vsm-dependencies 2015年1月后就没有更新
        - 安装脚本漏洞百出，安装时间比较长。
            - 无法实现无密码访问，需要数十次的手动输入密码
            - 依赖包无法正确安装，需手动在github中进行下载







参考文献
========
========



.. [#] http://www.slideshare.net/alaindechorgnat/inkscope-ceph-day-paris-final?qid=24a1a418-b01c-4f91-b718-f26cffe920b7&v=&b=&from_search=1
.. [#] https://01.org/virtual-storage-manager/documentation/vsm-0.5.1-training-slides
.. [#] http://www.slideshare.net/DaystromTech/ceph-days-sf2015-paul-evans-static?qid=4398eec4-e73a-4483-8e47-61f9875872d3&v=&b=&from_search=2
.. [#] http://calamari.readthedocs.org/en/latest/operations/index.html
.. [#] http://ceph.com/category/calamari/
.. [#] http://ceph.com/planet/ceph-calamari-the-survival-guide/
.. [#] http://www.openstack.cn/?p=2708
.. [#] https://communities.intel.com/community/itpeernetwork/datastack/blog/2014/11/03/helping-open-source-storage-move-into-enterprise-data-centers
.. [#] https://segmentfault.com/a/1190000002533877
.. [#] https://segmentfault.com/a/1190000003860692
.. [#] https://segmentfault.com/a/1190000000744706
.. [#] http://www.tuicool.com/articles/j6FBvq
.. [#] http://emmanuel.iffly.free.fr/doku.php?id=linux:graphite_opensuse


