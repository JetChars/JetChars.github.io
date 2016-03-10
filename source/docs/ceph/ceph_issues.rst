===========
Ceph Issues
===========


Installation issues
===================
===================




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
