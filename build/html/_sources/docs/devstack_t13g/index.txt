=========================
DevStack Trouble Shooting
=========================


Pip Issues
==========

.. sidebar:: Note

    - pip 7.0.1 seems not work well with ubuntu 14.04 (trusty)
    - apt's python-pip version is 1.5.4
    - pip can be upgrade to designated version use opt ``-U pip==version``
    - if pip installed by apt, then remove have to use it, too.


1. Install pip

.. code-block:: shell

    sudo easy_install pip
    sudo apt-get install python-pip
    sudo yum install python-pip

2. Upgrade pip

.. code-block:: shell

    sudo pip install -U pip
    sudo pip install -U pip==6.0.8
    sudo easy_install -U pip
   

3. Remove pip

.. code-block:: shell

    sudo easy_install remove pip
    sudo pip uninstall pip
    sudo apt-get remove python-pip
    sudo yum remove python-pip

4. Check pip version

::
  
    pip -V

4. Config pip

.. sidebar:: Note

    - if not add **trusted-host** to conf file, some pkgs might not be able install
    - sometimes official mirror not available, try some other `mirrors <http://www.pypi-mirrors.org>`_

| global conf file ``/etc/pip.conf``
| user conf file ``~/.pip/pip.conf``
|

::

    [global]
    default-timeout = 60
    respect-virtualenv = true
    build = /tmp/.pip/build
    download-cache = /tmp/.pip/cache
    index_url = http://pypi.python.org/simple/
    trusted-host = pypi.python.org

    [install]
    use-mirrors = true
    mirrors = http://pypi.python.org


Python issues
=============

1. importError
    - No module named MySQLdb::

        $ sudo apt-get install python-mysqldb

    - No module named libvirt::

        $ sudo apt-get remove python-libvirt
        $ sudo apt-get install python-libvirt


Rabbit issues
=============

1. unable to connect to node rabbit@upstream: nodedown 
::

    $ sudo apt-get remove rabbit-server
    $ sudo apt-get install rabbit-server

2. Failed to set rabbitmq password 
::

    $ sudo service rabbit-server restart

3. Failed to start rabbitmq-server

| Check the log file at ``/var/log/rabbitmq/startup_log`` , If error type is “eaddrinuse”, which mean the listen port had been in use. We can change parameters in ``/etc/rabbitmq/rabbitmq-env.conf`` , following are it’s default values:
|
::

    NODENAME=rabbit
    NODE_PORT=5632

| then we can restart it.
|
::

    $sudo service rabbit-server restart



Other issues
============

1. screen cannot open
::

    Cannot open your terminal '/dev/pts/0' - please check

| **Solution**
|
::

    $ sudo chown stack:stack /dev/pts/0

2. mysql server failed to start
::

    Setting up mysql-server-5.5 (5.5.43-0ubuntu0.14.04.1) ...
    start: Job failed to start
    invoke-rc.d: initscript mysql, action "start" failed.
    dpkg: error processing package mysql-server-5.5 (--configure):
     subprocess installed post-installation script returned error exit status 1
    dpkg: dependency problems prevent configuration of mysql-server:
     mysql-server depends on mysql-server-5.5; however:
      Package mysql-server-5.5 is not configured yet.
    
    dpkg: error processing package mysql-server (--configure):
     dependency problems - leaving unconfigured
    Errors were encountered while processing:
     mysql-server-5.5
     mysql-server
    E: Sub-process /usr/bin/dpkg returned an error code (1)

| **Solution :** uninstall thoroughly.
|
|
