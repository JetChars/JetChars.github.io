====================================
OpenStack installation with `DevStack <http://git.openstack.org/cgit/openstack-dev/devstack/>`_
====================================


Revision <1.0>

Last Print Date: DATE \\@ "yy/M/d" 3/19/2015 - DATE \\@ "AM/PMh:mm"
11:23 AM

**Primary Author(s): Wenjie, Cai <wenjie.cai@intel.com>**

**Key Contributors: Weiting, Chen Lin, Qi**

TOC \\o 2-4 \\t "Title, 5"

Multi-Node OpenStack installation with DevStack PAGEREF \_Toc \\h 1

Network Configuration PAGEREF \_Toc1 \\h 4

1. Network interface Configuration PAGEREF \_Toc2 \\h 5

2. Connect outside of Intel PAGEREF \_Toc3 \\h 5

1) Environment variables PAGEREF \_Toc4 \\h 5

2) Git Proxy Command PAGEREF \_Toc5 \\h 6

3) Pip index URL PAGEREF \_Toc6 \\h 6

4) apt configuration PAGEREF \_Toc7 \\h 7

DevStack Configuration PAGEREF \_Toc8 \\h 9

1. Preparation PAGEREF \_Toc9 \\h 10

Add third party repositories (EPEL, rpmforge, atomic, PUIAS) for
CentOS6.5 PAGEREF \_Toc10 \\h 10

Upgrade python 2.6 to 2.7 for CentOS6.5 PAGEREF \_Toc11 \\h 11

Add the DevStack User PAGEREF \_Toc12 \\h 11

Install NTP, change time zone into shanghai. PAGEREF \_Toc13 \\h 11

ssh login without password PAGEREF \_Toc14 \\h 12

1. Fire up DevStack PAGEREF \_Toc15 \\h 12

To work via the CLI PAGEREF \_Toc16 \\h 17

Tips PAGEREF \_Toc17 \\h 20

1) Tool screen can create screens; each screen might have lots of
       windows. PAGEREF \_Toc18 \\h 20

2) Hostname PAGEREF \_Toc19 \\h 20

3) Reset the bridge PAGEREF \_Toc20 \\h 20

4) Logs PAGEREF \_Toc21 \\h 20

5) config files PAGEREF \_Toc22 \\h 21

6) Sahara plugins PAGEREF \_Toc23 \\h 22

7) Multi-Node swift configuration PAGEREF \_Toc24 \\h 23

8) Debugging Neutron issues PAGEREF \_Toc25 \\h 25

Troubleshooting PAGEREF \_Toc26 \\h 27

1. Pip issues PAGEREF \_Toc27 \\h 27

2. Screen issue PAGEREF \_Toc28 \\h 30

3. olso issue PAGEREF \_Toc29 \\h 31

4. Dashboard issues PAGEREF \_Toc30 \\h 31

5. Python issue PAGEREF \_Toc31 \\h 32

6. Rabbit issues PAGEREF \_Toc32 \\h 32

7. MySQL issue PAGEREF \_Toc33 \\h 33

8. Cinder issue PAGEREF \_Toc34 \\h 33

9. Nova issues PAGEREF \_Toc35 \\h 33

\ *Network Configuration*

The Multi-Node tutorial does not cover all the configurations we need to
face in a normal environment or an environment with network connections
restrains.

Among all issues, Network connection is the biggest one. It contains
lots of sub issues.

1. Network interface Configuration

$ vi /etc/network/interfaces

auto p1p1

iface p1p1 inet static

address 192.168.11.67

netmask 255.255.0.0

network 192.168.0.0

broadcast 192.168.255.255

gateway 192.168.2.200

dns-nameservers 10.248.2.5 10.239.27.228 172.17.6.9

dns-search sh.intel.com

auto p2p1

iface p2p1 inet manual

up ifconfig $IFACE 0.0.0.0 up

down ifconfig $IFACE 0.0.0.0 down

2. Connect outside of Intel

Since we use ubuntu to install the OpenStack enviroment, lots of tools
need to be installed by apt, which need an http\_proxy or https\_proxy
to connect the internet. Pip and git also need some configuration to
access the internet.

List of available proxy servers:

proxy-shz.intel.com:911 #cannot over the wall

proxy-ir.intel.com:911

proxy-sc.socks.intel.com:1080

proxy-jf.intel.com:1080

1) Environment variables [1]_

Add below to **/etc/enviroments**

GIT\_PROXY\_COMMAND=/usr/bin/git-proxy

http\_proxy="*http://proxy-shz.intel.com:911*\ "

https\_proxy="*https://proxy-shz.intel.com:911*\ "

ftp\_proxy="*ftp://proxy-shz.intel.com:911*\ "

socks\_proxy="*socks://proxy-shz.intel.com:911*\ "

no\_proxy="localhost,\*intel.com:911,192.168.0.0/16,10.0.0.0/8,127.0.0.0/8"

HTTP\_PROXY="*http://proxy-shz.intel.com:911*\ "

HTTPS\_PROXY="*https://proxy-shz.intel.com:911*\ "

FTP\_PROXY="*ftp://proxy-shz.intel.com:911*\ "

SOCKS\_PROXY="*socks://proxy-shz.intel.com:911*\ "

NO\_PROXY="localhost,\*intel.com:911,192.168.0.0/16,10.0.0.0/8,127.0.0.0/8"

Sometimes set variables to **/etc/environment** not take effect. I also
write a script named my.pxy

export GIT\_PROXY\_COMMAND=/usr/bin/git-proxy

export proxyaddr=proxy-shz.intel.com

export proxyport=911

export http\_proxy="http://$proxyaddr:$proxyport"

export https\_proxy="https://$proxyaddr:$proxyport"

export ftp\_proxy="ftp://$proxyaddr:$proxyport"

export socks\_proxy="socks://$proxyaddr:$proxyport"

export
no\_proxy="localhost,\*intel.com:911,192.168.0.0/16,10.0.0.0/8,127.0.0.0/8"

export HTTP\_PROXY=$http\_proxy

export HTTPS\_PROXY=$https\_proxy

export FTP\_PROXY=$ftp\_proxy

export SOCKS\_PROXY=$socks\_proxy

export NO\_PROXY=$no\_proxy

Use command below to start this script [2]_:

$. my.pxy

Proxy urls without scheme might cause bugs; apt apps can be downloaded
and installed properly. ‘ping’ was always not available.

1) Git Proxy Command

Git need extra configuration for url with “git://” scheme. Configure
proxy command with netcat (/usr/bin/git-proxy) and add its link to the
environment (GIT\_PROXY\_COMMAND).

Create the file **/usr/bin/git-proxy**

/usr/bin/git-proxy

#!/bin/sh

case $1 in

\*.intel.com\|192.168.\*\|127.0.\*\|localhost\|10.\*)

