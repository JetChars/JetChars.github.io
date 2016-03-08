=======
Windows
=======


Tips
====

- Mirror a device: ``network neighbour --> mirror a device``
    - windows network neighbor can mirror sharepoint into local filesystem
- Add a startup item: ``C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`` or ``C:\users\username\appdata\roaming\Microsoft\Windows\Start Menu\Programs\StartUp``
- change hosts: ``C:\Windows\System32\drivers\etc``
- make mycompter default in explorer: ``%windir%/explorer.exe ,``
- any shortcut can change icon
- **dll** file can't delele directly, change name to .txt first
- stop password protection to enable LAN sharing
- fix bluetooth device disconnect issue: ``compmgmt-->device manager-->bluetooth controller-->power management-->not save power``
- epoch -- 1970-01-01 00:00:00 UTC

Shotcut keys
------------

================== ========================
combo              description
================== ========================
^ + <-/->          move skip a word
^ + c/v            copy paste
^ + z/y            undo, redo
^ + w              close tab
^shift + <-/->     select a word
shift + <-/->      select a character
shift + home/end   select a line
alt + direction    change screen direction
alt + space + N    minimize current window
cmd + enter        enable narrator (pronounce key strokes)
cmd x              enter god mode
================== ========================



Applications
============

built-in Apps
-------------

**Tools**

================== ===================
name               description
================== ===================
notepad            text editor
calc               calculator
mspaint            paint pallet
explorer           file explorer
charmap            get special chars
cleanmgr           clean system trash
write              wordpad
mstsc              remote desktop
osk                on screen keyboard
================== ===================


**sys mgmt**

================= ==================================
name              description
================= ==================================
dcomcnfg          component services
Msconfig          system configuration
regedt32          register management
devmgmt           device management
eudcedit          private character editor (create new char)
perfmon           performance monitor
compmgmt          computer management
fsmgmt            share folder management
================= ==================================

**cmdline tools**

================================ ======================
cmd                              description
================================ ======================
powercfg -h off/on               sleepmode management
chkdsk /r                        repair disk
help [command]                   get help
tasklist                         show task list
taskkill                         kill a task
schtask  /tn tname /tr tbinary   schedule a task
date                             set date
time                             set time
regsvr32                         register a server
================================ ======================






MS Applications
---------------


global shortcut keys

============== =================
combo          description
============== =================
cmd + s        onenote snapshot
cmd + y        open lync
============== =================



OneNote
^^^^^^^

- surface compatible
- Audio recording & hand writing simultaniously
- math-addon

skype/lync
^^^^^^^^^^

- keep icon out of dock: ``tools->settings->advanced``

IE
^^

============== =================
combo          description
============== =================
f5/^r          refresh
f11            full screen
^t/T/w         new/reopen/close a tab
^enter         auto-complete .com
^alt+enter     auto-complete .org
^shift+enter   auto-complete .net
============== =================




legacy Applications
-------------------

clover - explorer enhancement extension
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

goAgent -- google free vpn
^^^^^^^^^^^^^^^^^^^^^^^^^^






Metro Applications
------------------


drawboard
^^^^^^^^^

- free & support surface hand writing notes.




Command Prompt
==============


network tools
-------------

.. code-block:: bat

    ping
    pathping
    netsh interface portproxy add v4tov4 listenport=1080 connectaddress=10.239.4.80 connectport=1080
    netsh interface portproxy show all
    rem change commandprompt screen size
    mode con: cols=160 lines=78




