=============
Work at Intel
=============




intel-proxies
=============

available proxy list
--------------------

====================== =========== =========
domain                 ports       unblocked
====================== =========== =========
proxy-cd.intel.com     911/1080    no
proxy-shz.intel.com    911/1080    no
child-prc.intel.com    913         yes
====================== =========== =========






proxy arguments
---------------

.. code-block:: bash

    http_proxy="http://child-prc.intel.com:913"
    https_proxy="https://child-prc.intel.com:913"
    ftp_proxy="ftp://child-prc.intel.com:913"
    socks_proxy="socks://child-prc.intel.com:913"
    no_proxy="localhost,*intel.com:913,172.16.0.0/16,10.0.0.0/8,127.0.0.0/8"
    HTTP_PROXY="http://child-prc.intel.com:913"
    HTTPS_PROXY="https://child-prc.intel.com:913"
    FTP_PROXY="ftp://child-prc.intel.com:913"
    SOCKS_PROXY="socks://child-prc.intel.com:913"
    NO_PROXY="localhost,*intel.com:913,172.16.0.0/16,10.0.0.0/8,127.0.0.0/8"