METHOD="-X connect"

;;

\*)

METHOD="-X 5 -x proxy-socks.sc.intel.com:1080"

;;

esac

/bin/nc.openbsd $METHOD $\*

We have another choice to ‘avoid’ this issue. I found git source can be
changed in file stackrc, so we can simply change its scheme “git://” to
“http://”, because git source with http scheme is available.

1) Pip index URL

Create the file **~/.pip/pip.conf** and it also can be changed at
**/etc/pip.conf** for all users.

$mkdir ~/.pip

$ vi ~/.pip/pip.conf

[global]

default-timeout = 60

respect-virtualenv = true

build = /tmp/.pip/build

download-cache = /tmp/.pip/cache

index\_url = *http://pypi.douban.com/simple/*

[install]

use-mirrors = true

mirrors = `*http://pypi.douban.com* <http://pypi.douban.com>`__

Pip cannot browse default index url, we need to add another url to its
configuration file (~/.pip/pip.conf). douban’s source [3]_ is a choice.
But, sometimes it failed to work(might inform you that pkgs cannot find
at …/dist-packages), So I use gocept’s [4]_ as a backup. Other candidate
could be found in this website
`*http://www.pypi-mirrors.org/* <http://www.pypi-mirrors.org/>`__ , from
this site, you can see Location of Packages, Last update time, its Age,
Response Time and health Status of each available source.

1) apt configuration

create the file **/etc/apt/apt.conf**

Acquire::http::Proxy "*http://proxy-shz.intel.com:911/*\ ";

Acquire::https::Proxy "*https://proxy-shz.intel.com:911/*\ ";

Acquire::ftp::Proxy "*ftp://proxy-shz.intel.com:911/*\ ";

Acquire::socks::Proxy "*socks://proxy-shz.intel.com:911/*\ ";

Apt’s default package source is really slow, it takes bunch of time to
wait. Its source list **(/etc/apt/sources.list**) can be replaced with
our local server:

deb *http://linux-ftp.sh.intel.com/pub/mirrors/ubuntu/* trusty main
restricted universe multiverse

#deb *http://linux-ftp.sh.intel.com/pub/mirrors/ubuntu/* trusty-security
main restricted universe multiverse

deb *http://linux-ftp.sh.intel.com/pub/mirrors/ubuntu/* trusty-updates
main restricted universe multiverse

deb *http://linux-ftp.sh.intel.com/pub/mirrors/ubuntu/* trusty-proposed
main restricted universe multiverse

deb *http://linux-ftp.sh.intel.com/pub/mirrors/ubuntu/* trusty-backports
main restricted universe multiverse

deb-src *http://linux-ftp.sh.intel.com/pub/mirrors/ubuntu/* trusty main
restricted universe multiverse

deb-src *http://linux-ftp.sh.intel.com/pub/mirrors/ubuntu/*
trusty-security main restricted universe multiverse

#deb-src *http://linux-ftp.sh.intel.com/pub/mirrors/ubuntu/*
trusty-updates main restricted universe multiverse

deb-src *http://linux-ftp.sh.intel.com/pub/mirrors/ubuntu/*
trusty-proposed main restricted universe multiverse

deb-src *http://linux-ftp.sh.intel.com/pub/mirrors/ubuntu/*
trusty-backports main restricted universe multiverse

Speed is really fast, but some packages might be corrupt, and not up to
date.

Below is aliyun’s source list.

# deb cdrom:[Ubuntu 14.04.1 LTS \_Trusty Tahr\_ - Release amd64
(20140722.2)]/ trusty main restricted

# See http://help.ubuntu.com/community/UpgradeNotes for how to upgrade
to

# newer versions of the distribution.

deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted

deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted

## Major bug fix updates produced after the final release of the

## distribution.

deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted

deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the
Ubuntu

## team. Also, please note that software in universe WILL NOT receive
any

## review or updates from the Ubuntu security team.

deb http://mirrors.aliyun.com/ubuntu/ trusty universe

deb-src http://mirrors.aliyun.com/ubuntu/ trusty universe

deb http://mirrors.aliyun.com/ubuntu/ trusty-updates universe

deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates universe

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the
Ubuntu

## team, and may not be under a free licence. Please satisfy yourself as
to

## your rights to use the software. Also, please note that software in

## multiverse WILL NOT receive any review or updates from the Ubuntu

## security team.

deb http://mirrors.aliyun.com/ubuntu/ trusty multiverse

deb-src http://mirrors.aliyun.com/ubuntu/ trusty multiverse

deb http://mirrors.aliyun.com/ubuntu/ trusty-updates multiverse

deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates multiverse

## N.B. software from this repository may not have been tested as

## extensively as that contained in the main release, although it
includes

## newer versions of some applications which may provide useful
features.

## Also, please note that software in backports WILL NOT receive any
review

## or updates from the Ubuntu security team.

deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted
universe multiverse

deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main
restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted

deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main
restricted

deb http://mirrors.aliyun.com/ubuntu/ trusty-security universe

deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security universe

deb http://mirrors.aliyun.com/ubuntu/ trusty-security multiverse

deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security multiverse

## Uncomment the following two lines to add software from Canonical's

## 'partner' repository.

## This software is not part of Ubuntu, but is offered by Canonical and
the

## respective vendors as a service to Ubuntu users.

# deb http://archive.canonical.com/ubuntu trusty partner

# deb-src http://archive.canonical.com/ubuntu trusty partner

## This software is not part of Ubuntu, but is offered by third-party

## developers who want to ship their latest software.

deb http://extras.ubuntu.com/ubuntu trusty main

deb-src http://extras.ubuntu.com/ubuntu trusty main

|image1|

\ *DevStack Configuration*

It takes some time to realize that official tutorial [5]_ is not
explicit enough to deploy OpenStack, so I took a sample from
**devstack/samples/local.conf**, apparently this configuration works
better. So I use this tutorial as a reference to modify local.conf. And
I also referred from some other tutorials [6]_.

1. Preparation

Add third party repositories (EPEL, rpmforge, atomic, PUIAS) for
CentOS6.5

1. Install priority plugin

    # yum install yum-priorities

1. Download EPEL (Extended Packages for Enterprise Linux), RPMforge
       installing package, then install it

# wget
http://mirrors.ustc.edu.cn/fedora/epel/6/x86\_64/epel-release-6-8.noarch.rpm

# wget http://rpms.famillecollet.com/enterprise/remi-release-6.rpm

# wget
http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el6.rf.x86\_64.rpm

# rpm –ivh epel-release-6-8.noarch.rpm

# rpm –ivh remi-release-6.rpm

# rpm –ivh rpmforge-release-0.5.3-1.el6.rf.x86\_64.rpm

1. Check whether repo was installed like this

    # rpm -q epel-release

