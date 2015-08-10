=============
Linux Network
=============

Configurations
==============

- ``/etc/network/interfaces``
    - auto eth0 means auto-open

.. code-block:: guess

    auto eth0
    iface eth0 inet static
        address 192.168.11.66
        netmask 255.255.0.0
        gateway 192.168.2.200

- ``/etc/resolv.conf`` -- dns servers
- ``/etc/hostname`` ``/etc/sysconfig/network``

.. code-block:: bash

    hostname   # check current hostname
    hostname newname   # change hostname temporary

- ``/etc/hosts`` -- host names

.. code-block:: bash

    # restart network service to enable configurations
    service networking restart


Home made proxy setting tool
----------------------------

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



Network Trouble Shooting
========================

- Principle of fault investigation -- bottom up, from inside to outside
- Check basic configuration
    - check connectivity -- ``ping gateway`` ``ping g.cn`` ``nslookup``
    - check ip/netmask/gateway -- ``ip a`` ``ip r``
    - check nic -- ``ethtool eth0``
    - check configuration files
    - check enabled standard ports
- Network quality testing
    - check weakness node ``mtr g.cn``
    - check bandwidth -- ``iperf``
    - check trace route&path
        - check which nodes will go through -- ``traceroute``
        - check the mtu size of this path -- ``tracepath``
- Website stress testing
    - apache bench::
  
        apt-get install apache2-utils
        ab -c 100 -n 10000 http://z.cn/  # 100 concurrency, totally 10000 requests

WebSite Errs
------------

========= =======================
Error NO. Definition
========= =======================
400       BAD_REQUEST
401       UNAUTHORIZED
403       FORBIDDEN
404       NOT_FOUND
405       METHOD_NOT_ALLOWED
408       REQUEST_TIME_OUT
410       GONE
411       LENGTH_REQUIRED
412       PRECONDITION_FAILED
413       REQUEST_ENTITY_TOO_LARGE
414       REQUEST_URI_TOO_LARGE
415       UNSUPPORTED_MEDIA_TYPE
500       INTERNAL_SERVER_ERROR
501       NOT_IMPLEMENTED
502       BAD_GATEWAY
503       SERVICE_UNAVAILABLE
506       VARIANT_ALSO_VARIES
========= =======================



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
    # all pinged or other connected addrs will preserve mac addrs
    arp -a


Check NIC
---------

.. code-block:: console

    # ethtool eth0
    Settings for eth0:
        Link detected: yes

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
------------------------------

.. sidebar:: Terms

    | **router** is not a cached name server
    | baidu use godaddy's dns service??


For old systems ``bind`` and ``caching-nameserver`` both required, latter one for obtaining config file **/etc/named.conf**, by default bind's named.conf is caching name server, so no need to install caching-nameserver in latest systems.


dnsmasq
-------

Can provide both dhcp & dns server services. use port 53(ipv4&6,tcp&udp)

configure files:
- ``/etc/dnsmasq.conf`` -- storage dnsmasq's configure
    - all arguments can be used in cmdline w/ prefix '-'
    - can't reload conf file via hup signal
- ``/etc/resolv.dnsmasq.conf`` -- dnsmasq's resolve file

======================================= =====================================
options                                 description
======================================= =====================================
conf-dir=<dir> , -7                     read all conf files in this dir
conf-file=<path> , -c                   specify configure file
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


Route Management
================

- zebra -- route management software



IP commands
===========

show / manipulate routing, devices, policy routing and tunnels

addr/address
------------

.. sidebar:: Note

    - NO-CARRIER -- no network connected
    - inet/inet6 -- ipv4/ipv6 addr

.. code-block:: bash

    ip a[ddr]  # show all address info
    ip a del <cidr> dev <devname>  # rm a cidr in devname
    ip addr del 192.168.58.101/24 dev eth2  # rm cidr in eth2




link -- network device
----------------------

.. code-block:: bash

    ip link show [device]  # show network devices' info
    ip link set device [options]  # change device's configuration
    ip link set p2p1 mtu 1400


route -- routing table management
---------------------------------

local area network route management, at most 250+ route entries

.. sidebar:: Note

    - SIOCADDRT: File exists -- route entriy already exists
        - SIOC -- Serial Input Output Controller
        - ADD -- addition
        - RT -- routing


.. code-block:: bash

    ip r[oute]   # show route table
    ip r a[dd] cidr via ip [dev devname]   # add a route entry
    ip r d[el] cidr   # del a route entry


netns -- network namespace
--------------------------

network namespace is logically another copy of the network stack, with its own route, firewall rules, and network devices
default namespace 'global'


.. code-block:: bash

    ip netns [list]  # show net namespace list
    ip netns add ns1  # add a namespace
    ip link set dev eth1 netns ns1  # allocate physical nic to namespace
    ip netns exec ns1 CMD_UNDET_NETNS  # execute cmd within namespace ns1



rule -- routing policy database management
------------------------------------------





Open vSwitch
============


macvlan
=======

virtualize a nic into several virtual nic, each one owns a mac addr.
maximun 254 virtual nic, current over 10 vnic will cause unstable


4 modes
- bridge -- have a virtual bridge within host
- vepa -- comm via physical bridge
- private -- cann't comm via internal bridge
- passthru -- let vm use host's nic


Getting contents
================

`curl <http://curl.haxx.se/docs/httpscripting.html>`_ client URL
--------------



=================== =========================
opts                detail
=================== =========================
-L, --location      auto redirect to new location
-o, --output <file>               
-s, --silent        quiet mode, no verbose
-S, --show-error
--noproxy <list>
=================== =========================


wget
----



Terms
=====

- **CDN** -- Content Delivery Network, Delivery data according to client's ip or location, to assure fast and stable network.
