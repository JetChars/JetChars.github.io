=======
pelican
=======

`online doc <http://docs.getpelican.com>`_

Get start
=========
=========

.. code-block:: shell

    pip install pelican markdown
    mkdir -p ~/pelican_projs/testing   # create an folder for pelican project
    cd pelican_projs/testing           
    pelican-quickstart                 # start the interactive initialization
    vim content/test.md                # creating an article under folder *content*
    pelican content                    # generate static website
    open output/index.rst              # reviewing website

Update pelican w/ `rsync <https://rsync.samba.org/>`_
=======================
=======================

.. code-block:: shell

    # config rsync server
    # ===================
    yum install rsync
    touch /etc/rsyncd.{conf,secrets,motd}   # create config files
    chmod 600 /etc/rsyncd.secrets
    /usr/bin/rsync --daemon  --config=/etc/rsyncd.conf
    iptables -A INPUT -p tcp -m state --state NEW  -m tcp --dport 873 -j ACCEPT
    iptables -L

    # update files to server
    # ======================
    rsync --delete -avzP content/* root@192.168.0.106:content


rsync config file
-----------------

.. code-block:: shell

    # This line is required by the /etc/init.d/rsyncd script
    pid file = /var/run/rsyncd.pid
    port = 873
    uid = root
    gid = root
    use chroot = yes
    #limit access to private LANs
    hosts allow=192.168.0.0/255.255.255.0
    hosts deny=*
    max connections = 5
    motd file = /etc/rsyncd.motd
    log file = /var/log/rsync.log
    log format = %t %a %m %f %b
    timeout = 300

    [pelican_content]
    path = /root/test
    list=yes
    ignore errors = yes
    auth users = root
    secrets file = /etc/rsyncd.secrets
    comment = This is pelican content
    post-xfer exec = /usr/bin/pelican /homt/jet/pelican_projs/test/content


rcync cmd format
----------------

.. code-block:: shell

    rsync [OPTION]... SRC [SRC]... [USER@]HOST:DEST 
    rsync [OPTION]... [USER@]HOST:SRC DEST 
    rsync [OPTION]... SRC [SRC]... DEST 
    rsync [OPTION]... [USER@]HOST::SRC [DEST] 
    rsync [OPTION]... SRC [SRC]... [USER@]HOST::DEST 
    rsync [OPTION]... rsync://[USER@]HOST[:PORT]/SRC [DEST]