1. Import gpg key for epel & rpmforge

    # rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6

    # rpm --import http://apt.sw.be/RPM-GPG-KEY.dag.txt

1. Create PUIAS computational repository manually( gpgcheck should be
       disabled since gpgkey is not available)

    [PUIAS\_6\_computational]

    name=PUIAS computational Base $releasever - $basearch

    mirrorlist=http://puias.math.ias.edu/data/puias/computational/$releasever/$basearch/mirrorlist

    #baseurl=http://puias.math.ias.edu/data/puias/computational/$releasever/$basearch

    gpgcheck=0

    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-puias

1. By the way, package python-mox still can’t be found in any
       repository, so we need to install it manually.

    $ wget
    ftp://ftp.is.co.za/mirror/fedora.redhat.com/epel/6/ppc64/python-mox-0.5.3-2.el6.noarch.rpm

    $ rpm –ivh python-mox-0.5.3-2.el6.noarch.rpm

1. On the other side, mariadb-server conlicts with mysql-lib while
       installing it. We can solve this problem by removing mysql-lib’s
       dependency, which is dangerous. And Django conflicts with
       python-django.

    # rpm -e --nodeps mysql-libs

    # rpm -e --nodeps python-django

Upgrade python 2.6 to 2.7 for CentOS6.5

Add the DevStack User

Openstack runs as a non-root user that has sudo access to root. Every
node must use the same name and preferably uid.

# groupadd stack

# useradd -g stack -s /bin/bash -d /opt/stack -m stack

# echo "stack ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

Install NTP [7]_, change time zone into shanghai.

# atp-get install ntp

# ln -sf /usr/share/zoneinfo/posix/Asia/Shanghai/ etc/localtime

a. Controller node

Add to ctrl node’s **/etc/ntp.conf**

server 210.72.145.44 #Authorized Center in China

server 10.239.44.241

server 10.239.3.193

server 0.ubuntu.pool.ntp.org

server 1.ubuntu.pool.ntp.org

server 2.ubuntu.pool.ntp.org

server 3.ubuntu.pool.ntp.org

server 3.asia.pool.ntp.org

server 0.asia.pool.ntp.org

server 2.cn.pool.ntp.org

server 192.168.2.200 #Servers above is not accessible inside intel

server 127.127.1.0 #Hardware clock

fudge 127.127.1.0 stratum 10

a. Other nodes

Delete another time servers and add the following document to other
nodes’ **/etc/ntp.conf**

server 192.168.11.66 #delete all other servers. Set your local
ntp-server’s IP

a. Verify operation

Run these two commands to check NTP service’s status in all nodes:

# ntpq –c peers

remote refid st t when poll reach delay offset jitter

=============================================================================

\*192.168.11.66 LOCAL(0) 11 u 731 1024 377 0.248 0.045 0.023

Contents in remote column indicate hostname or IP address.

# ntpq –c assoc

ind assid status conf reach auth condition last\_event cnt

===========================================================

1 25916 965a yes yes none sys.peer sys\_peer 5

Content in the condition column should indicate sys.peer .

ssh login without password

It doesn’t work by simply copying rsa keys based on my experience, I
tried to solve this issue by changing its mod to 600, as some article
says [8]_. After reading ssh manual, finally the problem was solved with
this simple command below. [9]_

Create rsa key:

$ ssh-keygen -t rsa -P ''

Authorization:

$ssh-copy-id -i ~/.ssh/id\_rsa.pub stack@192.168.11.68

1. Fire up DevStack

Download DevStack

Clone devstack from its official repository. Also, you can get from
github [10]_ .

$ git clone https://git.openstack.org/openstack-dev/devstack

stack.sh [11]_

Load localrc before stackrc; before localrc loaded, ENABLED\_SERVICE is
not null, it contains all of the main services.

stackrc [12]_

stackrc is the primary configuration file for DevStack. It contains all
of the settings that control the services started and the repositories
used to download the source for those services. stackrc sources the
localrc section of local.conf to perform the default overrides.

DATABASE\_TYPE: Select the database backend to use. The default is
mysql, postgresql is also available

ENABLED\_SERVICES: Specify which services to launch. Below are its
default values.

ENABLED\_SERVICES=g-api,g-reg,key,n-api,n-crt,n-obj,n-cpu,n-net,n-cond,c-sch,c-api,c-vol,n-sch,n-cauth,horizon,rabbit,tempest,$DATABASE\_TYPE

Service Repos can be overridden in local.conf

GIT\_BASE=git://github.com/ #scheme http:// is supported

NOVA\_REPO=$GIT\_BASE/openstack/nova.git

NOVA\_BRANCH=master

Configure local.conf [13]_

