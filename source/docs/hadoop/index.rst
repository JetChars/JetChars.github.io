====================================
`Hadoop <http://hadoop.apache.org>`_
====================================

`wiki <http://wiki.apache.org/hadoop/>`_

.. image:: images/hadoop_evolve.jpg

Unlimit Non-root User's Resources
=================================

.. code-block:: shell
    :linenos:

    sudo rm -rf /etc/security/limits.d
    sudo cat >> /etc/security/limits.conf << EOF
    *                -       nproc           100000
    *                -       nofile          100000
    *                -       memlock         unlimited
    EOF



crunch
======

`CDAP <http://cdap.io>`_
========================


