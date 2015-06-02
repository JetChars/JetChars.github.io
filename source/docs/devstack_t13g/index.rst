=========================
DevStack Trouble Shooting
=========================

| Recommend using the following command combo to debug devstack
|

.. code-block:: bash

    # /tmp/.pip/build can be replaced to your own pip build folder
    sudo chown stack.stack /opt/stack/ -R && ./unstack.sh && sudo rm -rf /tmp/.pip/build/* && ./stack.sh

| And using the following command to trace error.
|

.. code-block:: bash

    grep -B10 -i error /opt/stack/logs/stack.sh.log | less

| Once you have passed the '**git clone**' phase you can turn ``RECLONE=False`` to enhance debugging speed. we can check 'stack.sh' in which phase via viewing ``stack.sh.log.summary``
|

.. code-block:: bash

    cat /opt/stack/logs/stack.sh.log.summary


Pip
===

.. sidebar:: Note

    - pip 7.0.1 seems not work well with ubuntu 14.04 (trusty)
    - apt and yum's python-pip versions both not up-to-date, apt is 1.5.4, yum is 1.5.6
    - pip can be upgrade to designated version use opt ``-U pip==version``
    - if pip installed by apt, then remove pip have to use apt, too.


1. Install python module
    - ``sudo easy_install pip``
    - ``sudo apt-get install python-pip``
    - ``sudo yum install python-pip``

2. Upgrade or downgrade module
    - ``sudo pip install -U pip``
    - ``sudo pip install -U pip==6.0.8``
    - ``sudo easy_install -U pip``
   

3. Remove module
    - ``sudo easy_install remove pip``
    - ``sudo pip uninstall pip``
    - ``sudo apt-get remove python-pip``
    - ``sudo yum remove python-pip``

4. Check pip & module version

.. code-block:: shell
    :linenos:
    :emphasize-lines: 2,7
  
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

    $ sudo chmod a+w /tmp/.pip/build   # make build path writeable for all user

| If not make build path writeable, will cause issue like this
|

::

    ...Installing setuptools, pip, wheel...done.
    Traceback (most recent call last):
      File "/bin/virtualenv", line 11, in <module>
        sys.exit(main())
      File "/usr/lib/python2.7/site-packages/virtualenv.py", line 832, in main
        symlink=options.symlink)
      File "/usr/lib/python2.7/site-packages/virtualenv.py", line 1004, in create_environment
        install_wheel(to_install, py_executable, search_dirs)
      File "/usr/lib/python2.7/site-packages/virtualenv.py", line 969, in install_wheel
        'PIP_NO_INDEX': '1'
      File "/usr/lib/python2.7/site-packages/virtualenv.py", line 910, in call_subprocess
        % (cmd_desc, proc.returncode))
    OSError: Command /opt/stack/devstack/tmp-venv-a6Q3/bin/python -c "import sys, pip; sys...d\"] + sys.argv[1:]))" setuptools pip wheel failed with error code 2
    +++ err_trap
    +++ local r=1
    Error on exit


6. Wheel: Multiple .disk-info directiries

.. sidebar:: What's wheel ?

    Wheel is a built-package format, and offers the advantage of not recompiling your software during every install. [#]_

| **Solutions :** 
|
* Not use wheel::

    sudo pip uninstall pkgname
    sudo rm -rf pip_build_folder
    sudo pip instll pkgname --no-use-wheel

* Use temporary build dir::


    sudo pip install -U pkgname --build==$(mktemp -d)

* Comment one line in /usr/local/lib/python2.7/dist-packages/pip/wheel.py
  
.. code-block:: python
    :linenos:
    :emphasize-lines: 12

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

7. No distributions have been found for pip in /usr/local/lib/python2.7/dist-packages

| **Solution :** This issue cause by stack.sh override pip incorrectly, in order to avoid this issue, comment following 3 lines
|
::

    if [[ "$OFFLINE" != "True" ]]; then
        PYPI_ALTERNATIVE_URL=$PYPI_ALTERNATIVE_URL $TOP_DIR/tools/install_pip.sh
    fi

|
|


.. sidebar:: Note

    - Most **import error** caused by module not installed or not installed properly
    - **attribute cannot be found** probably caused by module's integrity issue or version not compatible.
    - Some weird issue caused by module virsion, which might cause compatible issues; known trouble modules: ``python-{cinder,swift,glance}client`` ``django-openstack-auth`` ``python-openstack``



Python
======

1. ImportError
    - No module named MySQLdb::

        $ sudo apt-get install python-mysqldb

    - No module named libvirt::

        $ sudo apt-get remove python-libvirt
        $ sudo apt-get install python-libvirt


|
|
|
|

2. Attribute cannot be found
    - 'module' object has no attribute 'IPOpt'
.. code-block:: guess
    :linenos:
    :emphasize-lines: 9

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

| **Solution :** Open file "/opt/stack/neutron/neutron/plugins/openvswitch/common/config.py", we can easily find that cfg is a component of oslo.config.
|
::

    from oslo.config import cfg

| Apparently, this issue was caused by oslo.config’s integrity.
|
::

    $ sudo apt-get remove python-oslo.config
    $ sudo apt-get install python-oslo.config

3. command virtualenv not found

::

    ++ [[ 0 != 0 ]]
    ++ pip_install virtualenv
    ++ sudo -H http_proxy=http://proxy-shz.intel.com:911 https_proxy=https://proxy-shz.intel.com:911 'no_proxy=localhost,*intel.com:911,192.168.0.0/16,10.0.0.0/8,127.0.0.0/8' PIP_FIND_LINKS=file:///opt/stack/.wheelhouse /bin/pip install virtualenv
    DEPRECATION: --download-cache has been deprecated and will be removed in the future. Pip now automatically uses and configures its cache.
    Requirement already satisfied (use --upgrade to upgrade): virtualenv in /usr/lib/python2.7/site-packages
    ++ local test_req=virtualenv/test-requirements.txt
    ++ [[ -e virtualenv/test-requirements.txt ]]
    +++ mktemp -d tmp-venv-XXXX
    ++ TMP_VENV_PATH=tmp-venv-3TgB
    ++ virtualenv tmp-venv-3TgB
    /opt/stack/devstack/tools/build_wheels.sh: line 58: virtualenv: command not found
    +++ err_trap
    +++ local r=127
    Error on exit

| **Solution :** change to an earlier version can solve this issue.
|

::

    sudo -E pip install -U virtualenv=12.1.1


Rabbit
======

1. Unable to connect to node rabbit@upstream: nodedown 
::

    $ sudo apt-get remove rabbit-server
    $ sudo apt-get install rabbit-server

2. Failed to set rabbitmq password 
::

    $ sudo service rabbit-server restart

3. Failed to start rabbitmq-server

| **Solution :** Check the log file at ``/var/log/rabbitmq/startup_log`` 
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

MySQL
=====

.. sidebar:: Note 

    - **mariadb** -- Community developed branch of mysql, multi-user, multi-threaded SQL database server ``sudo service mariadb restart``
    - **mysql_secure_installation** -- improve MySQL installation security

1. Configure MySQL

Configure file ``/etc/mysql/my.cnf``--> ``/etc/my.cnf`` ``~/.my.cnf``
- Configurations
    - ``bind-address`` -- default ``127.0.0.1`` , change to ``0.0.0.0`` will listen all IPs
    - ``port`` -- listen port
- Restart MySQL
    - ``sudo /etc/init.d/mysql restart``
    - ``sudo pkill -1 mysqld``
- Check mysql status & variables::

    mysql -uroot -ppassword -e 'show status;'
    mysql -uroot -ppassword -e 'show variables;'

| username & password no need seperate from argument u & p)
| if password not concatenated with -p , will be recognized as database nodename
|

- Change max connction number::

    mysql -uroot -ppassword -e 'set global max_connections=40000;'

| can solve issue 1040 (too many connections).
| if enable too much service in control node, should do it in post-config phase!
|

2. Reset MySQL password

- Change password via reconfig mysql-server
::

    sudo dpkg-reconfigure mysql-server-5.5

- Change password in safemode, 'password' should be changed into your own password.

.. code-block:: bash
    :linenos:

    sudo service mysql stop
    sudo mysqld_safe &
    mysql -uroot -e "UPDATE mysql.user SET Password=PASSWORD('password') WHERE User='root';"
    sudo pkill -9 mysqld_safe
    sudo service mysql start

- mysqladmin
::

    # nova should be replaced to root password
    mysqladmin -u root -pnova password 'supersecret'

3. Uninstall MySQL

.. code-block:: bash
    :linenos:

    sudo apt-get remove -y --purge mysql* mariadb*
    sudo apt-get autoremove               
    sudo apt-get autoclean
    sudo rm -rf /var/lib/mysql /etc/apparmor.d/abstraction/mysql /{etc,run}/mysql /usr/{share,include,lib}/mysql



4. MySQL server failed to start

.. code-block:: guess
    :linenos:
    :emphasize-lines: 8

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

Apache
======

.. sidebar:: Note

    - **a2enmod**/**a2dismod** -- enable or disable an apache2 module
    ``/etc/apache2/mods-available`` ``/etc/apache2/mods-enabled``

