==============
Virtualization
==============


Hypervisors
===========




Libvirt
=======

libvirt is an open source API, daemon and management tool for managing platform virtualization. It can be used to manage KVM, Xen, VMware ESX, QEMU and other virtualization technologies. These APIs are widely used in the orchestration layer of hypervisors in the development of a cloud-based solution. [#]_


* ``/usr/sbin/libivirtd -d`` is a background process
* ``/var/log/libvirt/libvirtd.log`` default log file
* ``libvirt.xml`` every instance has a conf file

* hvm (hardware virtual machine)
* pvm (parallel virtual machine)


.. image:: images/libvirt_support.svg


Virsh -- Virtualization Management Interface
============================================

================ ======================================================
command          description
================ ======================================================
create           create an domain from xml(direct into running state)
define/undefine  define or undefine won't into running state
destroy          stop vm immediately, but not delete domain
shutdown         soft stop vm
list             show active domain list, --all (show include inactive)
edit <ID/name>   modify guest's xml file
dumpxml xxx.xml  output guest's xml
connect          connect vm
vncdisplay vm    create a vnc link for vm
console vm       connect the pty console of vm
================ ======================================================



Docker
======

* Concept
    * must have same os kernel
    * native CPU/syscall/kernel
    * use go language
    * can't over commitment
    * lightweight 'vm'





.. [#] http://en.wikipedia.org/wiki/Libvirt
