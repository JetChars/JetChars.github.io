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

also `online man page <http://www.freebsd.org/cgi/man.cgi>`_



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


Date management
===============


.. code-block:: shell

    hwclock   # show hardware clock
    hwclock --hctosys    # sync hwclock to sysclock
    hwclock --systohc    # sync sysclock to hwclock
    ntpdata <ntpserver>  # sync sysclock manually

- use windows an ntp server
    - HKEY_LOCAL_MACHINE-->SYSTEM-->CurrentControlSet-->services-->W32Time-->TimeProviders-->NtpServer-->Enabled=1
    - restart service windows time
    - or simply cp following as ``.reg`` file, click to overlap reg config

.. code-block:: guess

    Windows Registry Editor Version 5.00

    [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\W32Time\TimeProviders\NtpServer]
    "DllName"=hex(2):25,00,73,00,79,00,73,00,74,00,65,00,6d,00,72,00,6f,00,6f,00,\
      74,00,25,00,5c,00,73,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,77,\
      00,33,00,32,00,74,00,69,00,6d,00,65,00,2e,00,64,00,6c,00,6c,00,00,00
    "Enabled"=dword:00000001
    "InputProvider"=dword:00000000
    "AllowNonstandardModeCombinations"=dword:00000001
    "EventLogFlags"=dword:00000000
    "ChainEntryTimeout"=dword:00000010
    "ChainMaxEntries"=dword:00000080
    "ChainMaxHostEntries"=dword:00000004
    "ChainDisable"=dword:00000000
    "ChainLoggingRate"=dword:0000001e





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



