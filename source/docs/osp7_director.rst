===================
RedHat RHEL7.1 OSP7
===================

- manage w/ python-rdomanager-oscplugin (osp director)
- provisioning undercloud w/ puppet
- instead of used 6 nics, 2 nic is minimal
- a redhat account was needed
- use ironic to build overcloud
- build image w/ tripleo-image-elements & diskimage-builder




`RedHat OSP7 Docs <https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux_OpenStack_Platform/>`_
`OSP7 images <https://access.redhat.com/downloads/content/191/ver=7.0/rhel---7/7.0/x86_64/product-downloads>`_

Prepare
=======



.. code-block:: bash

    # change hostname
    # ---------------
    hostnamectl set-hostname manager.example.com
    hostnamectl set-hostname --transient manager.example.com
    echo "127.0.0.1   manager.example.com manager" > /etc/hosts
    
    # configure global proxy
    # ----------------------
    echo "no_proxy1=intel.com,localhost,127.0.0.1,172.16.0.1
    printf -v no_proxy2 '%s,' 172.16.{0..16}.{1..255};
    no_proxy2=\"\${no_proxy2%,}\";
    printf -v no_proxy3 '%s,' 192.0.2.{1..255};
    no_proxy3=\"\${no_proxy3%,}\";
    export no_proxy=\${no_proxy1},\${no_proxy2},\${no_proxy3}
    unset no_proxy1
    unset no_proxy2
    unset no_proxy3
    " >> /etc/bashrc
    
    # create stack user
    # -----------------
    useradd stack
    passwd stack --stdin << EOF
    123456
    EOF
    echo "stack ALL=(root) NOPASSWD:ALL" | tee -a /etc/sudoers.d/stack
    chmod 0440 /etc/sudoers.d/stack
    
    # add template&image folders
    # --------------------------
    su - stack
    mkdir ~/images
    mkdir ~/templates
    
    # enable ip forward
    # -----------------
    exit
    echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf
    sysctl -p /etc/sysctl.conf
    
    # register redhat
    # ---------------
    
    sudo subscription-manager register
    sudo -E subscription-manager list --available --all   # -E is required in an internal network
    sudo subscription-manager attach --pool=8a85f9814f02ff15014f08c451ee3644   # pick first one
    sudo subscription-manager repos --disable=*   # added in html version
    sudo subscription-manager repos --enable=rhel-7-server-rpms --enable=rhel-7-server-optional-rpms --enable=rhel-7-server-extras-rpms --enable=rhel-7-server-openstack-7.0-rpms --enable=rhel-7-server-openstack-7.0-director-rpms
    sudo yum update -y

- not always get same register ID

.. code-block:: console 

    root@osp7 ~]# subscription-manager register 
    Username: weiting.chen@intel.com
    Password: 
    The system has been registered with ID: 943016c8-26d6-429e-b9b8-fca4f8211fa5
    
    [stack@manager ~]$ sudo -E subscription-manager register
    Username: weiting.chen@intel.com
    Password: 
    The system has been registered with ID: ef6c499b-784a-4d37-9736-ccf401e98450


create ssl files
----------------

