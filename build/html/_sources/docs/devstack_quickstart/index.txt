.. image:: images/devstack.png
    :align: right

===============================================================================================
OpenStack installation with `DevStack <http://git.openstack.org/cgit/openstack-dev/devstack/>`_
===============================================================================================


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

5. Get admin creds
   
.. code-block:: bash
    :linenos:

    . openrc admin admin
    . openrc demo demo


Config file
===========

| The new config file ``local.conf`` is an extended-INI format that introduces a new meta-section header that provides some additional information such as a **phase name** and **destination config filename**
|

::

    [[ <phase> | <config-file-name> ]]

============= ================
phase         description  
============= ================
local         If localrc exists it will be used instead to preserve backward-compatibility
pre-install   runs after the system packages are installed but before any of the source repositories are installed
install       runs immediately after the repo installations are complete
post-config   runs after the layer 2 services are configured and before they are started
extra         runs after services are started and before any files in extra.d are executed
post-extra    runs after files in extra.d are executed
============= ================





Service List
------------
  
according to stackrc, if 'ENABLED_SERVICES' it is null, will install all default service.

=========== ====================
service     components
=========== ====================
default     g-api/g-reg/key/n-api/n-crt/n-obj/n-cpu/n-net/n-cond/n-sch/n-novnc/n-xvnc/n-cauth
nova        n-api/n-crt/n-obj/n-cpu/n-net/n-cond/n-sch/n-novnc/n-xvnc/n-cauth
cinder      c-sci/c-api/c-vol
heat        h-eng/h-api/h-api-cfn/h-api-cw
horizon     horizon
sahara      sahara
ceilometer  ceilometer-acompute, ceilometer-acentral, ceilometer-anotification, ceilometer-collector, ceilometer-alarm-evaluator, ceilometer-alarm-notifier, ceilometer-api
others      rabbit, tempest, mysql
=========== ====================


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

Neutron
-------

| Each node need ``q-agt``, Restart q-agt can help reset network settings (ovs).
|

Network Node
^^^^^^^^^^^^

Compute Nodes
^^^^^^^^^^^^^


Cinder
------

Dependency
^^^^^^^^^^

- **lib/cinder** -- configure cinder service
- **lib/lvm** -- default driver
- **lib/cinder_plugins/{glusterfs,nfs,sheepdog,vsphere,XENAPINFS}**
- **lib/cinder_backends/{ceph,glusterfs,lvm,netapp_iscsi,netapp_nfs,nfs,solidfire,vmdk,xiv}**

Default Values
^^^^^^^^^^^^^^
::

    CINDER_DRIVER=default
    VOLUME_GROUP="stack-volumes"
    VOLUME_NAME_PREFIX="volume-"
    VOLUME_BACKING_FILE_SIZE=10250M
    CINDER_ENABLED_BACKENDS=-lvm:lvmdriver-1,lvm:lvmdriver-2   # enable multi_lvm_backend

**CINDER_DRIVER :** default driver means lvm, other options are ``glusterfs`` ``nfs`` ``sheepdog`` ``vsphere`` ``XenAPINFS``, contains ``function configure_cinder_driver``

Nova
----

Configure file
^^^^^^^^^^^^^^

- **/etc/nova/nova.conf**
    - ``default_ephemeral_format`` -- ``ext3``, ``ext4`` or ``xfs``

**Control node**


**Compute node**::

    NOVA_VNC_ENABLED=True
    NOVNCPROXY_URL="http://${SERVICE_HOST}:6080/vnc_auto.html"
    VNCSERVER_LISTEN=$HOST_IP
    VNCSERVER_PROXYCLIENT_ADDRESS=$VNCSERVER_LISTEN

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
