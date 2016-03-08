============
Apache Httpd
============


Install
=======

.. code-block:: shell

    sudo apt-get install apache2 -y



Management
==========

.. code-block:: shell


    # 3 diff ways to start apache2
    apachctl start
    service httpd start
    /etc/init.d/apache2 start




config files
------------

- ``/etc/apache2/apache.conf`` -- 

- ``/etc/apache2/ports.conf`` -- users can change http/https access ports

Issues
======

AH00035
-------

Description:
**You don't have permission to access / on this server.**

Apache require the permissons of every parent directory!!

Solution:

.. code-block:: shell

    sudo chomd 755 /root
