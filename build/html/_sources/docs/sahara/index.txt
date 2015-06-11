=======================================================
`Sahara <http://docs.openstack.org/developer/sahara/>`_
=======================================================


About
=====

`Red Hat's doc of Deploying sahara <http://www.redhat.com/en/resources/deploying-sahara-analytics-service-red-hat-enterprise-linux-openstack-platform-5>`_


.. image:: images/sahara_fake_nodetemplate.png

.. sidebar:: Terms

    - **PTL** -- surgey lukjanov
    - **HaaS** -- Hadoop as a Service
    - **autoscaling** -- scaling depends on system loads
    - **anti affinity** -- avoid put datanode on same host 
    
.. note:: cinder volume not created locally according to instances' loaction

Sahara Cluster Status
---------------------

=========== ===========================
phase       description
=========== ===========================
Validating  check all necessary fields not violate, topology validation, or other validation before provisioning a cluster
Spawning    create VMs Volumes Floating IPs(need check default quota, hypervisor resources)
Waiting     waits while VM's operating system boot up & internal infrastructure like net and volumes are attached
Preparing   generating /etc/hosts, authorized_keys for VMs communication 
Starting    starting hadoop services on VMs
Active      cluster has started successfully
Error       cluster creation fails
=========== ===========================


plugins
=======

`vanilla <http://docs.openstack.org/developer/sahara/userdoc/vanilla_plugin.html>`_
-----------------------------------------------------------------------------------

The vanilla plugin is a reference implementation which allows users to operate a cluster with Apache Hadoop.

.. sidebar:: default usernames

    ============= ===========
    OS            username
    ============= ===========
    Ubuntu 14.04  ubuntu
    Fedora 20     fedora
    CentOS 6.5    cloud-user
    ============= ===========

Sahara Optimizaion Angles
=========================

* Cluster Type
    * Long term cluster
    * Transient cluster (Workload specific)
    * which docker or kvm for long tern clusetr?

* Cluster Size
    * big mem
    * more cores
    * faster disk
    * better network

* Data Locations
    * Streaming
    * copying

* Service Position
    * whether split master or slave services

* Disk type
    * ephemeral disk for sys
    * cinder for both sys and storage

* Tenent control & QoS

* Valuation other than performance, like boot speed, idle percent(vm system cost).

* whether use container like magnum


sahara image
============

`sahara-image-elements <https://github.com/openstack/sahara-image-elements>`_
`diskimage-builder <https://github.com/openstack/diskimage-builder>`_
