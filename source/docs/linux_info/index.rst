================
Get System Infos
================

Intro
=====

This chapter is important for people who are care about performance.

linux get system version info
-----------------------------

For any os
^^^^^^^^^^

.. code-block:: bash
    :linenos:

    cat /etc/issue
    cat /proc/version
    uname -a/-v/-r


For Ubuntu
^^^^^^^^^^

.. code-block:: bash
    :linenos:

    lsb_release -a



For Centos
^^^^^^^^^^

.. code-block:: bash
    :linenos:

    cat /etc/redhat-release
    rpm -q centos-release    



tar folder /etc
---------------

print infos
-----------

proc infos
----------



Enviroments
===========

- ``env`` - run a program in a modified environment
- ``printenv`` - print all or part of environment

w/ no parameters these too cmds gave same results.

username
--------

.. code-block:: console

    $ echo $USER
    $ echo $USERNAME
    $ id   # display current IDs
    uid=0(root) gid=0(root) groups=0(root)
    $ id -u   # only display userid
    0
    $ id -un   # only display username
    root
    $ whoami   #print effective userid
    root


- id
    - print real and effective user and group IDs

================== ==================================
options            descriptions
================== ==================================
-a                 ignore, for compatibility with other versions
-Z, --context      print only the security context of the current user
-g, --group        print only the effective group ID
-G, --groups       print all group IDs
-n, --name         print a name instead of a number, for -ugG
-r, --real         print the real ID instead of the  effective  ID,  with       -ugG
-u, --user         print only the effective user ID
--help             display this help and exit
--version          output version information and exit
================== ==================================



lscommands
==========

.. code-block:: bash

    lscpu
    lsmod
    lspci | grep net   # check nic model&vendor
    sudo lshw -C network | grep -i xg -A10 -B1


.. code-block:: console

    [root@r16s12 ~]# lshw -c network | grep 192
    configuration: autonegotiation=off broadcast=yes driver=ixgbe driverversion=3.15.1-k duplex=full firmware=0x5e0b0001 ip=192.168.16.12 latency=0 link=yes multicast=yes speed=10Gbit/s


