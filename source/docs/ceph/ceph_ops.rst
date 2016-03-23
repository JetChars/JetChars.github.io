==============
Ceph Operation
==============


Ceph managed by upstar, which leave users w/o define daemon.


.. sidebar:: Upstart

    Upstart is an event-based replacement for the /sbin/init daemon which handles starting of tasks and services during boot, stopping them during shutdown and supervising them while the system is running.
    It was originally developed for the Ubuntu distribution, but is intended to be suitable for deployment in all Linux distributions as a replacement for the venerable System-V init.
    `initctl <http://manpages.ubuntu.com/manpages/raring/en/man8/initctl.8.html>`_



.. code-block:: shell

    # using 'initctl list' get available ceph daemons
    # user can start or stop group of daemons
    # or manage w/ it's id/hostname
    # ===============================================
    sudo intictl list | grep ceph
    sudo start ceph-all   # start all in current host
    sudo stop ceph-all
    sudo start ceph-osd-all   # start all OSDs
    sudo start ceph-mon-all
    sudo start ceph-mds-all
    sudo stop ceph-osd-all
    sudo stop ceph-mon-all
    sudo stop ceph-mds-all
    sudo start ceph-osd id={id}
    sudo start ceph-mon id={hostname}
    sudo start ceph-mds id={hostname}
    sudo stop ceph-osd id={id}
    sudo stop ceph-mon id={hostname}
    sudo stop ceph-mds id={hostname}



ceph-conf
---------

ceph conf file tool [#]_

.. code-block:: console

    $ ceph -L   # will list all sections
    gloabl
    mon
    $ ceph -l global   # will display specified section
    global




Management
==========


OSD
---

- Remove OSD

.. code-block:: shell

    ceph osd out 5                 # mark it down
    service ceph -a stop osd.5     # if not working using following cmd
    sudo kill `ps aux | grep 'ceph -i 5' | awk '{print $2}'`   # kill osd process
    ceph osd crush remove osd.5
    ceph auth del osd.5            # remove auth info
    ceph osd rm 5                  # remove osd







References
==========
==========


.. [#] http://docs.ceph.com/docs/master/man/8/ceph-conf/

