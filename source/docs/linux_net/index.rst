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

Check DNS connectivity
----------------------

DNS management
==============

`oray <http://www.oray.com/>`_
totally 13 logical root servers all over the world, but there is no one in china. It's a strategic resource.

nslookup
^^^^^^^^

.. sidebar:: Alternatives

    - ``host domain_name``
    - ``dig domain_name``
    - ``ping domain_name``


This tool can be use as a command ``nslookup domain_name``, or interactive mode

.. code-block:: bash

    server dns_ip    # change dns
    set q=ns         # change query type: a, cname, ns
    domain_name      # query directly

bind -- main stream dns server
====

.. sidebar:: Terms

    | **router** is not a cached name server
    | baidu use godaddy's dns service??


For old systems ``bind`` and ``caching-nameserver`` both required, latter one for obtaining config file **/etc/named.conf**, by default bind's named.conf is caching name server, so no need to install caching-nameserver in latest systems.


Route Management
================





IP commands
===========


dnsmasq
=======

Can provide both dhcp & dns server services. use port 53(ipv4&6,tcp&udp)

configure files:
- ``/etc/dnsmasq.conf`` -- storage dnsmasq's configure, all this can use as arguments in cmdline w/ prefix '--'
    - can't reload conf file via hup signal
- ``/etc/resolv.dnsmasq.conf`` -- dnsmasq's resolve file

======================================= =====================================
options                                 description
======================================= =====================================
conf-dir=<dir>                          read all conf files in this dir
conf-file=<path>                        specify configure file
resolv-file=/etc/resolv.dnsmasq.conf    specify path to resolv.conf
strict-order, -o                        search in oredr (each line in /etc/hosts --> /etc/resolv.dnsmasq.conf)
no-hosts, -h                            not read /etc/hosts
listen-address=127.0.0.1,192.168.11.166 seperate each ip w/ comma
address=/<domain>/<ipaddr>              set aname
bind-interfaces                         listen to all interfaces
except-interfaces                       specify interface(s) NOT to listen on
dhcp-option-force                       DHCP option sent even if the client does not request it
======================================= =====================================


- Examples

.. code-block:: guess

    dhcp-option-force=26,1400    # 26 means mtu, 1400 is mtusize


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


Terms
=====

- **CDN** -- Content Delivery Network, Delivery data according to client's ip or location, to assure fast and stable network.
