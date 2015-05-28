====================================
OpenStack installation with `DevStack <http://git.openstack.org/cgit/openstack-dev/devstack/>`_
====================================


Quick Start
===========

1. Create stack user

| stack.sh is DevStack's main function, it should run with stack user with sudo privileges. and have privileges to all nodes.
|

.. code-block:: bash
    :linenos:

    groupadd stack
    useradd -g stack -s /bin/bash -d /opt/stack -m stack
    echo "stack ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
    su - stack
    ssh-keygen -t rsa -P ''
    ssh-copy-id localhost

2. Download DevStack

.. code-block:: bash
    :linenos:

    git clone https://git.openstack.org/openstack-dev/devstack
    cd devstack

| Also have another repo at github:   ``https://github.com/openstack-dev/devstack``
|


3. Config DevStack

- ``local.conf`` is devstack's *user config file*, ``stack.sh`` will read this file before it's default config file ``stackrc``
- ``stackrc`` : git repositories for all of the OpenStack services are defined in here. we can modify param ``GIT_BASE`` to change scheme or repo, eg: ``git://git.openstack.org`` to ``https://github.com``



4. Expected Result::

    Horizon is now available at http://192.168.48.134/ 
    Keystone is serving at http://192.168.48.134:5000/v2.0/
    Examples on using novaclient command line is in exercise.sh
    The default users are: admin and demo
    The password: openstack
    This is your host ip: 192.168.48.134


Config file
===========

| The new config file ``local.conf`` is an extended-INI format that introduces a new meta-section header that provides some additional information such as a phase name and destination config filename
|
::

    [[ <phase> | <config-file-name> ]]



Switches
--------

::

RECLONE=False
OFFLINE=False


Multi Host
----------

| Default: ``MULTI_HOST=False``
| Running DevStack with multiple hosts requires a custom local.conf section for each host. The master is the same as a single host installation with MULTI_HOST=True. The slaves have fewer services enabled and a couple of host variables pointing to the master. [#]_
|

- Master::

    MULTI_HOST=True

- Slave::

    MYSQL_HOST=w.x.y.z
    RABBIT_HOST=w.x.y.z
    GLANCE_HOSTPORT=w.x.y.z:9292
    ENABLED_SERVICES=n-vol,n-cpu,n-net,n-api



Log
---

::

    LOGDIR=$DEST/logs
    LOGFILE=$DEST/logs/stack.sh.log
    LOGDAYS=7
    LOGCOLOR=False
    SYSLOG=True
    SYSLOG_HOST=$SERVICE_HOST
    SCREEN_LOGDIR=$DEST/logs/screen



Cinder
------

Default Values::

    CINDER_DRIVER=default
    VOLUME_GROUP="stack-volumes"
    VOLUME_NAME_PREFIX="volume-"
    VOLUME_BACKING_FILE_SIZE=10250M

**CINDER_DRIVER :** default driver means lvm, other options are ``glusterfs`` ``nfs`` ``sheepdog`` ``vsphere`` ``XenAPINFS``, contains ``function configure_cinder_driver``

Swift
-----

::

    enable service s-proxy s-object s-container s-account
    SWIFT_HASH=66a3d6b56c1f479c8b4e70ab5c2000f5
    SWIFT_REPLICAS=1
    SWIFT_DATA_DIR=$DEST/data/swift
    SWIFT_LOOPBACK_DISK_SIZE=6G

Sahara
------

::

    ENABLED_SERVICES+=,sahara
    EXTRA_OPTS=(auto_assign_floating_ip=True)

Post Script file
================

.. [#] https://github.com/openstack-dev/devstack/blob/edfcb5f0bd9faa3c55ad1691465a45b7ef221789/doc/source/configuration.rst
