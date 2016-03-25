===========
Ceph Deploy
===========

This doc records ceph deployment based on **debian trusty(14.04)** and **ceph firefly(0.80.11)**


Prefight
========
========

- Ceph Cluster require at least 1 Admin, 1 MON and 2 OSDs.
- Ceph repo and key only need to be installed on Admin Node
- Admin node require password-less access to Ceph Nodes

ceph node
---------

Every node will config in a same way.
So basicly we can config a host manually, then clone it into some other nodes w/ hostname and IP changed.

Notice, we can't run this scrip directly
- some variables should be switched

.. code-block:: shell

    # install required pkgs
    # =====================
    sudo apt-get install ntp openssh-server -y

    # create a ceph deploy user with sudo privileges
    # ==============================================
    sudo useradd -d /home/{username} -m {username}
    sudo passwd {username} << EOF
    {passwd}
    {passwd}
    EOF
    echo "{username} ALL = (root) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/{username}
    sudo chmod 0440 /etc/sudoers.d/{username}

    # config ssh
    # ==========
    echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config
    echo "PermitRootLogin yes
    PasswordAuthentication yes
    ClientAliveInterval 30
    ClientAliveCountMax 99999
    " >> /etc/ssh/sshd_config
    echo "Host    {alias}
    HostName        {ipaddr}
    User            {username}
    IdentityFile    {keypath}
    Port            {port}
    " >> ~/.ssh/config
    
    # restart vm
    # ==========
    sudo reboot   



admin node
----------

Notice, we can't run this scrip directly
- some variables should be switched
- should change current user into ceph-admin user since this user was created
- we should add all nodes' hostname into **ssh_config**, *Port* and *IdentityFile* can be ommited.

.. code-block:: shell

    # add release key, apt repo and install ceph-deploy
    # =================================================
    wget -q -O- 'https://download.ceph.com/keys/release.asc' | sudo apt-key add -
    echo deb http://download.ceph.com/debian-{ceph-stable-release}/ $(lsb_release -sc) main | sudo tee /etc/apt/sources.list.d/ceph.list
    sudo apt-get update && sudo apt-get install ceph-deploy

    # install required pkgs
    # =====================
    sudo apt-get install ntp openssh-server -y

    # create a ceph deploy user with sudo privileges
    # ==============================================
    sudo useradd -d /home/{username} -m {username}
    sudo passwd {username} << EOF
    {passwd}
    {passwd}
    EOF
    echo "{username} ALL = (root) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/{username}
    sudo chmod 0440 /etc/sudoers.d/{username}

    # config ssh
    # ==========
    shh-keygen -P '' << EOF

    EOF
    echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config
    echo "PermitRootLogin yes
    PasswordAuthentication yes
    ClientAliveInterval 30
    ClientAliveCountMax 99999
    " >> /etc/ssh/sshd_config
    echo "Host    {alias}
    HostName        {ipaddr}
    User            {username}
    IdentityFile    {keypath}
    Port            {port}
    " >> ~/.ssh/config
    # ceph-deploy conn ceph nodes w/ hostname
    echo "{host list}" >> /etc/hosts
    # we should repeat this step, add copy to all ceph nodes
    ssh-copy-id {host}
    
    # restart vm
    # ==========
    sudo reboot

Storage Cluster Quick Start
===========================
===========================


create a cluster w/ 1 MON & 2 OSDs
----------------------------------

.. code-block:: guessdd

    -------------            -----------
   | admin-node  | ________ | ceph-mon  |
   | ceph-deploy |          | mon.node1 |
    -------------            -----------
         |                           
         |                           
         |                   -----------  
         |_________________ | ceph-osd0 |
         |                  | osd.0     |
         |                   -----------  
         |                              
         |                              
         |                   -----------  
         |_________________ | ceph-osd1 |
                            | osd.1     |
                             ----------- 

runnig this cmd in ceph-admin node w/ ceph-admin user and in config folder:

.. code-block:: shell

    # admin user need to create a folder storage config files
    # any deploy cmds will need running in this folder
    # =======================================================
    mkdir my-cluster
    cd my-clustr

    # add initial mon node,
    # then install ceph(full pkg) within all nodes
    # ========================================================
    ceph-deploy new ceph-mon
    # notice here are no underscores
    echo "osd pool default size = 2" >> ceph.conf
    ceph-deploy install ceph-admin ceph-mon ceph-osd1 ceph-osd2
    # create-initial create keyrings named start w/ clustername
    ceph-deploy {--overwrite-conf} mon create-initial

    # add OSDs
    # ========
    # create ceph folders first
    ssh ceph-osd0
    sudo mkdir /var/local/osd0
    exit
    ssh ceph-osd01
    sudo mkdir /var/local/osd1
    sudo chmod a+w /var/local/ -R   # can't write if not do this
    exit
    # prepare and activate OSDs
    ceph-deploy osd prepare ceph-osd0:/var/local/osd0 ceph-osd1:/var/local/osd1
    ceph-deploy osd activate ceph-osd0:/var/local/osd0 ceph-osd1:/var/local/osd1

    # copy admin key and conf-file to all ceph nodes
    # hence, all ceph nodes can exec ceph-cli w/o ip&keyring