This gives it the ability to override any variables set in
\`\`stackrc\`\`. Also, most of the settings in \`\`stack.sh\`\` are
written to only be set if no value has already been set; this lets
\`\`local.conf\`\` effectively override the default values.

Took sample from **devstack/samples/**

$cp samples/localrc ./

$vi localrc

And you can also get our configuration samples:

$ git clone git@github.com:poppyqi/devstack-multinode-nova-network.git

Minimal configuration

[[local\|localrc]]

FLOATING\_RANGE=192.168.11.224/27

FIXED\_RANGE=10.11.12.0/24

FIXED\_NETWORK\_SIZE=256

FLAT\_INTERFACE=eth0

ADMIN\_PASSWORD=123456

MYSQL\_PASSWORD=$ADMIN\_PASSWORD

RABBIT\_PASSWORD=$ADMIN\_PASSWORD

SERVICE\_PASSWORD=$ADMIN\_PASSWORD

The following list shows some of OpenStack’s service options.

# glance-Image service

g-api\ **,**\ g-reg

# keystone service

Key

# Nova-compute Service

n-api\ **,**\ n-crt\ **,**\ n-obj\ **,**\ n-cpu\ **,**\ n-cond\ **,**\ n-sch

# Nova-network Service

n-net

# vnc

n-novnc\ **,**\ n-xvnc\ **,**\ n-cauth

# heat

h-eng\ **,**\ h-api\ **,**\ h-api-cfn\ **,**\ h-api-cw

# dashboard

horizon

# additional services

rabbit\ **,**\ tempest\ **,**\ mysql

# Swift - Object Storage

s-proxy,s-object,s-container,s-account

# Neutron - Networking Service

# If Neutron is not declared the old good nova-network will be used

q-svc,q-agt,q-dhcp,q-l3,q-meta,neutron

## Neutron - Load Balancing

q-lbaas

## Neutron - VPN as a Service

q-vpn

## Neutron - Firewall as a Service

q-fwaas

# VLAN configuration

#Q\_PLUGIN=ml2

#ENABLE\_TENANT\_VLANS=True

# GRE tunnel configuration

Q\_PLUGIN=ml2

ENABLE\_TENANT\_TUNNELS=True

# VXLAN tunnel configuration

#Q\_PLUGIN=ml2

#Q\_ML2\_TENANT\_NETWORK\_TYPE=vxlan

# Cinder - Block Device Service

VOLUME\_GROUP="cinder-volumes"

cinder,c-api,c-vol,c-sch,c-bak

# Heat - Orchestration Service

heat,h-api,h-api-cfn,h-api-cw,h-eng

#IMAGE\_URLS+=",http://fedorapeople.org/groups/heat/prebuilt-jeos-images/F17-x86\_64-cfntools.qcow2"

# Ceilometer - Metering Service (metering + alarming)

ENABLED\_SERVICES+=,ceilometer-acompute,ceilometer-acentral,ceilometer-collector,ceilometer-api

ENABLED\_SERVICES+=,ceilometer-alarm-notify,ceilometer-alarm-eval

ENABLED\_SERVICES+=,trove,tr-api,tr-tmgr,tr-cond

# Sahara - Enable auto assignment of floating IPs. By default Sahara
expects this setting to be enabled

EXTRA\_OPTS=(auto\_assign\_floating\_ip=True)

ENABLED\_SERVICES+=,sahara

Services can be added, or disabled like this:

ENABLED\_SERVICES+=,new\_service #change variable

enable\_service service\_name

disable\_service service\_name

disable\_all\_services

Some common configuration variables:

#Set \`\`OFFLINE\`\` to \`\`True\`\` to configure \`\`stack.sh\`\` to
run cleanly without Internet access. \`\`stack.sh\`\` must have been
previously run with Internet access to install prerequisites and fetch
repositories.

OFFLINE=True

#Installation Directory default value is /opt/stack

DESK=/opt/stack

#Enable Logging

LOG\_COLOR=False #defaut: True

LOGDAYS=2 #defaut: 7

LOGFILE=$DEST/logs/stack.sh.log #old log files are cleaned automatically

SCREEN\_LOGDIR=$DEST/logs/screen

#Enabling Syslog

SYSLOG=True #default: False

SYSLOG\_HOST=$HOST\_IP

SYSLOG\_PORT=516

#Reclone every time

RECLONE=yes #default: “”

#Service Catalog Backend

KEYSTONE\_CATALOG\_BACKEND=template #default: sql

# Apache fronted for WSGI

APACHE\_ENABLED\_SERVICES+=keystone,swift

#APACHE\_ENABLED\_SERVICES+=keystone

# MultiNode

#master node

MULTI\_HOST=True

#slave node

MYSQL\_HOST=w.x.y.z

RABBIT\_HOST=w.x.y.z

GLANCE\_HOSTPORT=w.x.y.z:9292

If the installation is successful, you can see:

Controller node

Horizon is now available at http://192.168.11.66/

Keystone is serving at http://192.168.11.66:5000/v2.0/

Examples on using novaclient command line is in exercise.sh

The default users are: admin and demo

The password: 123456

This is your host ip: 192.168.11.66

Compute node

Keystone is serving at http://192.168.11.66:5000/v2.0/

Examples on using nova client command line is in exercise.sh

The default users are: admin and demo

The password: 123456

This is your host ip: 192.168.11.68

After installation, in order to access the dashboard, use plink.exe to
create a tunnel with the following command:

plink.exe -N -D 127.0.0.1:1080 root@10.239.44.197 -pw intel@123

|image2|

Then you can use 127.0.0.1 as a SOCKS Host.

|image3|

To work via the CLI

Start by getting admin creds.

$ source /opt/stack/python-novaclient/tools/nova.bash\_completion

$ source openrc admin admin # source openrc [username] [tenantname]

$ nova image-list

+--------------------------------------+---------------------------------+--------+--------+

\| ID \| Name \| Status \| Server \|

+--------------------------------------+---------------------------------+--------+--------+

\| fc516707-164b-404c-9576-420542012824 \|
Fedora-x86\_64-20-20140618-sda \| ACTIVE \| \|

\| 1d80bb04-480e-48ce-988e-b83bc551bd76 \| cirros-0.3.2-x86\_64-uec \|
ACTIVE \| \|

\| 88e9eac3-9fa2-42c9-a9f3-3c1523cf4d1f \|
cirros-0.3.2-x86\_64-uec-kernel \| ACTIVE \| \|

\| cab81836-ea3f-426a-a661-d5e6f4332245 \|
cirros-0.3.2-x86\_64-uec-ramdisk \| ACTIVE \| \|

+--------------------------------------+---------------------------------+--------+--------+

$ nova list

+--------------------------------------+------------------------------------------+--------+------------+-------------+--------------------+

\| ID \| Name \| Status \| Task State \| Power State \| Networks \|

+--------------------------------------+------------------------------------------+--------+------------+-------------+--------------------+

\| 604830c1-d005-437a-bcb3-c66d0311e8d3 \|
ttt-604830c1-d005-437a-bcb3-c66d0311e8d3 \| ACTIVE \| - \| Running \|
private=10.4.128.2 \|

+--------------------------------------+------------------------------------------+--------+------------+-------------+--------------------+

$ nova get-vnc-console 604830c1-d005-437a-bcb3-c66d0311e8d3 novnc

+-------+------------------------------------------------------------------------------------+

\| Type \| Url \|

+-------+------------------------------------------------------------------------------------+

\| novnc \|
http://192.168.11.71:6080/vnc\_auto.html?token=c327f2f8-077d-41d6-abdb-c7f32e23a095
\|

+-------+------------------------------------------------------------------------------------+

$ keystone service-list

+----------------------------------+----------+----------------+-----------------------------+

\| id \| name \| type \| description \|

+----------------------------------+----------+----------------+-----------------------------+

\| 1bd206f9e464425d929a64f0ba531010 \| cinder \| volume \| Cinder Volume
Service \|

\| dd42b0dbb9df4177ba17fefb3e40f5b4 \| cinderv2 \| volumev2 \| Cinder
Volume Service V2 \|

\| 4236a2d5567743d4b56904750568b485 \| ec2 \| ec2 \| EC2 Compatibility
Layer \|

\| bb4df826f91d49e1ba80fe871f7eb8bf \| glance \| image \| Glance Image
Service \|

\| 715bd7975203409b98d62254a1acd841 \| heat \| orchestration \| Heat
Orchestration Service \|

\| 2745721026403dad820fae659aa1a0 \| heat-cfn \| cloudformation \| Heat
CloudFormation Service \|

\| f4fa0e6e7a5749b89b65e38a4cfd7752 \| keystone \| identity \| Keystone
Identity Service \|

\| 9b7e54f73ff24b838d5958c06be0bf1f \| nova \| compute \| Nova Compute
Service \|

\| 8a1c5c61f986426093feb175083dc3b5 \| novav21 \| computev21 \| Nova
Compute Service V2.1 \|

\| c9b19b20ecb34eca879e80e105777d5f \| s3 \| s3 \| S3 \|

\| 356268b0abee42838e5ff8353d254d7f \| swift \| object-store \| Swift
Service \|

+----------------------------------+----------+----------------+-----------------------------+
1.

nova-manage service list # Check Nova service status

Binary Host Zone Status State Updated\_At

nova-cert control internal enabled :-) 2014-12-06 02:29:44

nova-conductor control internal enabled :-) 2014-12-06 02:29:42

nova-consoleauth control internal enabled :-) 2014-12-06 02:29:44

nova-scheduler control internal enabled :-) 2014-12-06 02:29:47

nova-compute node-01 nova enabled :-) 2014-12-06 02:29:46

nova-compute node-02 nova enabled :-) 2014-12-06 02:29:46

nova-compute node-03 nova enabled :-) 2014-04-06 02:29:42

#EC2 credentials

$. eucarc

\ *Tips*

1) Tool screen can create screens; each screen might have lots of
       windows.

Short-cut keys: “ctrl + a” as initial

+------------+----------------------------------------------------------------------------+
| Key        | Function                                                                   |
+------------+----------------------------------------------------------------------------+
| d          | detach screen                                                              |
+------------+----------------------------------------------------------------------------+
| c/n/p/k    | create, next, previous, kill window                                        |
+------------+----------------------------------------------------------------------------+
| “          | Select window from list                                                    |
+------------+----------------------------------------------------------------------------+
| Ctrl + a   | Previous window viewed                                                     |
+------------+----------------------------------------------------------------------------+
| [          | Edit mode, press space bar to start select, press again to complete copy   |
+------------+----------------------------------------------------------------------------+
| ]          | paste                                                                      |
+------------+----------------------------------------------------------------------------+
| ?          | help                                                                       |
+------------+----------------------------------------------------------------------------+

Recommended screenrc configuration:

1) Hostname

Name of current working computer can be saved in **/etc/hostname**. And
you can store other computer’s name in **/etc/hosts**.

1) Reset the bridge

$ sudo brctl delif br100 eth0.926

$ sudo ip link set dev br100 down

$ sudo brctl delbr br100

1)  Logs

Logs all stored at **$DEST/logs/**

/opt/stack/logs/stack.sh.log

/opt/stack/logs/screen-c-api.log

/opt/stack/logs/screen-c-sch.log

/opt/stack/logs/screen-c-vol.log

/opt/stack/logs/screen-g-api.log

/opt/stack/logs/screen-g-reg.log

/opt/stack/logs/screen-h-api-cfn.log

/opt/stack/logs/screen-h-api-cw.log

/opt/stack/logs/screen-h-api.log

/opt/stack/logs/screen-h-eng.log

/opt/stack/logs/screen-horizon.log

/opt/stack/logs/screen-key-access.log

/opt/stack/logs/screen-key.log

/opt/stack/logs/screen-n-api.log

/opt/stack/logs/screen-n-cauth.log

/opt/stack/logs/screen-n-cond.log

/opt/stack/logs/screen-n-cpu.log

/opt/stack/logs/screen-n-crt.log

/opt/stack/logs/screen-n-net.log

/opt/stack/logs/screen-n-novnc.log

/opt/stack/logs/screen-n-obj.log

/opt/stack/logs/screen-n-sch.log

/opt/stack/logs/screen-n-xvnc.log

/opt/stack/logs/screen-s-account.log

/opt/stack/logs/screen-sahara.log

/opt/stack/logs/screen-s-container.log

/opt/stack/logs/screen-s-object.log

/opt/stack/logs/screen-s-proxy.log

1) config files

/etc/apache2/apache2.conf

/etc/apache2/ports.conf

/etc/apt/apt.conf

/etc/cinder/cinder.conf

/etc/cinder/rootwrap.conf

/etc/dhcp/dhclient.conf

/etc/glance/glance-api.conf

/etc/glance/glance-cache.conf

/etc/glance/glance-registry.conf

/etc/heat/heat.conf

/etc/iscsi/iscsid.conf

/etc/keystone/keystone.conf

/etc/libvirt/libvirt.conf

/etc/libvirt/libvirtd.conf

/etc/libvirt/lxc.conf

/etc/libvirt/qemu.conf

/etc/libvirt/qemu-lockd.conf

/etc/libvirt/virtlockd.conf

/etc/libvirt/virt-login-shell.conf

/etc/nova/nova.conf

/etc/nova/rootwrap.conf

/etc/qemu/target-x86\_64.conf

/etc/sahara/sahara.conf

/etc/swift/container-sync-realms.conf

/etc/swift/proxy-server.conf

/etc/swift/swift.conf

/etc/swift/test.conf

/etc/tgt/targets.conf

/etc/ufw/sysctl.conf

/etc/ufw/ufw.conf

/opt/stack/cinder/openstack-common.conf

/opt/stack/devstack/local.conf

/opt/stack/glance/openstack-common.conf

/opt/stack/heat/openstack-common.conf

/opt/stack/horizon/openstack-common.conf

/opt/stack/keystone/openstack-common.conf

/opt/stack/nova/openstack-common.conf

/opt/stack/sahara/openstack-common.conf

/opt/stack/tempest/openstack-common.conf

/opt/stack/horizon/openstack\_dashboard/conf

/opt/stack/horizon/horizon/test/settings.py

/opt/stack/horizon/openstack\_dashboard/settings.py

/opt/stack/horizon/openstack\_dashboard/enabled/\_30\_settings.py

/opt/stack/horizon/openstack\_dashboard/local/local\_settings.py

/opt/stack/horizon/openstack\_dashboard/test/settings.py

/opt/stack/horizon/openstack\_dashboard/test/settings.pyc

/opt/stack/horizon/openstack\_dashboard/test/integration\_tests/tests/test\_user\_settings.py

/opt/stack/horizon/openstack\_dashboard/utils/settings.py

Eg: sahara’s proxy command can be added at **/etc/sahara/sahara.conf**

$ vi /etc/sahara/sahara.conf

1) Sahara plugins

**Vanilla Plugin **

image list

http://sahara-files.mirantis.com/sahara-juno-vanilla-1.2.1-ubuntu-14.04.qcow2

http://sahara-files.mirantis.com/sahara-juno-vanilla-1.2.1-centos-6.5.qcow2

http://sahara-files.mirantis.com/sahara-juno-vanilla-1.2.1-fedora-20.qcow2

http://sahara-files.mirantis.com/sahara-juno-vanilla-2.4.1-ubuntu-14.04.qcow2

http://sahara-files.mirantis.com/sahara-juno-vanilla-2.4.1-centos-6.5.qcow2

http://sahara-files.mirantis.com/sahara-juno-vanilla-2.4.1-fedora-20.qcow2

Default usernames:

OS username

Ubuntu 14.04 ubuntu

Fedora 20 fedora

CentOS 6.5 cloud-user

**Hortonworks Data Platform** (username: cloud-user)

http://sahara-files.mirantis.com/sahara-juno-hdp-1.3.2-centos-6.5.qcow2

http://sahara-files.mirantis.com/sahara-juno-hdp-2.0.6-centos-6.5.qcow2

http://sahara-files.mirantis.com/sahara-juno-hdp-plain-centos-6.5.qcow2

**Cloudera**

It is not enabled in sahara by default. To enable it you should manually
modify the Sahara configuration file (default
**/etc/sahara/sahara.conf**) to add “cdh” in “plugins” value. [14]_

plugins=cdh,vanilla,hdp,fake

To use the cloudera plugin, you should have cm\_api (version >=8.0.0)
installed on the server where Sahara is running. To install cm\_api,
simply use pip:

$ sudo pip install cm\_api

$ sudo /etc/init.d/memcached restart

7) Multi-Node swift configuration

By default, devstack didn’t support the installation of multi-node
swift. We need to install and configure swift to storage node manually
or write code into local.sh file to realize it.

At controller node, we need to configure rings. Run following script in
directory **/etc/swift**.

#!/bin/bash

rm -f \*.builder \*.ring.gz backups/\*.builder backups/\*.ring.gz

$SLAVES="192.168.11.65 192.168.11.67 192.168.11.68 192.168.11.69"
#change them to your storage node’s IP

for i in object container account; do

swift-ring-builder ${i}.builder create 10 3 1

done

for j in SLAVES;do

swift-ring-builder object.builder add r1z1-${j}:6013/sdb1 100

done

for j in SLAVES;do

swift-ring-builder account.builder add r1z1-${j}:6012/sdb1 100

done

for j in SLAVES;do

swift-ring-builder container.builder add r1z1-${j}:6011/sdb1 100

done

for i in object container account; do

swift-ring-builder ${i}.builder rebalance

done

for j in SLAVES;do

scp \*.gz stack@$j:/ect/swift

done

sudo /etc/init.d/rsync restart

sudo swift-init all restart

At storage node, we need to create a file named local.sh in
/opt/stack/devstack

#!/usr/bin/env bash

umask 022

PATH=$PATH:/usr/local/sbin:/usr/sbin:/sbin

FILES=/opt/stack/devstack/files

DEST=${DEST:-/opt/stack}

TOP\_DIR=$(cd $(dirname "$0") && pwd)

SWIFT\_HASH=66a3d6b56c1f479c8b4e70ab5c2000f5

source $TOP\_DIR/functions

source $TOP\_DIR/lib/config

source $TOP\_DIR/stackrc

source $TOP\_DIR/lib/database

source $TOP\_DIR/lib/rpc\_backend

source $TOP\_DIR/lib/apache

source $TOP\_DIR/lib/tls

source $TOP\_DIR/lib/infra

source $TOP\_DIR/lib/oslo

source $TOP\_DIR/lib/stackforge

source $TOP\_DIR/lib/horizon

source $TOP\_DIR/lib/keystone

source $TOP\_DIR/lib/glance

source $TOP\_DIR/lib/nova

source $TOP\_DIR/lib/cinder

source $TOP\_DIR/lib/swift

source $TOP\_DIR/lib/ceilometer

source $TOP\_DIR/lib/heat

source $TOP\_DIR/lib/neutron

source $TOP\_DIR/lib/ldap

source $TOP\_DIR/lib/dstat

source $TOP\_DIR/openrc admin admin

cleanup\_swift

install\_swift

configure\_swift

create\_swift\_disk

sudo /etc/init.d/rsync restart

sudo swift-init all restart

8) Debugging Neutron issues [15]_

1. show devices

**ip a** shows status of all physical and virtual devices

**ovs-vsctl** **show** shows interfaces and bridges in the virtual
switch

**ovs-dpctl** **show** shows datapaths on the switch

2. tracking packets

**tcpdump -n -i <interface> -w <filename>** dump traffic on a network

**iptables -L** check iptables rules

3. network namespaces

Network namespaces allow VLANs to share overlapping address space –
important for bigger deployments, and to provide multi-tenant networks

**ip netns list** lists all known network namespaces

**ip netns exec <namespace id> route –n** Shows routing table inside
specific namespace

Execute arbitrary commands (incl. ssh, ping)

4. DHCP

**Scenario: Instance is not getting IP address**

i. **nova console-log <instance name>** DHCP request sent, no reply
received

ii. Verify neutron-dhcp-agent is running: **ps aux \| grep -i dhcp**

iii. Check host logs (/opt/stack/logs/screen/screen-horizon.log)

iv. If host is not seeing DHCP traffic: **tcpdump -i all \| grep -i
dhcp**

5. Access/routing

Scenario: I can't SSH into an instance

i. Security groups: port 22 TCP & all ICMP allowed?

ii. Is floating IP address routable from client?

**route -n** on client\ **,** verify that public subnet in OpenStack is
accessible from client (eg. for local LAN, that it matches
192.168.0.0/24)

iii. Bridges OK?

**ovs-vsctl show** is ethernet card attached to same bridge as public
network?

**neutron router show router1** are the private subnet and public subnet
connected to the router?

**ip netns exec <public namespace id> ping <floating IP>** does the
public network match the local LAN exactly?

**ip netns exec <private namespace id> route –n** is traffic being
correctly routed from the instance out?

iv. mtu size

**ping <ip>** by default, packet size is 84 bytes.

# ping 10.11.12.34

PING 10.11.12.34 (10.11.12.34) 56(84) bytes of data.

64 bytes from 10.11.12.34: icmp\_seq=1 ttl=63 time=0.592 ms

64 bytes from 10.11.12.34: icmp\_seq=2 ttl=63 time=0.519 ms

64 bytes from 10.11.12.34: icmp\_seq=3 ttl=63 time=0.468 ms

Using argument –s to designate package size, to find out the maximum mtu
size of network.

Then change dhcp\_agent’s setting, by modifying
**/etc/neutron/dnsmasq-neutron.conf**

dnsmasq\_conf\_file = /etc/neutron/dnsmasq-neutron.conf

add dhcp force option to **/etc/neutron/dnsmasq-neutron.conf**

dhcp-option-force=26,1400

after configuration, restart the dhcp-agent service

$service neutron-dhcp-agent restart #restart dhcp agent service

\ *Troubleshooting*

Some issue can be solved by reading doc from SharePoint [16]_.

1. Pip issues

i. pip installation issue

+ install\_get\_pip

+ [[ ! -r /opt/devstack/files/get-pip.py ]]

+ sudo -E python /opt/devstack/files/get-pip.py

Cannot fetch index base URL https://pypi.python.org/simple/

Could not find any downloads that satisfy the requirement pip in
/usr/local/lib/python2.7/dist-packages

Downloading/unpacking pip

Cleaning up...

No distributions at all found for pip in
/usr/local/lib/python2.7/dist-packages

Storing debug log for failure in /opt/stack/.pip/pip.log

++ err\_trap

++ local r=1

++ set +o xtrace

stack.sh failed

Error on exit

World dumping... see ./worlddump-2014-12-04-071633.txt for details

Change pip source by editing **stack.sh** at line 703.

if [[ "$OFFLINE" != "True" ]]; then

PYPI\_ALTERNATIVE\_URL=$PYPI\_ALTERNATIVE\_URL
$TOP\_DIR/tools/install\_pip.sh

fi

ii. Index url issue

2014-12-10 14:38:43.222 \| Cannot fetch index base URL
http://pypi.douban.com/simple/

2014-12-10 14:38:43.222 \| http://pypi.douban.com/simple/pip/ uses an
insecure transport scheme (http). Consider using https if
pypi.douban.com has it available

2014-12-10 14:38:43.222 \| http://pypi.douban.com/pip/ uses an insecure
transport scheme (http). Consider using https if pypi.douban.com has it
available

2014-12-10 14:40:45.586 \| Could not find any downloads that satisfy the
requirement pip in /usr/local/lib/python2.7/dist-packages

2014-12-10 14:40:45.586 \| Downloading/unpacking pip

2014-12-10 14:40:45.586 \| Cleaning up...

2014-12-10 14:40:45.586 \| No distributions at all found for pip in
/usr/local/lib/python2.7/dist-packages

Perhaps the server is down, change index\_base\_URL into
`*http://pypi.gocept.com/simple/* <http://pypi.gocept.com/simple/>`__ to
solve the issue.

