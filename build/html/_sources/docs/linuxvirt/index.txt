==============
Virtualization
==============


Hypervisors
===========




Libvirt
=======

libvirt is an open source API, daemon and management tool for managing platform virtualization. It can be used to manage KVM, Xen, VMware ESX, QEMU and other virtualization technologies. These APIs are widely used in the orchestration layer of hypervisors in the development of a cloud-based solution. [#]_

It will create a linuxbridge **virbr0** , counterpart is **xenbr0** for xen, **vif0.0** for xen guest, **peth0** for xen kernel.


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

.. code-block:: guess

    virsh edit instanceid


`TI Calculators <http://www.ticalc.org/basics/calculators/index.html>`
=====================================================================


buntch of TI's calculators can run in emulators at mac/linux/windows.



Docker
======

* Concept
    * must have same os kernel
    * native CPU/syscall/kernel
    * use go language
    * can't over commitment
    * lightweight 'vm'

`Interactive Tutorial <https://www.docker.com/tryit/>`_



.. [#] http://en.wikipedia.org/wiki/Libvirt
