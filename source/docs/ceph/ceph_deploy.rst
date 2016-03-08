===========
Ceph Deploy
===========

This doc records ceph deployment based on debian 14.04 trusty


Prefight
========
========


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
    " >> /etc/ssh/ssh_config
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
    " >> /etc/ssh/ssh_config
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

runnig this cmd in ceph-admin node w/ cephadmin user:

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
    # will create keyrings named start w/ clustername
    ceph-deploy mon create-initial

    # add OSDs
    # ========
    # create ceph folders first
    ssh ceph-osd0
    sudo mkdir /var/local/osd0
    exit
    ssh ceph-osd01
    sudo mkdir /var/local/osd1
    exit
    # prepare and activate OSDs
    ceph-deploy osd prepare ceph-osd0:/var/local/osd0 ceph-osd1:/var/local/osd1
    ceph-deploy osd activate ceph-osd0:/var/local/osd0 ceph-osd1:/var/local/osd1

    # copy admin key and conf-file to all ceph nodes
    # hence, all ceph nodes can exec ceph-cli w/o ip&keyring


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
    rbd list

ceph client
-----------


rbd client
----------


References
==========
==========


.. [#] http://docs.ceph.com/docs/master/start/quick-start-preflight/
.. [#] http://docs.ceph.com/docs/master/start/quick-ceph-deploy/
.. [#] http://www.centoscn.com/CentosServer/test/2015/0521/5489.html
.. [#] http://zhanguo1110.blog.51cto.com/5750817/1543032
.. [#] http://www.07net01.com/2015/12/1029404.html