$mkdir ~/.pip

$ vi ~/.pip/pip.conf

change douban into gocept gloably.

:%s#douban#gocept#g

:x

If it still doesn’t work, it might be caused by proxy server’s
connectivity.

iii. AssertionError: Multiple .dist-info directories

2014-12-15 03:46:28.420 \| Installing collected packages: setuptools

2014-12-15 03:46:28.427 \| Found existing installation: setuptools 7.0

2014-12-15 03:46:28.431 \| Uninstalling setuptools:

2014-12-15 03:46:28.436 \| Successfully uninstalled setuptools

2014-12-15 03:46:28.505 \| Rolling back uninstall of setuptools

2014-12-15 03:46:28.508 \| Cleaning up...

2014-12-15 03:46:28.508 \| Exception:

2014-12-15 03:46:28.508 \| Traceback (most recent call last):

2014-12-15 03:46:28.508 \| File
"/usr/local/lib/python2.7/dist-packages/pip/basecommand.py", line 122,
in main

2014-12-15 03:46:28.508 \| status = self.run(options, args)

2014-12-15 03:46:28.508 \| File
"/usr/local/lib/python2.7/dist-packages/pip/commands/install.py", line
283, in run

2014-12-15 03:46:28.508 \| requirement\_set.install(install\_options,
global\_options, root=options.root\_path)