.. code-block:: console

    [stack@osp7 ~]$ openssl req -new -x509 -key privkey.pem -out cacert.pem -days 365
    You are about to be asked to enter information that will be incorporated
    into your certificate request.
    What you are about to enter is what is called a Distinguished Name or a DN.
    There are quite a few fields but you can leave some blank
    For some fields there will be a default value,
    If you enter '.', the field will be left blank.
    -----
    Country Name (2 letter code) [XX]:CN
    State or Province Name (full name) []:Shanghai
    Locality Name (eg, city) [Default City]:Shanghai
    Organization Name (eg, company) [Default Company Ltd]:Intel APAC R&D        
    Organizational Unit Name (eg, section) []:SSG
    Common Name (eg, your name or your server's hostname) []:Weiting, Chen
    Email Address []:weiting.chen@intel.com


configure undercloud
--------------------

.. code-block:: bash

    sudo yum install -y python-rdomanager-oscplugin
    cp /usr/share/instack-undercloud/undercloud.conf.sample undercloud.conf
    openstack undercloud install

.. code-block:: console

    [stack@osp7 ~]$ ls /tmp/tmpbIW3ir/
    bin                   __init__.pyo                       root.d
    cleanup.d             install.d                          rsyslog.d
    config.json.template  os-apply-config                    selinux
    custom-policies       os-refresh-config                  source-repository-os-cloud-config
    dib-init-system       package-installs.yaml              source-repository-puppet-modules
    element-deps          pkg-map                            source-repository-tripleo-heat-templates
    element-provides      post-install.d                     source-repository-tuskar
    environment.d         pre-install.d                      svc-map
    extra-data.d          puppet-stack-config.pp             tests
    finalise.d            puppet-stack-config.yaml.template  upstart
    __init__.py           README.md
    __init__.pyc          README.rst


[stack@manager ~]$ openstack overcloud image upload
ERROR: Required file "./deploy-ramdisk-ironic.initramfs" does not exist

get the admin password ``sudo hiera admin_password``

neutron subnet-list
neutron subnet-update `neutron subnet-list | grep start | awk '{print $2}'` --dns-nameserver 10.248.2.1
neutron subnet-show `neutron subnet-list | grep start | awk '{print $2}'`

172.16.3.101(r3s1)
00:1e:67:b3:ba:d1 nic 1

172.16.3.107 (r3s4)
00:1e:67:bc:01:33 nic1
00:1E:67:BC:01:37 bmc1
openstack baremetal introspection bulk start

[stack@manager ~]$ openstack baremetal introspection bulk start
Setting available nodes to manageable...
Starting introspection of node: 85830c07-f106-4287-8619-68d352aaf282
Starting introspection of node: ea979244-7fef-48f7-8c4a-24cbf05aac43
Waiting for discovery to finish...
Discovery for UUID 85830c07-f106-4287-8619-68d352aaf282 finished successfully.
Discovery for UUID ea979244-7fef-48f7-8c4a-24cbf05aac43 finished successfully.
Setting manageable nodes to available...
Node 85830c07-f106-4287-8619-68d352aaf282 has been set to available.
Node ea979244-7fef-48f7-8c4a-24cbf05aac43 has been set to available.

openstack flavor set --property "capabilities:boot_option"="local" <flavor>


puppet
======

- ".ppk" of PuTTY means putty private key
puppetmaster puppet(agent)

/etc/puppet/puppet.conf
 add server

root@agent# puppet agent --no-daemonize --onetime --verbose   # running foreground one time only
root@server# puppet cert list
root@server# puppet cert sign "<hostname>"   # after this, agent can connect the server


``/etc/puppet/fileserver.conf`` configures the fileserver management
    - path: /etc/puppet/files
    - access with scheme ``puppet://``

grep /var/log/syslog


``/etc/puppet/manifests/`` would be the root of any class
    - ``/etc/puppet/manifests/classes``
    - ``/etc/puppet/manifests/<filename>.pp``

# use this as comment
# other classes can be imported from manifest root folder

import classes

class cname {
    package {

    }
    file {
        owner => root, group => root, mode =>
    }

}

Note

puppet apply --detailed-exitcodes /etc/puppet/manifests/puppet-stack-config.pp
Warning: You cannot collect without storeconfigs being set on line 262 in file /etc/puppet/manifests/puppet-stack-config.pp
Warning: You cannot collect without storeconfigs being set on line 266 in file /etc/puppet/manifests/puppet-stack-config.pp
Warning: You cannot collect without storeconfigs being set on line 270 in file /etc/puppet/manifests/puppet-stack-config.pp
Error: Unknown function count at /etc/puppet/manifests/puppet-stack-config.pp:16 on node osp7
Error: Unknown function count at /etc/puppet/manifests/puppet-stack-config.pp:16 on node osp7

puppet module install puppetlabs-stdlib
[stack@osp7 ~]$ puppet apply --detailed-exitcodes /etc/puppet/manifests/puppet-stack-config.pp
Warning: You cannot collect without storeconfigs being set on line 262 in file /etc/puppet/manifests/puppet-stack-config.pp
Warning: You cannot collect without storeconfigs being set on line 266 in file /etc/puppet/manifests/puppet-stack-config.pp
Warning: You cannot collect without storeconfigs being set on line 270 in file /etc/puppet/manifests/puppet-stack-config.pp
Error: Could not find data item ntp::servers in any Hiera data file and no default supplied at /etc/puppet/manifests/puppet-stack-config.pp:16 on node osp7
Error: Could not find data item ntp::servers in any Hiera data file and no default supplied at /etc/puppet/manifests/puppet-stack-config.pp:16 on node osp7

https://forge.puppetlabs.com/puppetlabs/stdlib


selinux
=======

Intro
-----

- 3 status
    - enforcing -- violating selinux policy is prohibited and violations are logged
    - permissive -- viloations generate warning and the violation is logged, but the action is allowed to continue
    - disabled -- turned off, if want turn it on, reboot is required.
- logged at ``/var/log/messages``
- ``/etc/sysconfig/selinux`` links to ``/etc/selinux/config``
    - make permanently change

commands
--------

- ``setenforce`` -- won't work if selinux is disabled
    - ``setenforce 0`` -- permissive
    - ``setenforce 1`` -- enforcing
- ``getenforce`` -- get current selinux status
- ``ll -z`` show file list with context
- ``chcon`` -- change a file's selinux security context
    - ``-R`` -- recursively
    - ``--reference`` -- copy context from other file
    - ``-u`` -- set the user portion of the context
    - ``-r`` -- set the role ...
    - ``-t`` -- set the type ...


CISCO Switch
============

exec/configure (mode or context)
- exec mode -- make changes temporary
- configure mode -- make permantly changes


create a vlan

.. code-block:: telnet

    configure terminal

hp switch
=========


http://www.hp.com/rnd/support/manuals/2910.htm
ftp://ftp.hp.com/pub/networking/software/6400-5300-4200-3400-AdvTrafficMgmt-Oct2005-Ch-02-VLANs.pdf

- vlan
    - tagged: Allows the port to join multiple VLANs
    - untagged: Allows VLAN connection to a device that is configured for an untagged VLAN instead of a tagged VLAN. A port can be an untagged member of only one port-based VLAN
    - forbid: Prevents the port from joining the VLAN, even if GVRP is enabled on the switch
    - no: Appears when the switch is not GVRP-enabled; prevents the port from - or - joining that VLAN.


issues
======


1. Package does not match intended download 


.. code-block:: console

Delta RPMs disabled because /usr/bin/applydeltarpm not installed.
openssh-6.6.1p1-12.el7_1.x86_6 FAILED                                           ]  72 kB/s | 180 kB  00:01:50 ETA 
https://cdn.redhat.com/content/dist/rhel/server/7/7Server/x86_64/os/Packages/openssh-6.6.1p1-12.el7_1.x86_64.rpm: [Errno -1] Package does not match intended download. Suggestion: run yum --enablerepo=rhel-7-server-rpms clean metadata
Trying other mirror.
NetworkManager-1.0.0-16.git201 FAILED                                           ]  70 kB/s | 3.5 MB  00:01:04 ETA 
https://cdn.redhat.com/content/dist/rhel/server/7/7Server/x86_64/os/Packages/NetworkManager-1.0.0-16.git20150121.b4ea599c.el7_1.x86_64.rpm: [Errno -1] Package does not match intended download. Suggestion: run yum --enablerepo=rhel-7-server-rpms clean metadata
Trying other mirror.
python-libs-2.7.5-18.el7_1.1.x FAILED                                           ]  25 kB/s | 3.4 MB  00:03:05 ETA 
https://cdn.redhat.com/content/dist/rhel/server/7/7Server/x86_64/os/Packages/python-libs-2.7.5-18.el7_1.1.x86_64.rpm: [Errno -1] Package does not match intended download. Suggestion: run yum --enablerepo=rhel-7-server-rpms clean metadata
Trying other mirror.


