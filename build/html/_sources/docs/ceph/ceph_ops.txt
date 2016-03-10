==============
Ceph Operation
==============


Ceph managed by upstar, which leave users w/o define daemon.


.. sidebar:: Upstart

    Upstart is an event-based replacement for the /sbin/init daemon which handles starting of tasks and services during boot, stopping them during shutdown and supervising them while the system is running.
    It was originally developed for the Ubuntu distribution, but is intended to be suitable for deployment in all Linux distributions as a replacement for the venerable System-V init.



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