2014-12-15 03:46:28.508 \| File
"/usr/local/lib/python2.7/dist-packages/pip/req.py", line 1435, in
install

2014-12-15 03:46:28.508 \| requirement.install(install\_options,
global\_options, \*args, \*\*kwargs)

2014-12-15 03:46:28.508 \| File
"/usr/local/lib/python2.7/dist-packages/pip/req.py", line 671, in
install

2014-12-15 03:46:28.508 \| self.move\_wheel\_files(self.source\_dir,
root=root)

2014-12-15 03:46:28.508 \| File
"/usr/local/lib/python2.7/dist-packages/pip/req.py", line 901, in
move\_wheel\_files

2014-12-15 03:46:28.508 \| pycompile=self.pycompile,

2014-12-15 03:46:28.508 \| File
"/usr/local/lib/python2.7/dist-packages/pip/wheel.py", line 215, in
move\_wheel\_files

2014-12-15 03:46:28.508 \| clobber(source, lib\_dir, True)

2014-12-15 03:46:28.508 \| File
"/usr/local/lib/python2.7/dist-packages/pip/wheel.py", line 193, in
clobber

2014-12-15 03:46:28.508 \| assert not info\_dir, 'Multiple .dist-info
directories'

Solution:

$ rm –rf /usr/local/lib/python2.7/dist-packages

