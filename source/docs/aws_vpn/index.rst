==================
Build VPN with AWS
==================


What's VPN
==========

- TCP(1723) is required for PPTP packets
- TCP(1701) is required for L2TP packets
- compare to proxy, vpn provide ...



Deployment 
==========

PPTP VPN
--------

.. code-block:: shell

    sudo yum install -y ppp
    sudo rpm -ivh http://static.ucloud.cn/pptpd-1.3.4-2.el6.x86_64.rpm

- Edit ``/etc/pptp.conf`` -- config localip & guestip::

    localip 172.31.5.164
    remoteip 172.31.5.165-180

- Edit ``/etc/ppp/options.pptpd`` -- config dns server for pptp server ::

    # require local dns
    ms-dns 172.31.0.2

- Edit ``/etc/ppp/chap-secrets`` -- add pptp client account::

    # client        server      secret            IP addresses
      account       pptpd       password          *

- Edit ``/etc/sysctl.conf`` then apply the changes ``sysctl -p`` ::

    net.ipv4.ip_forward = 1

- Start pptp daemon

.. code-block:: shell

    iptables -t nat -A POSTROUTING -s 172.31.5.0/24 -o eth0 -j MASQUERADE
    iptables-save > /etc/sysconfig/iptables
    service pptpd start
    # startup automatically
    chkconfig pptpd on
    chkconfig iptables on



Script for quick deployment
---------------------------


following script should run as root user

.. code-block:: bash
    :linenos:

    # prepare
    # -------
    LOCALIP=172.31.5.164
    REMOTEIP=172.31.5.165-180
    MSDNS=172.31.0.2
    CIDR=172.31.5.0/24
    NIC=${NIC:-eth0}
    ACCOUNT=${ACCOUNT:-account}
    PASSWD=${PASSWD:-passwd}

    # install
    # -------
    yum install -y ppp
    rpm -ivh http://static.ucloud.cn/pptpd-1.3.4-2.el6.x86_64.rpm

    # config
    # ------
    echo "localip $LOCALIP
    remoteip $REMOTEIP" >> /etc/pptpd.conf
    echo "ms-dns $MSDNS" >> /etc/ppp/options.pptpd
    echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf
    # sysctl -w net.ipv4.ip_forward=1
    echo "  ACCOUNT       pptpd       passwd          *" >> /etc/ppp/chap-secrets
    iptables -t nat -A POSTROUTING -s $CIDR -o $NIC -j MASQUERADE
    iptables-save > /etc/sysconfig/iptables

    # startup & auto-startup
    # ----------------------
    service pptpd start
    chkconfig pptpd on
    chkconfig iptables on



