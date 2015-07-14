=====
Linux
=====


Configuration file
==================

``/etc/rc.local`` executed at the end of each multiuser runlevel


Pseudo-filesystem
-----------------

- ``/proc`` -- process infomation pseudo-filesystem
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