$ sudo init 6

iv. pkg\_resources.DistributionNotFound: pip==1.5.6

2014-12-29 08:20:40.632 \| + pip\_install -U setuptools

2014-12-29 08:20:40.635 \| + sudo -H PIP\_DOWNLOAD\_CACHE=/var/cache/pip
http\_proxy=http://proxy-shz.intel.com:911
https\_proxy=https://proxy-shz.intel.com:911
'no\_proxy=localhost,\*intel.com:911,192.168.0.0/16,10.0.0.0/8,127.0.0.0/8'
/usr/local/bin/pip install -U setuptools

2014-12-29 08:20:40.686 \| Traceback (most recent call last):

2014-12-29 08:20:40.686 \| File "/usr/local/bin/pip", line 5, in
<module>

2014-12-29 08:20:40.686 \| from pkg\_resources import load\_entry\_point

2014-12-29 08:20:40.686 \| File
"/usr/local/lib/python2.7/dist-packages/pkg\_resources/\_\_init\_\_.py",
line 2956, in <module>

2014-12-29 08:20:40.686 \| working\_set = WorkingSet.\_build\_master()

2014-12-29 08:20:40.686 \| File
"/usr/local/lib/python2.7/dist-packages/pkg\_resources/\_\_init\_\_.py",
line 568, in \_build\_master

2014-12-29 08:20:40.686 \| return
cls.\_build\_from\_requirements(\_\_requires\_\_)

2014-12-29 08:20:40.686 \| File
"/usr/local/lib/python2.7/dist-packages/pkg\_resources/\_\_init\_\_.py",
line 581, in \_build\_from\_requirements

2014-12-29 08:20:40.686 \| dists = ws.resolve(reqs, Environment())

2014-12-29 08:20:40.686 \| File
"/usr/local/lib/python2.7/dist-packages/pkg\_resources/\_\_init\_\_.py",
line 760, in resolve

2014-12-29 08:20:40.686 \| raise DistributionNotFound(req)

2014-12-29 08:20:40.687 \| pkg\_resources.DistributionNotFound:
pip==1.5.6

$ sudo rm /usr/local/bin/pip

$ sudo rm /usr/local/lib/python2.7/dist-packages/pip\* -rf

And comment the install\_pip command in stack.sh

Then manually install the pip

$ sudo apt-get install python-pip

If not work, try this to fix DistributionNotFound error:

$ sudo –E easy\_install --upgrade pip

1. Screen issue

i. screen cannot open

