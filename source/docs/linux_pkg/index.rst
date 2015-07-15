========================
Linux Package Management
========================



apt
===



yum
===


.. code-block:: bash
    :linenos:

    # Find what package provides the given value (online)
    yum provides SOME_STRING   # str can be a cmd
    yum provides lsb_release
    yum install redhat-lsb-core


rpm
===



Applications
============

Check Install
-------------

.. code-block::
    :linenos:

    if ! which $pkgname; then
        sudo apt-get install -y --force-yes $pkgname || sudo yum install -y $pkgname
    fi
