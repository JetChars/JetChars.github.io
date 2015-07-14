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