Cannot open your terminal '/dev/pts/0' - please check.

Solve this issue by changing its owner:

$ sudo chown stack:stack /dev/pts/0

1. olso issue

i. pkg\_resources.VersionConflict

2014-12-13 21:18:01.099 \| raise VersionConflict(tmpl % args)

2014-12-13 21:18:01.099 \| pkg\_resources.VersionConflict: SQLAlchemy
0.8.4 is installed but SQLAlchemy<=0.8.99,<=0.9.99,>=0.8.4,>=0.9.7 is
required by ['ceilometer']

Solution:

$ sudo pip uninstall oslo.db

$ sudo pip install oslo.db

Ii. Can’t import packages

$ sudo apt-get remove oslo.config oslo.rootwrap

$ sudo apt-get install oslo.config oslo.rootwrap

1. Dashboard issues

i. authorization error

Unauthorized at /admin/

Unauthorized (HTTP 401) (Request-ID:
req-a7ef8ee1-3ce6-4082-b91b-4876208164c6)

This error occurs when adding new node to controller node. Clearing web
browser’s cookie can solve this problem.

ii. Authentication failure when login dashboard

After restarting the machine, an error occurs when you login dashboard:

“An error occurred authenticating. Please try again later”

Solution:

$cd /devstack && sh rejoin-stack.sh

iii. apache2: Could not determine the server's fully qualified domain
name

$ echo "ServerName localhost" \| sudo tee
/etc/apache2/conf-available/fqdn.conf

$ sudo a2enconf fqdn

1. Python issue

i. ImportError: No module named MySQLdb

$ sudo apt-get install python-mysqldb

ii. ImportError: No module named libvirt

$ sudo apt-get remove python-libvirt

$ sudo apt-get install python-libvirt

iii. attribute cannot be found.

Traceback (most recent call last):

File "/usr/local/bin/neutron-openvswitch-agent", line 6, in <module>

from neutron.plugins.openvswitch.agent.ovs\_neutron\_agent import main

File
"/opt/stack/neutron/neutron/plugins/openvswitch/agent/ovs\_neutron\_agent.py",
line 53, in <module>

cfg.CONF.import\_group('AGENT',
'neutron.plugins.openvswitch.common.config')

File "/usr/lib/python2.7/dist-packages/oslo/config/cfg.py", line 1810,
in import\_group

\_\_import\_\_(module\_str)

File "/opt/stack/neutron/neutron/plugins/openvswitch/common/config.py",
line 38, in <module>

cfg.IPOpt('local\_ip', version=4,

AttributeError: 'module' object has no attribute 'IPOpt'

Open file
"/opt/stack/neutron/neutron/plugins/openvswitch/common/config.py", we
can easily find that cfg is a component of oslo.config.

from oslo.config import cfg

Apparently, this issue caused by oslo.config’s integrity.

$ sudo apt-get remove python-oslo.config

$ sudo apt-get install python-oslo.config

1. Rabbit issues

i. Error: unable to connect to node rabbit@upstream: nodedown

$ sudo apt-get remove rabbit-server

$ sudo apt-get install rabbit-server

ii. Failed to set rabbitmq password

$sudo service rabbit-server restart

iii. Failed to start rabbitmq-server

Check the log file at **/var/log/rabbitmq/startup\_log**

If error type is “eaddrinuse”, which mean the listen port had been in
use. We can change parameters in /etc/rabbitmq/rabbitmq-env.conf , below
are it’s default values:

NODENAME=rabbit

NODE\_PORT=5632

$sudo service rabbit-server restart

1. MySQL issue

i. ERROR 2003 (HY000): Can't connect to MySQL server on '127.0.0.1'
(111)

$sudo apt-get remove mysql-server mysql-common

$sudo /etc/init.d/mysql restart

1. Cinder issue

i. auto configuration is incorrect.

Edit **/etc/cinder/cinder.conf**, and restart cinder service.

$ cinder-volume

1. Nova issues

i. Permissions of directory

    **/opt/stack, /etc /nova, / var /log /nova** user groups and users
    are stack. If somehow the problem, make sure that these directory
    permissions are correct.

    Cited a problem:

    please re-run nova-manage db sync

    This problem is probably caused by permission\ **. /var /log /nova**
    needs when /**etc/nova/nova.conf** debugs.

    logdir = / var / log / nova

    This option is very important when you debug, A problem can go to
    **/var /log /nova** in check.

    Therefore, when you encounter a strange installation problem, you
    can execute the following three commands:

sudo chown stack:stack /opt -R

sudo chown stack:stack /etc/nova -R

    sudo chown stack:stack /var/log/nova –R

ii. nova-compute services start unsuccessfully

Refer to the **/logs/nova-compute.log**

ERROR oslo.messaging.\_drivers.impl\_rabbit [-] AMQP server on
controller:5672 is unreachable: Socket closed. Try again in 5 seconds.

    If the compute node can’t communicate with RabbitMQ, check
    RabbitMQ’s password in **/etc/nova/nova.conf** first.

    The results show that the password is set incorrectly; no wonder
    compute node has been unable to communicate with RabbitMQ. After
    changing the RabbitMQ’s password, the compute node starts
    successfully.

    **SIOCADDRT: File exists**

.. [1]
   https://intelpedia.intel.com/Proxy\_at\_Intel

.. [2]
   ‘#’ for root user, ‘$’ for normal user, below the same

.. [3]
   http://pypi.douban.com/simple/

.. [4]
   http://pypi.gocept.com/simple/

.. [5]
   http://docs.openstack.org/developer/devstack/guides/multinode-lab.html

.. [6]
   https://github.com/openstack-dev/devstack

.. [7]
   http://blog.csdn.net/iloli/article/details/6431757

.. [8]
   http://www.linuxidc.com/Linux/2011-04/34278.htm

.. [9]
   http://blog.chinaunix.net/uid-26284395-id-2949145.html

.. [10]
   https://github.com/openstack-dev/devstack.git

.. [11]
   http://docs.openstack.org/developer/devstack/stack.sh.html

.. [12]
   http://docs.openstack.org/developer/devstack/stackrc.html

.. [13]
   http://docs.openstack.org/developer/devstack/configuration.html

.. [14]
   http://docs.openstack.org/developer/sahara/userdoc/cdh\_plugin.html

.. [15]
   http://www.slideshare.net/nearyd/neutron-open-vswt?qid=aa5d9d51-02da-4724-8a23-f812e857670c&v=default&b=&from\_search=2

.. [16]
   https://sharepoint.gar.ith.intel.com/sites/SSG-0751/SP/COE/\_layouts/WordViewer.aspx?id=/sites/SSG-0751/SP/COE/OpenStack

.. |image0| image:: media/image1.png
.. |image1| image:: media/image2.png
.. |image2| image:: media/image3.png
.. |image3| image:: media/image4.png
