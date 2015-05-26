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

5. Config pip

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

6. wheel Multiple .disk-info directiries

| **Solutions** 
|
* not use wheel::

    sudo pip uninstall pkgname
    sudo rm -rf pip_build_folder
    sudo pip instll pkgname --no-use-wheel

* use tmp build dir::

    sudo pip install -U pkgname --build==$(mktemp -d)

* comment one line in /usr/local/lib/python2.7/dist-packages/pip/wheel.py::

    for s in subdirs:
        destsubdir = os.path.join(dest, basedir, s)
        if is_base and basedir == '' and destsubdir.endswith('.data'):
            data_dirs.append(s)
            continue
        elif (is_base and
                s.endswith('.dist-info') and
                # is self.req.project_name case preserving?
                s.lower().startswith(
                    req.project_name.replace('-', '_').lower())):
            # comment this line
            # assert not info_dir, 'Multiple .dist-info directories'
            info_dir.append(destsubdir)


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

| Check the log file at ``/var/log/rabbitmq/startup_log`` 
| If error type is “eaddrinuse”, which mean the listen port had been in use.
| We can change parameters in ``/etc/rabbitmq/rabbitmq-env.conf`` 
| Following are it’s default values:
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

| **Solution :** change tmp dir [#]_ [#]_
|

| Edit /etc/mysql/my.cnf
| Change: ``tmpdir = /tmp`` To: ``tmpdir = /var/tmp/mysql``
|
| And make sure you create that directory and set the permissions appropriately:
|
::

    sudo mkdir -m 0770 /var/tmp/mysql
    sudo chown mysql:mysql /var/tmp/mysql

| Then you can try a reinstall and it should work :
|
::

    sudo apt-get install -f


.. [#] https://bugs.launchpad.net/ubuntu/+source/mysql-dfsg-5.1/+bug/375371
.. [#] https://bugs.launchpad.net/ubuntu/+source/mysql-dfsg-5.0/+bug/227615
