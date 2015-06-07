========================
Linux Package Management
========================


Check Install
-------------

.. code-block::
    :linenos:

    if ! which $pkgname; then
        sudo apt-get install -y --force-yes $pkgname || sudo yum install -y $pkgname
    fi
