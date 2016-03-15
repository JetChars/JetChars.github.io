
=========
Ceph APIs
=========


LIBRBD
======

- librbd does not know how to deal w/ characters wider than a **:c:type:char**

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