Expanding Cluster
-----------------

.. code-block:: guessdd

    -------------            ---------------
   | admin-node  | ________ | ceph-mon      |
   | ceph-deploy |          | mon.ceph-mon  |
    -------------           | osd.2         |
         |                  | mds.ceph-mon  |
         |                   ---------------
         |                           
         |                           
         |                   ---------------
         |_________________ | ceph-osd0     |
         |                  | osd.0         |
         |                  | mon.ceph-osd0 |
         |                   ---------------
         |                              
         |                              
         |                   ---------------  
         |_________________ | ceph-osd1     |
                            | osd.1         |
                            | mon.ceph-osd1 |
                             ---------------

runnig this cmd in ceph-admin node w/ ceph-admin user and in config folder:


.. code-block:: shell

    # adding a OSD in ceph-mon
    # ========================
    ssh ceph-mon
    sudo mkdir /var/local/osd2
    exit
    ceph-deploy osd prepare ceph-mon:/var/local/osd2
    ceph-deploy osd activate ceph-mon:/var/local/osd2
    ceph -w   # watch changes when adding new osd

    # adding a MDS in ceph-mon
    # ========================
    ceph-deploy mds create ceph-mon
    
    # adding MONs
    # ===========
    ssh ceph-osd1
    sudo apt-get install ntp -y
    echo "server 192.168.56.101" >> /etc/ntp.conf
    exit
    ssh ceph-osd2
    sudo apt-get install ntp -y
    echo "server 192.168.56.101" >> /etc/ntp.conf
    exit
    ceph-deploy mon add ceph-osd1 ceph-osd2   # probably not working when adding 2 MONs


.. note:: when run ceph cluster w/ multi MONs, ntp should configured.


