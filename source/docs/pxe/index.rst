===================================
PXE -- Preboot Execution Enviriment
===================================


Dependencies
============

DHCP-Server
-----------

.. code-block:: bash
    :linenos:

    sudo apt-get install dhcp3-server
    sudo vi /etc/dhcp3/dhcpd.conf
    # next-server tftp-server's-IP;
    # filename "pxelinux.0";
    sudo /etc/init.d/dhcpd restart


tftp-Server
-----------

.. sidebar:: Note

    most pxe files could getting by ``yum install syslinux``

This service is used for launch anaconda

::

    sudo apt-get install tftpd-hpa


vmlinuz & initrd.img from installer's iso image.

======================= ==============================
filename                description
======================= ==============================
pxelinux.0              startup management programs
menu.c32/vesamenu.c32   menu layouts, menu.c32 has darker color
pxelinux.cfg/default    menu items
vmlinuz                 kernel file
initrd.img              core modules
======================= ==============================

| **example**
|

::

    TIMEOUT=600   # wait 600 x 0.1sec
    
    label CentOS 7 - Devstack & hadoop
    MENU LABEL ^[wenjie]----Install CentOS 7 - testing
       kernel vmlinuz_centos70
       ipappend 2
       append ks=ftp://192.168.164.2/centos70.cfg ksdevice=bootif initrd=initrd_centos70.img ramdisk_size=8192 nodmraid


FTP-Server
----------

::

    sudo apt-get install vsftp

- mount an iso installation image::

    sudo vi /etc/fstab
    # /imagepath.iso /ftp_root/os/centos70 iso9660 defaults,loop 0 0
    mount -a   # take effect



Anaconda
========

`Anaconda <http://fedoraproject.org/wiki/Anaconda>`_ is an python based OS installer, some module written w/ C.

| https://fedorapeople.org/cgit/karsten/public_git/anaconda.git/
|

kickstart
=========

`kickstart(ks) <http://fedoraproject.org/wiki/Anaconda/Kickstart>`_ is an installation method/mechanisam

| `official guide <http://www.redhat.com/magazine/024oct06/features/kickstart/>`_
| http://github.com/rhinstaller/pykickstart
|

command section
---------------

+---------------------------------------+------------------------------------------------------------+
|option                                 |description                                                 |
+=======================================+============================================================+
|install / upgrade                      |chose one                                                   |
+---------------------------------------+------------------------------------------------------------+
|text / graphical                       |text mode install faster, but default is graphical          |
+---------------------------------------+------------------------------------------------------------+
|zerombr                                |any disks whose formatting is unrecognized are initialized  |
+---------------------------------------+------------------------------------------------------------+
|clearpart --drivers=sda --all          |clear partition table, change all into none will do nothing |
+---------------------------------------+------------------------------------------------------------+
|part /dir --fstype=ext4 --size=500     |format filesystem, can **grow** from a small **size** like 1|
|  [--grow] [--ondisk=sda] [--asprimary]|                                                            |
+---------------------------------------+------------------------------------------------------------+

other sections
--------------

start section w/ ``%name`` , end w/ ``%end``

=============== ==========================
name            description
=============== ==========================
packages        pkg-groups or pkgs, ``yum grouplist``
pre/post        before/after system installaion, not use 'pre' by normal
=============== ==========================

Examples
--------

| **centos7**
|

