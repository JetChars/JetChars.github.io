.. image:: images/docker.png
    :align: right
    :width: 250px

======
Docker
======

Why docker
==========

.. sidebar:: about

    - Since March 2014(2013?) , Managed by DGAB (Docker Governance Advisory Board)
    - It's an open source container application engine. Portable and easy to deployment.
    - Use go language
    - Use native cpu/syscall/kernel (namespace/capabilities/ctrlgroup/apparmor/netfilter)
        - Use ipc namespace communicate between containers
        - Require libcontainer/lxc/libvirt/systemd-nspawn
    - Containers don't aim to be a replacement for VMs, they are complementary in the sense that they are better for specific use cases.



* Advangtages
    - compare to kvm use virtio, docker use AUFS, which is better.
    - light weight 'vm', use less mem than kvm, closer to BM
    - will not be install into host OS
    - each container owns a set of env
* Constrains
    - 64bit platform
    * must have same OS kernel
    * kernel 3.8 is minimal, except rhel **2.6.32** . So, 3.10(ubuntu 1404 trusty) or higher is recommended
    * can't over commitment
    * v1.10 can't modify files under /etc, v1.20 solved this issue (mount | grep etc)
    * network buttleneck
    * no time namespace

Underlying Technologies
-----------------------

Namespaces

============ ========== ======================
namespace    kernel     isolation
============ ========== ======================
mount        2.4.19     mount point / fs
uts          2.6.19     host name & NIS domain name
ipc          2.6.19     ipc resources
pid          2.6.24     process id space
network      2.6.29     network resources
user         3.8        user & group id
============ ========== ======================




    
Getting started
---------------

.. sidebar:: Note

    - docker not work well w/ proxy, so here is a workaround: ``service docker stop; docker -d &``
    - docker container not work well w/ proxy, add **key-values** of proxy server before cmds which need proxy
    - wrapped up in a function so that we have some protection against only getting half the file during "curl | sh"


Configuration files
^^^^^^^^^^^^^^^^^^^

- ``/etc/default/docker`` -- Docker Upstart and SysVinit configuration file(ubuntu)
    - location of docker binary, daemon startup opts, proxy, tmpdir
    - can work with export or any other cmds
- ``/etc/sysconfig/docker`` -- Docker configuration file for centos/fedora/redhat
    - parameters(key-value pair) only 
- docker will copy host's ``resolv.conf``



Install Docker
^^^^^^^^^^^^^^

.. code-block:: bash
        
    # require root user
    wget -qO- https://get.docker.com/ | sh
    curl -sSL https://get.docker.com/ | sh
    wget -qO- https://test.docker.com/ | sh   # test verison


Update Dockera
^^^^^^^^^^^^^^

.. code-block:: bash

    sudo wget https://get.docker.com/builds/Linux/x86_64/docker-latest -O /usr/bin/docker
    sudo chmod a+x /usr/bin/docker


Docker users
^^^^^^^^^^^^

If you would like to use Docker as a non-root user, you should now consider
adding your user to the "docker" group with something like::

    sudo usermod -aG docker your-user


Core techs
==========


storage
-------

If you're using Docker on CentOS, RHEL, Fedora, or any other distro that doesn't ship by default with **AUFS** support, you are probably using the **Device Mapper storage plugin**. By default, this plugin will store all your containers in a 100 GB sparse file, and each container will be limited to 10 GB.

- `AUFS <http://aufs.sourceforge.net/>`_

