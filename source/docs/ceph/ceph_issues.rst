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


Err deploy rgw
--------------

.. code-block:: console

    $ ceph-deploy rgw create ceph-rgw
    [ceph_deploy.rgw][DEBUG ] Deploying rgw, cluster ceph hosts ceph-rgw:rgw.ceph-rgw
    [ceph_deploy][ERROR ] RuntimeError: bootstrap-rgw keyring not found; run 'gatherkeys'


- solution: this issue caused by bootstrap-rgw.keying missing, which is only created during installation of cluster running **hammer or newer**.



Maintenance issues
==================
==================


Troubleshooting MON
-------------------


.. code-block:: shell

    ceph-conf --name mon.{ID} --show-config-value {admin_socket}



Troubleshooting OSDs
--------------------


.. code-block:: shell

    # obtaining data about OSDs
    # =========================
    ls /var/log/ceph   # will show current log list
    ls /var/run/ceph   # will show current running sockets
    ceph daemon {daemon-name/socket-file}   # can be "osd.0" or "/var/run/ceph/ceph-osd.0.asok"
    df -h
    iostat -x
    dmesg | tail
    dmesg | grep scsi

    # stopping w/o rebalancing
    # ========================
    ceph osd set noout
    stop ceph-osd id={num}   # start from 0
    start ceph-osd id={num}   # start from 0
    ceph osd unset noout



- admin sockets ``ceph daemon`` allowing you:
    - list you conf at runtime
    - dump historic ops/operation queue stat/ops in flight/perfcounter
- **snoot** will withhold rebalancing while rm OSD
- if OSD can't start
    - check conf(hostname/paths/max_threadcount)
    - check kernel version
    - segment fault -- contact ceph-dev team

An OSD failed
^^^^^^^^^^^^^

.. code-block:: console

    $ ceph health
    HEALTH_WARN 1/3 in osds are down

    $ ceph health detail
    HEALTH_WARN 1/3 in osds are down
    osd.0 is down since epoch 23, last address 192.168.106.220:6800/11080


- using cmd ``ceph health detail`` locate which OSD is down
- Errs will logged at ``/var/log/ceph``
- ``dmesg`` also can show something


No free drive space
^^^^^^^^^^^^^^^^^^^


Networking issues
^^^^^^^^^^^^^^^^^





ceph -s err
-----------

.. code-block:: console

    $ ceph -s
    2016-03-13 05:54:31.854272 7f3fe8269700  0 -- :/3950156637 >> 192.168.56.113:6789/0 pipe(0x7f3fe4060590 sd=3 :0 s=1 pgs=0 cs=0 l=1 c=0x7f3fe405a370).fault
    $ sudo start ceph-mon id=0
    $ dmesg | tail
    [190945.284897] init: ceph-mon (ceph/ceph-mon) main process (23755) terminated with status 28
    [190945.284904] init: ceph-mon (ceph/ceph-mon) respawning too fast, stopped
    [190945.293275] init: ceph-create-keys main process (23758) killed by TERM signal




- which means monitor can't comm w/ the rest fo the cluster.




ceph fs mount err
-----------------

.. code-block:: console

    $ sudo mount -t ceph 192.168.56.113:6789:/ /mnt/mycephfs -o name=admin,secret=AQAsO9hWcAqwJRAAuahZhGDGjQryjaK4AXqUww==
    mount error 5 = Input/output error


auth file can't found
---------------------

.. code-block:: console

    2016-03-12 18:27:05.747204 7f3c8d193700 -1 auth: unable to find a keyring on /etc/ceph/ceph.client.admin.keyring,/etc/ceph/ceph.keyring,/etc/ceph/keyring,/etc/ceph/keyring.bin: (2) No such file or directory
    2016-03-12 18:27:05.747476 7f3c8d193700 -1 monclient(hunting): ERROR: missing keyring, cannot use cephx for authentication
    2016-03-12 18:27:05.747579 7f3c8d193700  0 librados: client.admin initialization error (2) No such file or directory
    Error connecting to cluster: ObjectNotFound


Solution: copy auth files to ``/etc/ceph/`` or use cmd ``ceph admin <nodename>`` in ctrl node.




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