- Solution: delete corrupt packages

.. code-block:: bash

    sudo rm -rf /var/cache/yum/x86_x64/7Server/<repo>/packages/<pkg>




2. can't create context



3. exit 6

Notice: /Stage[main]/Nova::Compute/Nova::Generic_service[compute]/Service[nova-compute]/ensure: ensure changed 'stopped' to 'running'
Notice: Finished catalog run in 17.07 seconds
+ rc=6
+ set -e
+ echo 'puppet apply exited with exit code 6'
puppet apply exited with exit code 6
+ '[' 6 '!=' 2 -a 6 '!=' 0 ']'
+ exit 6
[2015-08-13 18:09:06,946] (os-refresh-config) [ERROR] during configure phase. [Command '['dib-run-parts', '/usr/libexec/os-refresh-config/configure.d']' returned non-zero exit status 6]

[2015-08-13 18:09:06,946] (os-refresh-config) [ERROR] Aborting...
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/usr/lib/python2.7/site-packages/instack_undercloud/undercloud.py", line 526, in install
    _run_orc(instack_env)
  File "/usr/lib/python2.7/site-packages/instack_undercloud/undercloud.py", line 461, in _run_orc
    _run_live_command(args, instack_env, 'os-refresh-config')
  File "/usr/lib/python2.7/site-packages/instack_undercloud/undercloud.py", line 297, in _run_live_command
    raise RuntimeError('%s failed. See log for details.', name)
RuntimeError: ('%s failed. See log for details.', 'os-refresh-config')
ERROR: openstack Command 'instack-install-undercloud' returned non-zero exit status 1


4. Can't load policy

.. code-block:: console

