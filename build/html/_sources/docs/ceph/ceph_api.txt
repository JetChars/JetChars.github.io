
=========
Ceph APIs
=========

LIBRADOS
========

librados ralize the messaging layer protocol, enable ceph-client comm w/ ceph-nodes.
- librados support multi-lang
    - librados-dev -- C/C++ version
    - librados-python -- python version
    - java verion will be unfriendly


.. code-block:: python

    import rados, sys

    # use default or designate conffile, even specify a keyring
    # =========================================================
    cluster = rados.Rados(conffile='/etc/ceph/ceph.conf')
    cluster = rados.Rados(conffile=sys.argv[1])
    cluster = rados.Rados(conffile=sys.argv[1], conf=dict(keyring='/path/to/keyring'))

    # conn to ceph cluster and manage pools
    # =====================================
    cluster.connect()
    cluster_stats = cluster.get_cluster_stats()
    pools = cluster.list_pools()
    cluster.create_pool('test')
    cluster.delete_pool('test')

    # r/w w/ ioctx
    ioctx = cluster.open_ioctx('mypool')
    ioctx.write_full("hw", "Hello World!")
    print ioctx.read("hw")
    ioctx.remove_object("hw")




LIBRBD
======

- librbd does not know how to deal w/ characters wider than a **:c:type:char**
    - image -- a block device, can be attached to a VM. consist of multiple object
    - snapshot -- a preservation of image. used to recovery image(clone).

.. image:: /images/ceph/ceph_librbd_path.png

- librbd is suited for VM useage, which is much stable. on the other side krbd is used for the Host.


.. image:: /images/ceph/ceph_librbd_snapshot.png

- while reading objs, data could be derived from it's parent volume.



Example of creating & writing to an image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. code-block:: python

    # conn to RADOS & open a IO context
    # =================================
    cluster = rados.Rados(conffile='my_ceph.conf')
    cluster.connect()
    ioctx = cluster.open_ioctx('mypool')

    # instantiate an :class:rbd.RBD obj
    # =================================
    rbd_inst = rbd.RBD()
    size = 4 * 1024**3  # 4 GiB
    rbd_inst.create(ioctx, 'myimage', size)

    # perform I/O on the image
    # ========================
    image = rbd.Image(ioctx, 'myimage')
    data = 'foo' * 200
    image.write(data, 0)   # write first 600 bytes

    # close the image, IO context & RADOS connection
    image.close()
    ioctx.close()
    cluster.shutdown()


- properly way

.. code-block:: python

    cluster = rados.Rados(conffile='my_ceph_conf')
    try:
        ioctx = cluster.open_ioctx('my_pool')
        try:
            rbd_inst = rbd.RBD()
            size = 4 * 1024**3  # 4 GiB
            rbd_inst.create(ioctx, 'myimage', size)
            image = rbd.Image(ioctx, 'myimage')
            try:
                data = 'foo' * 200
                image.write(data, 0)
            finally:
                image.close()
        finally:
            ioctx.close()
    finally:
        cluster.shutdown()

- simpler way

.. code-block:: python

    with rados.Rados(conffile='my_ceph.conf') as cluster:
        with cluster.open_ioctx('mypool') as ioctx:
            rbd_inst = rbd.RBD()
            size = 4 * 1024**3  # 4 GiB
            rbd_inst.create(ioctx, 'myimage', size)
            with rbd.Image(ioctx, 'myimage') as image:
                data = 'foo' * 200
                image.write(data, 0)


API reference
^^^^^^^^^^^^^

Error --> PermissionError
      --> IOError



References
==========
==========


.. [#] http://www.tuicool.com/articles/mYbEn2u
