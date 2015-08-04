=====
Linux
=====


Getting Helps
=============

.. code-block:: bash

    apropos <key>   # search all available help for key
    man -k <key>   # search all available man's help for key
    man -n <key>   # show level-n's help for key
    info <key>
    help <key>    # for built-in cmds



Configuration file
==================

``/etc/rc.local`` executed at the end of each multiuser runlevel


Pseudo-filesystem
-----------------

- ``/proc`` -- process infomation pseudo-filesystem
    - only files under ``proc/sys`` can be changed via ``echo >``
- ``/dev/zero`` -- echo endless zeros
- ``/dev/null``  -- black hole, devour everything


User Managemanet
================

.. code-block:: bash
    :linenos:

    id <username>
    useradd <username>
    userdel -r <username>   # del everything about user
    gpasswd -a <user> <group>
    gpasswd -d <user> <group>



usermod
^^^^^^^

.. code-block:: bash
    :linenos:

    usermod -G <group> <user>   # add user to group
    usermod -l <old> <new>   # change username
    usermod -L <user>   # lock user's account
    usermod -U <user>   # unlock user's account



Kernel Management
=================


sysctl
------

configure kernel parameters at runtime

.. code-block:: bash

    # take effect /etc/sysctl.conf
    sysctl -p
    # tack effect specified config file
    sysctl -f sysctl.conf -p
    # print all current sysctl variables.
    sysctl -a
    # change kernel variable once, only write into /etc/sysctl.conf will take effect permantly
    # ip forward is used to forward packets from one interface to another.
    sysctl -w net.ipv4.ip_forward=1
    # will not response pinging
    sysctl -w net.ipv4.icmp_echo_ignore_all=1
    # will not response broadcasts, defaut 0 since rhel5
    sysctl -w net.ipv4.icmp_echo_ignore_broadcasts=1



