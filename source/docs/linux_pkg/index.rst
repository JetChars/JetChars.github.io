========================
Linux Package Management
========================



apt
===



yum
===


.. code-block:: bash
    :linenos:

    # Find what package provides the given value (online)
    yum provides SOME_STRING   # str can be a cmd
    yum provides lsb_release
    yum install redhat-lsb-core
    # repo mgmt
    yum-config-manager --save --setopt=<repo>.<key>=<val>


Issues
------

1. One of the configured repositories failed (Unknown)

.. code-block:: console

    Cannot retrieve metalink for repository: epel/x86_64. Please verify its path and try again

**Solution** :

.. code-block:: console


    # proxy child-prc not work well (epel in this case)
    # yum-config-manager --save --setopt=epel.proxy=http://proxy-shz.intel.ocm:911

    # # alternatives
    # # ------------
    # # list suspecious repos
    # grep enabled=1 /etc/yum.repos.d/*
    /etc/yum.repos.d/docker-main.repo:enabled=1
    /etc/yum.repos.d/epel.repo:enabled=1
    # # skip issue, it will be add to /etc/yum.repos.d/epel.repo
    # yum-config-manager --save --setopt=epel.skip_if_unavailable=true
    # sudo yum upgrade ca-certificates --disablerepo=epel
    # yum-config-manager --save --setopt=epel.sslverify=false    





rpm
===


.. code-block:: bash

    rpm -ivh xxx.rpm


Applications
============

Check Install
-------------

.. code-block::
    :linenos:

    if ! which $pkgname; then
        sudo apt-get install -y --force-yes $pkgname || sudo yum install -y $pkgname
    fi
