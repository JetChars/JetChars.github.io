======
Docker
======

- Since March 2014
* Use go language
* Use native cpu/syscall/kernel
* Use ``namespace/capabilities/ctrl group/apparmor/netfilter``
* Use ipc namespace communicate between containers
* Require ``libcontainer/lxc/libvirt/systemd-nspawn``
* Managed by DGAB (Docker Governance Advisory Board)
* Advangtages
    * compare to kvm use virtio, docker use AUFS, which is better.
    * light weight 'vm', use less mem than kvm, closer to BM
* Constrains
    * must have same OS kernel
    * kernel 3.8 is minimal, except rhel 2.6.32, 3.10 or higher is recommended
    * can't over commitment
    * v1.10 can't modify files under /etc, v1.20 solved this issue (mount | grep etc)


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
    - docker container not work well w/ proxy, ``add key-values of proxy server before cmds which need proxy``



Install Docker::

    wget -qO- https://get.docker.com/ | sh
    wget -qO- https://test.docker.com/ | sh   # test verison


Update Dockera::

    sudo wget https://get.docker.com/builds/Linux/x86_64/docker-latest -O /usr/bin/docker
    sudo chmod a+x /usr/bin/docker


If you would like to use Docker as a non-root user, you should now consider
adding your user to the "docker" group with something like:

    sudo usermod -aG docker your-user



Commands
--------

.. sidebar:: Note

    - detach a instance ``^p^q``

.. code-block:: shell
    :linenos:

    docker run [-v [hostpath:]path[:mountopts]] [-itd] [--rm] [--name cname] [--volumes-from <container>] <image> CMD
    docker images [-aq]
    docker ps [-aq] [--no-trunc]
    docker kill/stop/inspect/rm <container>
    docker exec <container> CMD
    docker attach <container>
    docker search <image>
    # get backgound container id
    cid=$(docker run -itd)
    # clean docker containers
    docker kill $(docker ps -q)
    docker rm $(docker ps -qa)
    # exec cmd one time through container
    docker run --rm --volumes-from john1 -v $(pwd):/backup busybox tar cvf /backup/john2.tar /john1



    


* `Kubernetes <http://kubernetes.io>`_ is an open source orchestration system for Docker containers