1. Uninstall apache2
::

    sudo apt-get purge -y apache* libapache*
    sudo rm -rf /etc/apache2 /usr/{lib,sbin}/apache2 /run/apache2
    sudo autoremove -y
    sudo autoclean -y

2. Could not determine the server's fully qualified domain name

::

    $ echo "ServerName localhost" | sudo tee /etc/apache2/conf-available/fqdn.conf
    $ sudo a2enconf fqdn

3. Openstack Service Unavailable (HTTP 503)

| **Solution :** Reinstall apache2 can solve this issue
|
|
|

4. Module version does not exist!
::

    $ sudo a2enmod version
    ERROR: Module version does not exist!

| This error can be ignored
|

Other issues
============


1. Screen cannot open
::

    $ screen -x stack
    Cannot open your terminal '/dev/pts/0' - please check

| **Solution** : Change screen owner to current user.
|
::

    $ sudo chown stack:stack /dev/pts/0

2. Tempest

| If **./stack.sh** stuck at this step.
|
::

    ++ local test_req=tox/test-requirements.txt
    ++ [[ -e tox/test-requirements.txt ]]
    ++ pushd /opt/stack/tempest
    ~/tempest ~/devstack
    ++ tox --notest -efull
    full create: /opt/stack/tempest/.tox/full
    full installdeps: setuptools, -r/opt/stack/tempest/requirements.txt

| **Solution :** Comment one line in devstack/lib/tempest
|

.. code-block:: bash
    :linenos:
    :emphasize-lines: 5

    function install_tempest {
        git_clone $TEMPEST_REPO $TEMPEST_DIR $TEMPEST_BRANCH
        pip_install tox
        pushd $TEMPEST_DIR
        # tox --notest -efull
        PROJECT_VENV["tempest"]=${TEMPEST_DIR}/.tox/full
        install_tempest_lib
        popd
    }

3. Dashboard issue

* Authorization error::

    Unauthorized at /admin/
    Unauthorized (HTTP 401) (Request-ID: req-a7ef8ee1-3ce6-4082-b91b-4876208164c6)

| **Solution :** This error occurs when restarting controller node. Clearing web browser’s cookie can solve this problem.
|
|
|
|


.. [#] https://pip.pypa.io/en/latest/reference/pip_wheel.html
.. [#] https://bugs.launchpad.net/ubuntu/+source/mysql-dfsg-5.1/+bug/375371
.. [#] https://bugs.launchpad.net/ubuntu/+source/mysql-dfsg-5.0/+bug/227615