.. code-block:: ks

    ##################################################
    install
    ##################################################
    # start to install centos 7.0.1406
    ##################################################
    
    # text installaion mode
    text
    
    #backup installation image url
    #url --url=http://linux-ftp.jf.intel.com/pub/mirrors/centos/7.0.1406/os/x86_64
    url --url=ftp://192.168.164.2/os/centos70
    lang en_US.UTF-8
    keyboard us
    network --device eth0 --bootproto dhcp --gateway 192.168.2.200 --nameserver 10.248.2.1
    
    #root passwd 123456
    rootpw --iscrypted $6$uicFbbbBsSB8hLTL$c18L0LZpPJCg76l4XG8vRK0dOt2KNBwvQz9RPjc4I/TBs.a/a6FgOOMsmFZOuiC386h.TtHSJFcjeZT9L1L0g1
    firewall --disabled
    selinux --disabled
    authconfig --enableshadow --enablemd5
    timezone --utc Asia/Shanghai
    bootloader --location=mbr
    
    #disk allocation
    ################
    zerombr
    clearpart --all
    part biosboot --fstype=biosboot --size=1
    part /boot --fstype=ext4 --size=500 --ondisk=sda
    part / --fstype=ext4 --asprimary --grow --ondisk=sda
    
    
    
    ##################################################
    %packages
    ##################################################
    # install pkg-groups & pkgs during installation
    ##################################################
    
    # pkg groups
    ############
    @base
    @console-internet
    @core
    @debugging
    @directory-client
    @hardware-monitoring
    @java-platform
    @large-systems
    @network-file-system-client
    @performance
    @perl-runtime
    @virtualization-client
    @virtualization-platform
    
    # pkgs
    ######
    pax
    oddjob
    sgpio
    device-mapper-persistent-data
    samba-winbind
    certmonger
    pam_krb5
    krb5-workstation
    perl-DBD-SQLite
    %end
    
    
    ##################################################
    %post
    ##################################################
    # running scripts after installation
    ##################################################
    
    # sync time with gateway
    ########################
    cat >> /etc/ntp.conf << EOF
    server 192.168.2.200
    EOF
    ntpdate 192.168.2.200
    
    # record configuration time
    echo Start configuration at `date +%Y_%m_%d--%H:%M` >> /root/time.txt
    
    
    # default hostname & gateway & dns-servers
    ##########################################
    echo devstoop > /etc/hostname
    cat >> /etc/sysconfig/network << EOF
    HOSTNAME=devstoop
    DNS1=10.248.2.1
    DNS2=10.248.2.5
    DNS3=10.239.27.228
    EOF
    
    
    # adding proxies urls for each bash user
    ########################################
    echo '
    export GIT_PROXY_COMMAND=/usr/bin/git-proxy
    export proxyaddr=proxy-shz.intel.com
    export proxyport=911
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
    ' >> /etc/bashrc
    
    cat >> /etc/bashrc << EOF
    alias sls='screen -x'
    EOF
    
    # git's proxy confs
    ###################
    
    #script for git://
    cat >> /usr/bin/git-proxy << EOF
    #!/bin/sh
    case $1 in
        *.intel.com|192.168.*|127.0.*|localhost|10.*)
            METHOD="-X connect"
        ;;
        *)
            METHOD="-X 5 -x proxy-shz.intel.com:1080"
        ;;
    esac
    /bin/nc.openbsd $METHOD $*
    EOF
    
    chmod +x /usr/bin/git-proxy
    
    cat >> /etc/gitconfig << EOF
    [core]
    gitproxy=/usr/bin/git-proxy
    EOF
    
    # pip's conf
    ############
    cat >> /etc/pip.conf << EOF
    [global]
    default-timeout = 60
    respect-virtualenv = true
    build = /tmp/.pip/build
    download-cache = /tmp/.pip/cache
    index_url = https://pypi.gocept.com/simple/
    
    [install]
    use-mirrors = true
    mirrors = https://pypi.gocept.com
    EOF
    
    # yum's confs
    #############
    cat >> /etc/yum.conf << EOF
    proxy=http://proxy-shz.intel.com:911
    exclude=kernel*
    EOF
    
    # disable gpgcheck
    sed -i s/gpgcheck=1/gpgcheck=0/g /etc/yum.conf
    
    # wget's
    ########
    sed -i s/.yoyodyne.com:18023/-shz.intel.com:911/g /etc/wgetrc
    
    # hosts
    #######
    cat >> /etc/hosts << EOF
    192.168.2.200 gw
    192.168.164.2 pxe
    192.168.11.166 wenjie
    EOF
    
    #############
    # other confs
    #############
    
    # add ssh keys
    ##############
    mkdir -p /root/.ssh
    chmod 700 /root/.ssh
    cat >> /root/.ssh/authorized_keys << EOF
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC9VSDVLkO0QAuS4AmRHgHrySnpCMD3/vf2boEKO7RDSoA0kuAeIijRuoxkO2HpoZ/RrUgJsohzumsmyDRfJC64HZo+mNRQ0WEfUg7hM4QOy+XrPafaghFmhfTcrSbCm65h6vzZ0OjIs8+h98Hjmb7NgrYsyO5LBh4NLVOXpD5VhbpC/AmgPXeUoAXQAI+8By3irfL8A9vGwBkV7bj044fDE7DFMOujA4uWfTxYrqZ/MGWs0KQtn5J5yMMhUZft/3LNxnhGbXIp6e4J8o+51TidABwXDUMg8w0G1wv1vQbbTJA9mrrGzK3T5h8fM0zEsdOkUKcv8VW5+GFdyBvpQee/ root@prime
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDlBX6kzdnvlic6DgQTiQZun6Cow0x5KMM3LleRoUSGNqkNY1581cYxTTn/bwdLjChyR/BTCa9IdAD0oGZ18C6hwao2SvHTDi61ceHLwVcXxzc441fYUx1e913tljWKKaNayMppsYIx92BAmw1/YlxjghXoR3A1vqTyAAZGqOLKu/Bbqt4jb2FPHZ1V4IQyeLB5JO55+NyxCebQkRloFCA4E5BNG+rF562O4VjfAZkOec8vmOjWMZCxH5L+f6oOX/JgV7rYnSZGuvEPnvYZCENWVUTPb0ddm7i8hf3AWUIKgqk63X+L2sHrQovSF9F1LHNbtGenMQI6h7Ph5D7qGFRR root@wenjie
    EOF
    chmod 644 /root/.ssh/authorized_keys
    chown root.root /root -R
    
    # add tab view for screen
    #########################
    cat >> /etc/screenrc << EOF
    caption always '%{=b cw}%-w%{=rb db}%>%n %t%{-}%+w%{-b}%< %{= kG}%-=%D %c%{-}'
    shelltitle '$ |bash'
    EOF
    
    # unlimit normal users
    ######################
    cat >> /etc/security/limits.conf << EOF
    *                -       nproc           100000
    *                -       nofile          100000
    *                -       memlock         unlimited
    EOF
    
    
    ##########################
    # add stack & hadoop users
    ##########################
    
    # add user stack with devstack
    ##############################
    groupadd stack
    useradd -g stack -s /bin/bash -d /opt/stack -m stack
    echo "stack ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers 
    passwd stack --stdin << EOF
    123456
    EOF
    
    # add user hadoop with hadoop-2.6.0
    ###################################
    groupadd hadoop
    useradd -g hadoop -s /bin/bash -d /home/hadoop -m hadoop
    echo "hadoop ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers 
    passwd hadoop --stdin << EOF
    123456
    EOF
    
    # script for changing hostname 
    ##############################
    echo '#!/bin/bash 
    hostname $1
    echo $1 > /etc/hostname
    #echo "127.0.0.1 $1" >> /etc/hosts 
    sed -i s/HOSTNAME=.*/HOSTNAME=$1/g /etc/sysconfig/network 
    ' > /root/changehost.sh
    chmod +x /root/changehost.sh
    
    ##########################
    # record installation time
    ##########################
    
    echo Finish configuration at `date +%Y_%m_%d--%H:%M` >> /root/time.txt
    
    %end
    
    reboot