dib-run-parts Sun Aug 16 03:57:03 CST 2015 Running /usr/libexec/os-refresh-config/configure.d/88-httpd-vhost-port
+ set -o pipefail  
+ add-rule INPUT -p tcp --dport 8088 -j ACCEPT
active
iptables: Bad rule (does a matching rule exist in that chain?).
+ mkdir -p /etc/httpd/conf.d
++ dirname /usr/libexec/os-refresh-config/configure.d/88-httpd-vhost-port
+ sudo cp -r /usr/libexec/os-refresh-config/configure.d/ipxe-vhost.template /etc/httpd/conf.d/10-ipxe_vhost.conf
+ os-svc-enable -n apache2
WARNING: map-services has been deprecated.  Please use the svc-map element.
+ os-svc-restart -n apache2
WARNING: map-services has been deprecated.  Please use the svc-map element.
+ '[' -x /usr/sbin/semanage ']'
+ semanage fcontext -a -t httpd_sys_content_t '/httpboot(/.*)?'
SELinux:  Could not downgrade policy file /etc/selinux/targeted/policy/policy.29, searching for an older version.
SELinux:  Could not open policy file <= /etc/selinux/targeted/policy/policy.29:  No such file or directory
/sbin/load_policy:  Can't load policy:  No such file or directory
libsemanage.semanage_reload_policy: load_policy returned error code 2.
SELinux:  Could not downgrade policy file /etc/selinux/targeted/policy/policy.29, searching for an older version.
SELinux:  Could not open policy file <= /etc/selinux/targeted/policy/policy.29:  No such file or directory
/sbin/load_policy:  Can't load policy:  No such file or directory
libsemanage.semanage_reload_policy: load_policy returned error code 2.
ValueError: Could not commit semanage transaction
[2015-08-16 03:57:12,568] (os-refresh-config) [ERROR] during configure phase. [Command '['dib-run-parts', '/usr/libexec/os-refresh-config/configure.d']' returned non-zero exit status 1]

[2015-08-16 03:57:12,569] (os-refresh-config) [ERROR] Aborting...
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/usr/lib/python2.7/site-packages/instack_undercloud/undercloud.py", line 526, in install
    _run_orc(instack_env)
  File "/usr/lib/python2.7/site-packages/instack_undercloud/undercloud.py", line 461, in _run_orc
    _run_live_command(args, instack_env, 'os-refresh-config')
  File "/usr/lib/python2.7/site-packages/instack_undercloud/undercloud.py", line 297, in _run_live_command
    raise RuntimeError('%s failed. See log for details.', name)
RuntimeError: ('%s failed. See log for details.', 'os-refresh-config')
ERROR: openstack Command 'instack-install-undercloud' returned non-zero exit status 1
[stack@manager ~]$ vi /etc/selinux/targeted/policy/policy.29

- Solution : enable selinux


5. horizon(rdo dashboard) can't be accessed other than the localhost

.. sidebar:: Tips

    httpd will logging each horizon access at ``/var/log/httpd/horizon_access.log``

By default, OSP7 Undercloud’s dashboard can’t be accessed by hosts other than the localhost. 
If you want do that.

Edit ``/etc/openstack-dashboard/local_settings``
Change `` ALLOWED_HOSTS = ['192.0.2.1', 'manager.example.com', 'localhost', ] ``  to  ``ALLOWED_HOSTS = ['*']``
Then restart the httpd service ``sudo service httpd restart``

If still not work, try edit ``/etc/httpd/conf.d/10-horizon_vhost.conf``
add a new line ``ServerAlias *``

for more info, pls refer to:
https://bugzilla.redhat.com/show_bug.cgi?id=1119920
https://ask.openstack.org/en/question/44151/red-hat-rdo-horizon-dashboard-will-not-load-from-internet/





[stack@manager ~]$ openstack baremetal introspection bulk start
Setting available nodes to manageable...
WARNING: ironicclient.common.http Request returned failure status.
WARNING: ironicclient.common.http Error contacting Ironic server: Node 1f0dde23-597e-48aa-9d86-5ea203a6d65d is locked by host manager.example.com, please retry after the current operation is completed. (HTTP 409). Attempt 1 of 61
WARNING: ironicclient.common.http Request returned failure status.

.. code-block:: bash

    sudo service openstack-ironic-* restart


[root@manager ~]# service --status-all
netconsole module not loaded
Configured devices:
lo br-ctlplane eno1 eno2 eno3 eno4 enp6s0f0 enp6s0f1
Currently active devices:
lo eno1 eno2 eno3 eno4 enp6s0f0 enp6s0f1 virbr0 br-ctlplane


No Presto metadata available for rhel-7-server-rpms

.. code-block:: bash

    sudo yum clean metadata
    sudo yum clean all
    sudo yum update -y
