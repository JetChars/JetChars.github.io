.. image:: images/intel_logo.png
    :align: right
    :width: 250px


=============
Work at Intel
=============




Networking
==========

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




export proxies
--------------

.. code-block:: bat

    export http_proxy=http://10.239.4.80:913
    export https_proxy=https://10.239.4.80:913
    export ftp_proxy=ftp://10.239.4.80:913
    export socks_proxy=socks://10.239.4.80:913
    export no_proxy=localhost,*intel.com:913,172.16.0.0/16,10.0.0.0/8,127.0.0.0/8
    export HTTP_PROXY=http://10.239.4.80:913
    export HTTPS_PROXY=https://10.239.4.80:913
    export FTP_PROXY=ftp://10.239.4.80:913
    export SOCKS_PROXY=socks://10.239.4.80:913
    export NO_PROXY=localhost,*intel.com:913,172.16.0.0/16,10.0.0.0/8,127.0.0.0/8





command-prompt proxies
----------------------

.. code-block:: bat

    set http_proxy=http://10.239.4.80:913
    set https_proxy=https://10.239.4.80:913
    set ftp_proxy=ftp://10.239.4.80:913
    set socks_proxy=socks://10.239.4.80:913
    set no_proxy=localhost,*intel.com:913,172.16.0.0/16,10.0.0.0/8,127.0.0.0/8
    set HTTP_PROXY=http://10.239.4.80:913
    set HTTPS_PROXY=https://10.239.4.80:913
    set FTP_PROXY=ftp://10.239.4.80:913
    set SOCKS_PROXY=socks://10.239.4.80:913
    set NO_PROXY=localhost,*intel.com:913,172.16.0.0/16,10.0.0.0/8,127.0.0.0/8




use intel proxy 
----------------


- use ssh as http proxy


.. code-block:: bash

    # Privileged ports can only be forwarded by root.
    # can't use domain because of dns can't resolve internal domain
    # web browser should use http as proxy protocol
    # because of firewall tunnel can't built at working laptop
    # minimal configuration
    sudo ssh -N -L 0.0.0.0:913:172.16.213.225:913 wenjieca@192.168.199.116
    # compress and run in background
    sudo ssh -fgCNL 0.0.0.0:913:172.16.213.225:913 wenjieca@192.168.199.116


- use command-prompt  as socks5 proxy
    - can't access lots of sites, eg: google,youtube ...
    - can access facebook,z.cn ...
    - not work w/ ios

.. code-block:: cmd

    netsh interface portproxy add v4tov4 listenport=1080 connectaddress=10.239.4.80 connectport=1080
    netsh interface portproxy show all
    netsh interface portproxy set v4tov4 listenport=8080 connectaddress=10.239.4.80 connectport=1080
    netsh interface portproxy delete v4tov4 listenport=8080



Find out occupied IPs
---------------------

.. code-block:: bash

    >ip_occupied;for i in `seq 1 6`;do for j in `seq 1 255`;do bash -c "ping -w1 -c1 172.16.$i.$j | grep ttl | cut -d' ' -f4 | cut -d: -f1 | tee -a ip_occupied &" ;done;done
    arp-scan -I eth0 -l   # will check every IP eth0 can access locally