| In the early days, aufs was entirely re-designed and re-implemented Unionfs Version 1.x series. Adding many original ideas, approaches, improvements and implementations, it becomes totally different from Unionfs while keeping the basic features. [#]_






Basic Commands
==============

Infos
-----

.. code-block:: bash

    # Shows containers/images/storage infos
    # /execution driver/kernel/os/cpus/mem
    # /hostname/id/proxies
    docker info
    docker version



Container Management
--------------------


.. sidebar:: Note

    - docker daemon receives the commands
    - detach a instance ``^p^q``
    - 64-character long id, twice the length of uuid(32char)
    - docker can auto complete id, only need to provide an unique prefix

.. code-block:: shell
    :linenos:

    docker run [-v [hostpath:]path[:mountopts]] [-itd] [--rm] [--name cname] [--volumes-from <container>] <image> CMD
    docker ps [-aq] [--no-trunc]   # only have running/exited 2 stats
    docker kill <container>
    docker stop<container>
    docker inspect [-f, --format <format>] <container>
    docker rm <container>
    docker exec <container> CMD
    docker attach <container>
    docker stats <container>
    docker top <container>


Image Management
----------------

.. sidebar:: About tags

    same image can have multiple tags, eg:
    ubuntu, ubuntu:trusty, ubuntu:latest, ubuntu:14.04

.. code-block:: shell
    :linenos:

    docker images [-aq] <image>
    docker search <image>
    docker rmi <image>
    docker history [-q] [--no-trunc] <image>
    docker build [-f build-file] [-t tag] .
    docker save ubuntu > ubuntu.tar.gz
    docker load < ubuntu.tar.gz


tricks
------

.. code-block:: shell
    :linenos:

    # get backgound container id
    cid=$(docker run -itd)
    nid=$(docker inspect -f '{{.NetworkSettings.IPAddress}}' $cid)
    docker exec $cid <CMD>
    # clean docker containers
    docker kill $(docker ps -q) && docker rm $(docker ps -qa)
    # exec cmd one time through container
    docker run --rm --volumes-from john1 -v $(pwd):/backup busybox tar cvf /backup/john2.tar /john1
    # remove failure images
    docker rmi -f `docker images |  grep none | awk '{print $3}'`




Dockerfile
==========

Instructions
------------


================= =========================================
instructions      description
================= =========================================
FROM              sets the Base Image for subsequent instructions
MAINTAINER        set the Author field of the generated images
LABEL             adds metadata to an image, use ``docker inspect`` view an image's labels
ENV               sets the environment in container, same as ``docker run --env <key>=<value>``
ADD               copies new files, directories or remote file URLs to container
COPY              copies new files or directories to container
RUN               execute any commands in a new layer on top of the current image and commit the results
CMD               provide defaults for an executing container, There can only be one CMD instruction in a Dockerfile
================= =========================================






- ``RUN`` -- commad to change the base image, can exec multiple cmds via \\ and && ::

    RUN \
      apt-get update && \
      apt-get -y install apache2


- ``CMD`` -- default commands when container launched
- ``ADD`` -- move copy file from current dir to container ::

    ADD index.html /var/www/html/index.html

- ``EXPOSE`` -- container's port to be exposed ::

    EXPOSE 80

- ``VOLUME`` ["/data"]-- create a mount point ::

    VOLUME ["/var/www/html"]

- ``ENV REFRESHED_AT``
- ``ENTRYPOINT``
    

- ``ENV`` 
    - ``ENV <key> <value>``
    - ``ENV <key>=<value> ...``
  
.. code-block:: guess


    ENV http_proxy="http://10.239.4.80:913"
    ENV https_proxy="https://10.239.4.80:913"
    ENV ftp_proxy="ftp://10.239.4.80:913"
    ENV socks_proxy="socks://10.239.4.80:913"
    ENV no_proxy="localhost,*intel.com:913,172.16.0.0/16,10.0.0.0/8,127.0.0.0/8"
    ENV HTTP_PROXY="http://10.239.4.80:913"
    ENV HTTPS_PROXY="https://10.239.4.80:913"
    ENV FTP_PROXY="ftp://10.239.4.80:913"
    ENV SOCKS_PROXY="socks://10.239.4.80:913"
    ENV NO_PROXY="localhost,*intel.com:913,172.16.0.0/16,10.0.0.0/8,127.0.0.0/8"


configurationfs like below will not take effect!

.. code-block:: guess

    RUN export http_proxy="http://10.239.4.80:913"
    RUN export https_proxy="https://10.239.4.80:913"
    RUN export ftp_proxy="ftp://10.239.4.80:913"
    RUN export socks_proxy="socks://10.239.4.80:913"
    RUN export no_proxy="localhost,*intel.com:913,172.16.0.0/16,10.0.0.0/8,127.0.0.0/8"
    RUN export HTTP_PROXY="http://10.239.4.80:913"
    RUN export HTTPS_PROXY="https://10.239.4.80:913"
    RUN export FTP_PROXY="ftp://10.239.4.80:913"
    RUN export SOCKS_PROXY="socks://10.239.4.80:913"
    RUN export NO_PROXY="localhost,*intel.com:913,172.16.0.0/16,10.0.0.0/8,127.0.0.0/8"







Caching
-------

by default build use cache

.. code-block:: shell
    :linenos:

    docker build -f <dockerfile> -t <tag> .
    docker build --no-cache=true -f <dockerfile> -t <tag> .


Network Management
==================

.. image:: images/docker_swarm.png
    :align: right
    :width: 200px

`libswarm <https://github.com/docker/swarm>`_
-------------------------------------------

It's a small toolkit, for docker network settings. Defines a standard service interface, for communications between service module in distributed operation system.


`pipwork <https://github.com/jpetazzo/pipework>`_
-------------------------------------------------

Software-Defined Networking for Linux Containers



container in kvm
================

like coreos, intel clear linux or any other light weight linux work with container in hybrid mode.
- can take both the advangtages of kvm and container


3 tier of competition
---------------------

================================= ========================
tiers                             items
================================= ========================
application container provider    lxc,docker,rocket(rkt)
container management              ECS,k8s,swarm,mesos,magnum/k8s|swarm|mesos
computing engines                 EC2,GCE,Nova/Heat,mesos,magnum,vagrant/virtualbox/vmware
kvm images                        fedora-atomic,coreos,clearos
================================= ========================


.. image:: images/coreos.png
    :align: right

`CoreOS <https://coreos.com>`_
-----------------------------

- Open Source project for linux containers
- Linux for massive server deployment
- Started a project **rocket** , claimed simpler, lighter and much secure than docker

.. image:: images/coreos_docker.png
.. image:: images/coreos_etcd.png


`Kubernetes <http://kubernetes.io>`_
------------------------------------


https://github.com/GoogleCloudPlatform/kubernetes

It's an open source orchestration system for Docker containers, open-sourced by google

- kubelet manage all containers(aprserver, schedule, proxy)
- kubernetes pilot run at GAE


.. image:: images/k8s-singlenode-docker.png



Issues
======


1. FATA[0000] -- permission denied

.. code-block:: console

    FATA[0000] Get http:///var/run/docker.sock/v1.18/containers/json: dial unix /var/run/docker.sock: permission denied. Are you trying to connect to a TLS-enabled daemon without TLS? 

| **solution**

.. code-block:: bash

    sudo groupadd docker
    sudo usermod -aG docker stack   # stack is our current user
    then relog in to current user


2. FATA[0020] -- Error response from daemon

.. code-block:: console

    stack@r16s01:~/stacker$ docker run --net=host -d gcr.io/google_containers/etcd:2.0.9 /usr/local/bin/etcd --addr=127.0.0.1:4001 --bind-addr=0.0.0.0:4001 --data-dir=/var/etcd/data
    Unable to find image 'gcr.io/google_containers/etcd:2.0.9' locally
    FATA[0020] Error response from daemon: v1 ping attempt failed with error: Get https://gcr.io/v1/_ping: read tcp 10.239.4.160:913: i/o timeout. If this private registry supports only HTTP or HTTPS with an unknown CA certificate, please add `--insecure-registry gcr.io` to the daemon's arguments. In the case of HTTPS, if you have access to the registry's CA certificate, no need for the flag; simply place the CA certificate at /etc/docker/certs.d/gcr.io/ca.crt 


- solution: add ``OPTIONS=--insecure-registry gcr.io`` to /etc/sysconfig/docker


3. FATA[0040] -- Error response from daemon


.. code-block:: console

    FATA[0040] Error response from daemon: v1 ping attempt failed with error: Get http://gcr.io/v1/_ping: read tcp 10.239.4.80:913: i/o timeout

- solution: this personal repository is unreachable.
    - gcr.io means google container repository


4. centos image not provide binary ``service``, and ``systemctl`` failed to work.

.. code-block:: console

    RUN systemctl start sshd
    Failed to get D-Bus connection: No connection to service manager

- solution: ``/usr/sbin/sshd``


5. service docker failed to start

.. code-block:: console

[root@r3s1 ~]# service docker status
docker.service - Docker Application Container Engine
   Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled)
   Active: failed (Result: start-limit) since Mon 2015-08-03 22:53:15 CST; 56s ago
     Docs: https://docs.docker.com
  Process: 53392 ExecStart=/usr/bin/docker -d -H fd:// (code=exited, status=127)
 Main PID: 53392 (code=exited, status=127)

Aug 03 22:53:15 r3s1 systemd[1]: Started Docker Application Container Engine.
Aug 03 22:53:15 r3s1 docker[53392]: /usr/bin/docker: relocation error: /usr/bin/docker: symbol d...ence
Aug 03 22:53:15 r3s1 systemd[1]: docker.service: main process exited, code=exited, status=127/n/a
Aug 03 22:53:15 r3s1 systemd[1]: Unit docker.service entered failed state.
Aug 03 22:53:15 r3s1 systemd[1]: Starting Docker Application Container Engine...
Aug 03 22:53:15 r3s1 systemd[1]: docker.service start request repeated too quickly, refusing to start.
Aug 03 22:53:15 r3s1 systemd[1]: Failed to start Docker Application Container Engine.
Hint: Some lines were ellipsized, use -l to show in full.

[root@r3s1 ~]# docker -d
INFO[0000] Listening for HTTP on unix (/var/run/docker.sock) 
docker: relocation error: docker: symbol dm_task_get_info_with_deferred_remove, version Base not defined in file libdevmapper.so.1.02 with link time reference

- Solution: ``yum update -y device-mapper``
    - `docker require proper device-mapper <https://github.com/docker/docker/issues/12108>`_




.. [#] http://aufs.sourceforge.net/
