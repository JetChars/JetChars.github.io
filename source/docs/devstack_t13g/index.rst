=========================
DevStack Trouble Shooting
=========================


Pip
===

.. sidebar:: Note

    - pip 7.0.1 seems not work well with ubuntu 14.04 (trusty)
    - apt's python-pip version is 1.5.4
    - pip can be upgrade to designated version use opt ``-U pip==version``
    - if pip installed by apt, then remove pip have to use apt, too.


1. Install pip
    - ``sudo easy_install pip``
    - ``sudo apt-get install python-pip``
    - ``sudo yum install python-pip``

2. Upgrade pip
    - ``sudo pip install -U pip``
    - ``sudo pip install -U pip==6.0.8``
    - ``sudo easy_install -U pip``
   

3. Remove pip
    - ``sudo easy_install remove pip``
    - ``sudo pip uninstall pip``
    - ``sudo apt-get remove python-pip``
    - ``sudo yum remove python-pip``

4. Check pip & module version

::
  
    $ pip -V
    pip 6.1.1 from /Library/Python/2.7/site-packages/pip-6.1.1-py2.7.egg (python 2.7)

    $ pip show six #pkgname
    Metadata-Version: 1.1
    Name: six
    Version: 1.4.1
    Summary: Python 2 and 3 compatibility utilities
    Home-page: http://pypi.python.org/pypi/six/
    Author: Benjamin Peterson
    Author-email: benjamin@python.org
    License: UNKNOWN
    Location: /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python


5. Config pip

.. sidebar:: Note

    - if not add **trusted-host** to conf file, some pkgs might not be able install
    - sometimes official mirror not available, try some other `mirrors <http://www.pypi-mirrors.org>`_
    - build folder should be writeable for all users.

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

::

    $ sudo chmod +x /tmp/.pip/build

6. wheel Multiple .disk-info directiries

.. sidebar:: What's wheel

    Wheel is a built-package format, and offers the advantage of not recompiling your software during every install. [#]_

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


Python
======

.. sidebar:: Note

    - most **import error** caused by module not installed or not installed properly
    - **attribute cannot be found** probably caused by module's integrity issue or version not compatible.
    - some weird issue caused by module virsion, eg: ``python-cinderclient==1.2.1`` , ``django-openstack-auth=1.20.0`` , ``python-openstack==1.0.4`` might cause compatible issues

1. importError
    - No module named MySQLdb::

        $ sudo apt-get install python-mysqldb

    - No module named libvirt::

        $ sudo apt-get remove python-libvirt
        $ sudo apt-get install python-libvirt

2. attribute cannot be found
    - 'module' object has no attribute 'IPOpt'
::

        Traceback (most recent call last):
          File "/usr/local/bin/neutron-openvswitch-agent", line 6, in <module>
            from neutron.plugins.openvswitch.agent.ovs_neutron_agent import main
          File "/opt/stack/neutron/neutron/plugins/openvswitch/agent/ovs_neutron_agent.py", line 53, in <module>
            cfg.CONF.import_group('AGENT', 'neutron.plugins.openvswitch.common.config')
          File "/usr/lib/python2.7/dist-packages/oslo/config/cfg.py", line 1810, in import_group
            __import__(module_str)
          File "/opt/stack/neutron/neutron/plugins/openvswitch/common/config.py", line 38, in <module>
            cfg.IPOpt('local_ip', version=4,
        AttributeError: 'module' object has no attribute 'IPOpt'

| Open file "/opt/stack/neutron/neutron/plugins/openvswitch/common/config.py", we can easily find that cfg is a component of oslo.config.
|
::

    from oslo.config import cfg

| Apparently, this issue caused by oslo.config’s integrity.
|
::

    $ sudo apt-get remove python-oslo.config
    $ sudo apt-get install python-oslo.config

Rabbit
======

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

| **Solution : change tmp dir** [#]_ [#]_
|

-  Edit **/etc/mysql/my.cnf**, Change: ``tmpdir = /tmp`` To: ``tmpdir = /var/tmp/mysql``
-  And make sure you create that directory and set the permissions appropriately::

    sudo mkdir -m 0770 /var/tmp/mysql
    sudo chown mysql:mysql /var/tmp/mysql

- Then you can try a reinstall and it should work ::

    sudo apt-get install -f

.. [#] https://pip.pypa.io/en/latest/reference/pip_wheel.html
.. [#] https://bugs.launchpad.net/ubuntu/+source/mysql-dfsg-5.1/+bug/375371
.. [#] https://bugs.launchpad.net/ubuntu/+source/mysql-dfsg-5.0/+bug/227615
