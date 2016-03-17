======
Ubuntu
======

Shortcuts
=========






Installation
============
============

ubuntu 14.10 boot w/ syslinux, but ultraISO not support it. [#]_

Termial Mode Configuration
--------------------------

.. code-block:: bash

    # can change encode, font size, keyboard layout
    sudo dpkg-reconfigure console-setup

Configure Wireless NIC
----------------------

.. sidebar:: Note

    iwconfig not support PSK encryption::

        iwconfig wlan0 key helloworld
        Error for wireless request "Set Encode" (8B2A) :
            SET failed on device eth1 ; Invalid argument.

    in this situation, we can use wpa_supplicant::

        echo '
        ctrl_interface=/var/run/wpa_supplicant
        # make sure only root user can access conf-file
        ctrl_interface_group=0
        # it can be change into 0 or 2, but ony mode 1 works
        ap_scan=1
        network={
           ssid="ssidname"
           psk="passwd" 
        }' > /etc/wpa_supplicant.conf

        # take effect configurations
        wpa_supplicant -B -Dnl80211 -iwlan0 -c/etc/wpa_supplicant.conf

.. code-block:: bash

    # power on wnic
    iwconfig wlan0 txpower on
    # get ssid list
    iwlist wlan0 scan | grep -i ssid
    # connet to a ssid, password come after 'key'
    iwconfig wlan0 essid ChinaNet
    iwconfig wlan0 essid ChinaNet key <password>
    # enable wnic after configuration
    ifconfig wlan0 up
    dhclient wlan0

Install gnome
-------------

.. code-block:: bash
    :linenos:

    # Personal Package Archives(short for ppa, provided by ubuntu)
    sudo add-apt-repository ppa:gnome3-team/gnome3
    sudo apt-get update
    sudo apt-get install gnome-shell ubuntu-gnome-desktop

    # unity desktop
    sudo apt-get install ubuntu-desktop

    # kde desktop
    sudo apt-get install kubuntu-desktop
    sudo apt-get install language-pack-kde-zh language-pack-kde-zh-base language-pack-zh language-pack-zh-base language-support-zh

    # change font size, get tweak tool
    sudo apt-get install unity-tweak-tool

APT (Advanced Package Tool)
===========================
===========================

It is the command-line tool for handling packages

Configuration files
-------------------

.. sidebar:: aliyun's trusty(14.04) source

    .. code-block:: guess

        # deb cdrom:[Ubuntu 14.04.1 LTS _Trusty Tahr_ - Release amd64 (20140722.2)]/ trusty main restricted

        # See http://help.ubuntu.com/community/UpgradeNotes for how to upgrade to
        # newer versions of the distribution.
        deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted
        deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted

        ## Major bug fix updates produced after the final release of the
        ## distribution.
        deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted
        deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted

        ## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
        ## team. Also, please note that software in universe WILL NOT receive any
        ## review or updates from the Ubuntu security team.
        deb http://mirrors.aliyun.com/ubuntu/ trusty universe
        deb-src http://mirrors.aliyun.com/ubuntu/ trusty universe
        deb http://mirrors.aliyun.com/ubuntu/ trusty-updates universe
        deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates universe

        ## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu 
        ## team, and may not be under a free licence. Please satisfy yourself as to 
        ## your rights to use the software. Also, please note that software in 
        ## multiverse WILL NOT receive any review or updates from the Ubuntu
        ## security team.
        deb http://mirrors.aliyun.com/ubuntu/ trusty multiverse
        deb-src http://mirrors.aliyun.com/ubuntu/ trusty multiverse
        deb http://mirrors.aliyun.com/ubuntu/ trusty-updates multiverse
        deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates multiverse

        ## N.B. software from this repository may not have been tested as
        ## extensively as that contained in the main release, although it includes
        ## newer versions of some applications which may provide useful features.
        ## Also, please note that software in backports WILL NOT receive any review
        ## or updates from the Ubuntu security team.
        deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
        deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse

        deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted
        deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted
        deb http://mirrors.aliyun.com/ubuntu/ trusty-security universe
        deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security universe
        deb http://mirrors.aliyun.com/ubuntu/ trusty-security multiverse
        deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security multiverse

        ## Uncomment the following two lines to add software from Canonical's
        ## 'partner' repository.
        ## This software is not part of Ubuntu, but is offered by Canonical and the
        ## respective vendors as a service to Ubuntu users.
        # deb http://archive.canonical.com/ubuntu trusty partner
        # deb-src http://archive.canonical.com/ubuntu trusty partner

        ## This software is not part of Ubuntu, but is offered by third-party
        ## developers who want to ship their latest software.
        deb http://extras.ubuntu.com/ubuntu trusty main
        deb-src http://extras.ubuntu.com/ubuntu trusty main


    

1. ``/etc/apt/source.list`` Repositories list::

    DebType AddressType://Hostaddress/Ubuntu Distribution Component1 Component2 ...

  - DebType: 'deb' means binary, 'deb-src' means source-codes
  - AddrType: http/file/ftp/cdrom/ssh
  - Distribution: dapper/feisty/trusty(14.04)
  - resource types
      - main -- supported by Canonical society
      - universe -- maintain by community
      - restricted -- dedicated driver for devices
      - multiverse -- have copyright and legitimacy issue


2. ``/etc/apt/apt.conf`` overall conf-file::

    Acquire::http::Proxy::linux-ftp.sc.intel.com "DIRECT";
    Acquire::http::Proxy "http://proxy-shz.intel.com:911/";
    Acquire::https::Proxy "https://proxy-shz.intel.com:911/";
    Acquire::ftp::Proxy "ftp://proxy-shz.intel.com:911/";
    Acquire::socks::Proxy "socks://proxy-shz.intel.com:911/";


apt-get
-------

- install

.. code-block:: bash

    apt-get install <pkg>  # multiple pkgs seperated by space
    apt-get install --reinstall <pkg>
    apt-get install -f <pkg>  # fix pkg and dependencies


- uninstall

.. code-block:: bash

    apt-get remove --purge -y <pkg>
    apt-get autoremove -y  # remove obsolete pkgs
    apt-get autoclean -y  # clean removed pkg's dependencies


- others

.. code-block:: bash

    apt-get source [-d] <pkg>    # download src code to current folder, compile src code w/ -d
    apt-get download <pkg>   # download binary to current folder
    apt-get build-dep <pkg>  # make pkg's dependencies
    apt-get update  # update repo
    apt-get dist-update  # upgrade os
    apt-get clean  # remove downloaded pkgs ``/var/cache/apt/archives``


apt-cache
---------

.. code-block:: bash

    apt-cache search <pkg>   # search w/ regex
    pkgnames  # list all installed pkgnames
    apt-cache stats    # list statistic infos
    apt-cache show <pkg>   # show pkg's detail online
    apt-cache depends <pkg>  # show pkg's dependencies
    apt-cache rdepends <pkg>  # show pkgs depends on this pkg


DPKG
====

.. code-block:: shell

    # install or remove a deb binary
    dpkg -i <pkgname>   
    dpkg -r <pkgname>
    dpkg -P <pkgname>   # will purge deb completely
    # show pkg list
    dpkg -l
    dpkg -l | grep <pkg>




.. [#] https://bugs.launchpad.net/ubuntu/+source/usb-creator/+bug/1325801
