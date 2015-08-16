=========================
Intel BMC/RMM Quick Start
=========================

| The **Intel Integrated Baseboard management controller (BMC) Web Console** provides both exceptional stability and permanent availability independent of the present *state of the server's operating system*. As a system administrator, you can use the Intel Integrated BMC Web Console to gain location-independent remote access to respond to critical incidents and to *undertake necessary maintenance*.
|
| Designed to work with the BMC, the **Intel RMM4 (Remote Management Module)** is a small form-factor mezzanine card that enables *remote KVM (Keyboard, Video, and Mouse)* and *media redirection* on your server system, from the built-in Web Console, from anywhere, at any time. [#]_
|
|



Prequisites & Configration
==========================

- Prequisites
    - hardware
        - BMC/RMM hardward support.
        - 1 extra cable
    - software
        - cygwin(openssh-client)
        - JRE(1.8 works)
        - scripts(batch)

.. image:: /images/bios_server_management_hl.png


- Congigure Mangement IP
    - NIC1 for BaseBoard mgmt (tagged **|O|O|**)
    - NIC2 for RMM (Remote Management Module), basicly a backup NIC of NIC1.

.. image:: /images/bios_bmc_lan_cfg_hl.png

- IPMI User Configurations
    - Username & Password should be configured
    - Changes user status into enabled

.. image:: /images/bios_bmc_lan_cfg2_hl.png



Baseboard Management Console
============================



| The Intelligent Platform Management Interface (IPMI) is a set of computer interface specifications for an autonomous computer subsystem that provides management and monitoring capabilities independently of the host system's CPU, firmware (BIOS or UEFI) and operating system. IPMI defines a set of interfaces used by system administrators for out-of-band management of computer systems and monitoring of their operation. For example, IPMI provides a way to manage a computer that may be powered off or otherwise unresponsive by using a network connection to the hardware rather than to an operating system or login shell. [#]_
|
|

The baseboard management controller (BMC) is the intelligence in the IPMI architecture. It is a specialized microcontroller embedded on the motherboard of a computer, generally a server. The BMC manages the interface between system management software and platform hardware. [#]_

- System Information

.. image:: /images/bmc_sysinfo.png

- Server Health (126 sensors w/ thresholds)

.. image:: /images/bmc_health.png

- Server Power Control

.. image:: /images/bmc_power_ctrl.png

- Virtual Front Panel

.. image:: /images/bmc_virt_panel.png



Remote Management Model
=======================

| **Intel Remote Management Model 4 (RMM4)** includes two components, Intel Remote Management Module 4 Lite (RMM4 Lite) and Intel Dedicated Management NIC (DMN).
| **The RMM4 Lite** is the key that can enable advance KVM and media sharing features for the server onboard Integrated BMC (ServerEngines* Pilot III Baseboard Management Controller).
| **The DMN** provides a dedicated management LAN interface with an Ethernet network controller. This DMN only provides access to the Integrated BMC management communication and is not shared with OS [#]_
|
|

- `RMM4 Technical Product Specification <http://download.intel.com/support/motherboards/server/sb/g24513005_rmm4_tps_r1_5.pdf>`_

Keyboard, Vdieo and Mouse(KVM) redirection
------------------------------------------


- Click **launch console** button will download a file named ``jViewer.jnlp`` , it's a xml file open with java.

.. image:: /images/console_redirection.png





Access RMM/KVM from remote desktop
----------------------------------


The Intel RMM/KVM can access via NAT/portforwarding. [#]_

- File: ``rmm@r3s2.bat``

.. sidebar:: Note

    enable portforward of 80 port requires admin previledge.

| Only 80 and 7578 port require portforward.
| Username can be replaced with you own at omega.sh.intel.com.
| If you want it passwordless, using 'echo \|' pipwork or ``ssh-copy-id`` might be a good idea.
|

.. code-block:: batch

    @ echo off
    title r3s2
    ssh -fgCNL 0.0.0.0:7578:172.16.3.103:7578 wenjie@10.239.44.158 || echo cygwin reguired!
    ssh -fgCNL 0.0.0.0:81:172.16.3.103:80 wenjie@10.239.44.158 || echo cygwin reguired!
    echo SSH proxy is working (port 7578&81)
    echo Don't trun it off!


.. image:: /images/screenshot_tunnel_r3s2.png

- File: ``jviewer@r3s2.jnlp``

use existing jnlp and replace received token in it with your token.


.. code-block:: xml
    :emphasize-lines: 3,12,17

    <?xml version="1.0" encoding="UTF-8"?>

    <jnlp spec="1.0+" codebase="http://172.16.3.103:80/Java">
    <!--
    <jnlp spec="1.0+" codebase="http://127.0.0.1:81/Java">
    -->
        <information>
            <title>JViewer</title>
            ...
            ...
        <application-desc>
            <argument>172.16.3.103</argument>
            <!--
            <argument>127.0.0.1</argument>
            -->
            <argument>7578</argument>
            <argument>NDR5DJy1nTcIpGw1</argument>
            <!-- one-time token, need to be replaced by latest one -->
            ...
            ...
        </application-desc>
    </jnlp>


.. image:: /images/screen_out_of_band_hl.png



Discoverings
============

.. image:: /images/nmap_smc.png


SMASH-CLP Console v1.09
-----------------------

| Targets: SMASH-CLP provides support for different configuration parameters of the server.
| For a complete list of targets please refer to the user's guide. Example targets
| are system1,sp1,logs1 etc.
|
|

.. code-block:: bash

    ssh root@172.16.3.103

.. image:: /images/smc_ssh.png







.. [#] http://download.intel.com/support/motherboards/server/sb/intel_rmm4_ibwc_userguide_r2_72.pdf>`_
.. [#] https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface
.. [#] https://en.wikipedia.org/wiki/Intelligent_Platform_Management_Interface#Baseboard_management_controller
.. [#] http://download.intel.com/support/motherboards/server/sb/g24513005_rmm4_tps_r1_5.pdf
.. [#] https://communities.intel.com/message/269675