Once MONs were adding into current cluster,it will begin synchronizing MONs and form a quorum. [#]_


.. code-block:: console

    # ceph quorum_status --format json-pretty

    { "election_epoch": 12,
      "quorum": [
            0,
            1,
            2],
      "quorum_names": [
            "ceph-osd1",
            "ceph-osd2",
            "ceph-mon"],
      "quorum_leader_name": "ceph-osd1",
      "monmap": { "epoch": 3,
          "fsid": "5b598bb1-4fa5-44c8-bce0-d490cf8571a5",
          "modified": "2016-03-08 19:19:39.396616",
          "created": "0.000000",
          "mons": [
                { "rank": 0,
                  "name": "ceph-osd1",
                  "addr": "192.168.56.111:6789\/0"},
                { "rank": 1,
                  "name": "ceph-osd2",
                  "addr": "192.168.56.112:6789\/0"},
                { "rank": 2,
                  "name": "ceph-mon",
                  "addr": "192.168.56.113:6789\/0"}]}}


Remove Ceph
-----------

.. code-block:: shell

    ceph-deploy purgedata <ceph-nodes>
    ceph-deploy forgetkeys
    ceph-deploy purge <ceph-nodes>   # will purge ceph pkgs too



Ceph Usages
===========
===========


cmds to check cluster stats
---------------------------

.. code-block:: shell

    # check cluster version
    ceph -v
    # w/ param detail will see verbose verion of health stat
    ceph health {detail}
    # show cluster stat, will contain more info than *ceph health*
    ceph -s
    # watch live cluster changes, will contain info in *ceph -s*
    ceph -w
    ceph osd lspools
    ceph auth list
    ceph df
    ceph mon stat
    ceph mon dump
    ceph osd stat
    ceph osd dump
    ceph osd tree
    ceph pg dump
    rbd list

ceph client
-----------


rados client
------------


.. code-block:: console

    $ echo "hello ceph" >> testobj.txt
    $ rados -p data put testobj testobj.txt
    $ rados -p data ls   # get file list in pool 'data'
    testobj
    $ ceph osd map data testobj   # get testobj's location
    osdmap e20 pool 'data' (0) object 'testobj' -> 
    pg 0.780569b (0.1b) -> up ([1,2], p1) acting ([1,2], p1)
    $ # get obj locations within pool 'rbd'
    $ for i in $(rados -p rbd ls);do ceph osd map rbd $i;done
    $ # remove obj
    $ rados -p data rm testobj 


.. note:: notice that **rados** can exec w/ ``-p data`` or ``-p=data`` or ``--pool=data``


rbd client
----------

.. code-block:: shell

    # create a 4GB block device, and map to localhost
    # using -m0 make sure no space preserved for superuser
    # ====================================================
    rbd create foo --size 4096   # unit is MB
    sudo rbd map foo --pool rbd --name client.admin
    sudo mkfs.ext4 -m0 /dev/rbd/rbd/foo
    sudo mkdir /mnt/test
    sudo mount /dev/rbd/rbd/foo /mnt/test
    cd /mnt/test
    rbd list {-l/--long}  # check rbd list, 'long' for more info
    # unmount device and unmap the block device
    # =========================================
    umount /mnt/test
    rbd unmap /dev/rbd/rdb/foo


ceph_fs
-------

- ``ceph osd pool create <poolname> <int[0-]> {<int[0-]>} {replicated|erasure} {<erasure_code_profile>} {<ruleset>}``


.. code-block:: shell

    ceph osd pool create fs_data 100   # pg num required
    ceph osd pool create fs_metadata 100
    # ceph osd fs new myfs fs_metadata fs_data
    # exec this cmd is quickly, but takes long to active
    ceph mds newfs {metaid} {dataid} --yes-i-really-mean-it
    ceph mds newfs 4 3 --yes-i-really-mean-it

    # mount cephfs, need secret if cephx enabled
    # ==========================================
    sudo mkdir /mnt/mycephfs
    sudo mount -t ceph 192.168.56.113:6789:/ /mnt/mycephfs
    sudo mount -t ceph 192.168.56.113:6789:/ /mnt/mycephfs -o name=admin,secret=AQAsO9hWcAqwJRAAuahZhGDGjQryjaK4AXqUww==
    sudo mount -t ceph 192.168.56.113:6789:/ /mnt/mycephfs -o name=admin,secretfile=/etc/ceph/admin.secret
    sudo umount /mnt/mycephfs

    # mount cephfs in User Space (FUSE)
    sudo mkdir /mnt/mycephfs
    sudo ceph-fuse -m 192.168.56.113:6789 /mnt/mycephfs
    sudo ceph-fuse -m 192.168.56.113:6789 /mnt/mycephfs -k /etc/ceph/ceph.client.admin.keyring

.. note:: this IP is MON's, and admin.secret looks like this ``AQAsO9hWcAqwJRAAuahZhGDGjQryjaK4AXqUww==``



RGW
---

.. code-block:: shell

    ceph-deploy rgw create {gateway-node}


change RGW config file in RGW node

.. code-block:: ini

    [client]
    rgw frontends = civetweb port=80
    rgw frontends = civetweb port=[::]:80

- notice second option is for ipv6, only need one line of rgw frontends.



disable cephx [#]_
-------------


change ``ceph.conf`` [#]_

.. code-block:: ini

    [global]
    ...
    auth_cluster_required = none
    auth_service_required = none
    auth_client_required = none



Upgrading
---------

upgrade ceph from **firefly(0.80.11)** to **hammmer(0.94.6)**

- will processed in this order
    - Ceph deploy
    - Ceph MONs
    - Ceph OSDs
    - Ceph MDSs
    - RGW


.. code-block:: shell

    # upgrade ceph
    # ============
    echo deb http://download.ceph.com/debian-{ceph-stable-release}/ $(lsb_release -sc) main | sudo tee /etc/apt/sources.list.d/ceph.list
    sudo apt-get update && sudo apt-get install --upgrade ceph-deploy
    ceph-deploy install --release hammer ceph-mon ceph-osd1 ceph-osd2 ceph-mds ceph-rgw

    # restart all services
    # ====================
    sudo restart ceph-mon-all
    sudo restart ceph-osd-all
    sudo restart ceph-mds-all
    sudo restart ceph-rgw-all
    ceph -s   # check cluster stat 




References
==========
==========


.. [#] https://en.wikipedia.org/wiki/Quorum_(distributed_computing)
.. [#] http://dachary.org/loic/ceph-doc/rados/configuration/auth-config-ref/
.. [#] http://docs.openfans.org/ceph/ceph4e2d658765876863/ceph-1/ceph-storage-cluster3010ceph5b5850a896c67fa43011/operations301064cd4f5c3011/cephx-authentication3010cephx9a8c8bc13011
.. [#] http://docs.ceph.com/docs/master/start/quick-start-preflight/
.. [#] http://docs.ceph.com/docs/master/start/quick-ceph-deploy/
.. [#] http://www.centoscn.com/CentosServer/test/2015/0521/5489.html
.. [#] http://zhanguo1110.blog.51cto.com/5750817/1543032
.. [#] http://www.07net01.com/2015/12/1029404.html
.. [#] http://blog.csdn.net/zhoudaxia/article/details/8044129
