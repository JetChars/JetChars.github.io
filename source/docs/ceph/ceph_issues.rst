===========
Ceph Issues
===========


Installation issues
===================
===================

err upgrade cluster
-------------------

this err occurs when upgrade firefly to hammer

.. code-block:: console

    $ ceph-deploy install --version hammer ceph-admin ceph-mon ceph-osd1 ceph-osd2 ceph-msd ceph-rgw
    [ceph-admin][INFO  ] Running command: sudo env DEBIAN_FRONTEND=noninteractive apt-get -q install --assume-yes ca-certificates
    [ceph-admin][WARNIN] E: Unmet dependencies. Try 'apt-get -f install' with no packages (or specify a solution).
    [ceph-admin][DEBUG ] Reading package lists...
    [ceph-admin][DEBUG ] Building dependency tree...
    [ceph-admin][DEBUG ] Reading state information...
    [ceph-admin][DEBUG ] ca-certificates is already the newest version.
    [ceph-admin][DEBUG ] You might want to run 'apt-get -f install' to correct these:
    [ceph-admin][DEBUG ] The following packages have unmet dependencies:
    [ceph-admin][DEBUG ]  ceph-common : Breaks: ceph (< 0.94.2-2) but 0.80.11-1trusty is to be installed
    [ceph-admin][ERROR ] RuntimeError: command returned non-zero exit status: 100
    [ceph_deploy][ERROR ] RuntimeError: Failed to execute command: env DEBIAN_FRONTEND=noninteractive apt-get -q install --assume-yes ca-certificates



Err upgrade debian
------------------

.. code-block:: console

    $ sudo apt-get install -fy   # try to fix current issues
    Unpacking ceph (0.94.6-1trusty) over (0.80.11-1trusty) ...
    dpkg: error processing archive /var/cache/apt/archives/ceph_0.94.6-1trusty_amd64.deb (--unpack):
     trying to overwrite '/usr/share/man/man8/ceph-deploy.8.gz', which is also in package ceph-deploy 1.4.0-0ubuntu1
     Processing triggers for ureadahead (0.100.0-16) ...
     Processing triggers for man-db (2.6.7.1-1ubuntu1) ...
     Errors were encountered while processing:
      /var/cache/apt/archives/ceph_0.94.6-1trusty_amd64.deb
      E: Sub-process /usr/bin/dpkg returned an error code (1)

solution: ``dpkg -r ceph-deploy && apt-get instll -fy``

- ceph-deploy and ceph are in conflict [#]_




Maintenance issues
==================
==================


clock skew detected on mon
--------------------------

.. code-block:: console

    # ceph health
    HEALTH_WARN clock skew detected on
    mon.ceph-osd2, mon.ceph-mon 
    Monitor clock skew detected


- Add key-vals into ceph.conf

.. code-block:: guess

    [mon.{hostname of MON}]
    host = {hostname of MON}
    mon_data = /var/lib/ceph/mon/ceph-{hostname of MON}/
    mon_addr = {IP of MON}:6789
    mon clock drift allowed = 2
    mon clock drift warn backoff = 30

- Then sync config: ``ceph-deploy --overwrite-conf admin {hostname of MON}``
- Restart MON: ``/etc/init.d/ceph restart mon``
- Verify: ``ceph -w``




References
==========


.. [#] https://bugs.launchpad.net/ubuntu/+source/ceph/+bug/1475910