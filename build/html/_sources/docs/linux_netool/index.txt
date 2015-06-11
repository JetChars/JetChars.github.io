=============
Network Tools
=============


Network Trouble Shooting
========================

Ping
----

``ping [-c count] [-w deadline] [-i interval] [-s packetsize]``

* other options

========= ======================
option    description
========= ======================
f         flood ping, will cause network jam.
b         allow pinging a broadcast address
========= ======================


.. code-block:: bash

    # Find out occupied IPs within 192.168.1.0/24
    for i in `seq 1 255`; do ping -c1 -w1 192.168.1.$i;done | grep ttl

Check DNS
---------

nslookup
^^^^^^^^

.. sidebar:: Alternatives

    - ``host domain_name``
    - ``dig domain_name``


This tool can be use as a command ``nslookup domain_name``, or in a interactive mode

.. code-block:: bash

    server dns_ip    # change dns
    set q=ns         # change query type: a, cname, ns
    domain_name      # query directly







IP commands
===========






.. image:: images/django_logo.svg
    :align: right

Django -- web framework
=======================

`cn version doc <http://django-chinese-docs.readthedocs.org/en/latest/index.html>`_


Open vSwitch
============

Home made proxy setting tool
============================

.. code-block:: shell
    :linenos:

    echo ' 
    #!/bin/bash 
     
    # Use script like this 
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    # source /intel-pxy.sh proxy-ir.intel.com 
    # source /intel-pxy.sh proxy-ir.intel.com 912 
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
     
    proxyaddr=$1 
    proxyport=$2 
    export GIT_PROXY_COMMAND=/usr/bin/git-proxy 
    export proxyaddr=${proxyaddr:-proxy-shz.intel.com} 
    export proxyport=${proxyport:-911} 
    export http_proxy="http://$proxyaddr:$proxyport" 
    export https_proxy="https://$proxyaddr:$proxyport" 
    export ftp_proxy="ftp://$proxyaddr:$proxyport" 
    export socks_proxy="socks://$proxyaddr:$proxyport" 
    export no_proxy="localhost,*intel.com:911,192.168.0.0/16,10.0.0.0/8,127.0.0.0/8" 
    export HTTP_PROXY=$http_proxy 
    export HTTPS_PROXY=$https_proxy 
    export FTP_PROXY=$ftp_proxy 
    export SOCKS_PROXY=$socks_proxy 
    export NO_PROXY=$no_proxy 
    ' > /intel-pxy.sh 
    chmod a+x /intel-pxy.sh 



