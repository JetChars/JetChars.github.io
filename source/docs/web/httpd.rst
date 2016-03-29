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

- ``/etc/apache2/{apache,httpd}.conf`` -- httpd's main configrue file
- ``/etc/apache2/ports.conf`` -- users can change http/https access ports


Features
========

virtual host
------------

- enable vhost at **httpd.conf** -- ``Include /private/etc/apache2/extra/httpd-vhosts.conf``
- add virtual hosts at ``/etc/apache2/extra/httpd-vhosts.conf``

.. code-block:: xml

    <VirtualHost *:8008>
        DocumentRoot "/Users/JetChars/github/autoop/dashboard"
        ServerName sphinx
        ErrorLog "/private/var/log/apache2/sites-error_log"
        CustomLog "/private/var/log/apache2/sites-access_log" common
        <Directory />
                    Options Indexes FollowSymLinks MultiViews
                    AllowOverride None
                    Require all granted
          </Directory>
    </VirtualHost>




Issues
======

try to find solutions at `httpd wiki <http://wiki.apache.org/httpd/FrontPage>`_ first




AH00035
-------

Description:
**You don't have permission to access / on this server.**

Apache require the permissons of every parent directory!!

Solution:

.. code-block:: shell

    sudo chomd 755 /root
