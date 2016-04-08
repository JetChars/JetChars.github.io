==============
Mac as Main OS
==============

ShortCuts
=========

Mac Featured
------------

==================== ==============================
commands                 description
==================== ==============================
cmd + ?              help
cmd + space          spotlight(can work as calc & dict)
hold alt             see hidden options
hold cmd             toggle icons in upright corner
space                quick preview
==================== ==============================


* MS Windows replacement

======================== ==============================
commands                 description
======================== ==============================
fn + up/down/left/right  pgup/pgdn/home/end
fn + delete              delete
cmd + enter              insert
cmd                      win
======================== ==============================


* Window Management

====================== ==============================
commands               description
====================== ==============================
cmd + t/w/z/Z          create/close/resume/redo tab
cmd + n/m/^f           new/min/max window
cmd + click/shiftclick open/open and turn to new tab
cmd + {/}              prev/next tab
cmd + 0/-/+            default/smaller/bigger font
cmd + q                quit software(w/ all windows & tabs)
====================== ==============================

Safari
------

============================ ==============================
commands                     description
============================ ==============================
cmd + r                      refresh
cmd + B                      show favorite
cmd + l                      address bar
cmd + L                      side bar
cmd + D (shift + rightclick) add to readlist
cmd + 1~9                    quick open bookmark
cmd + alt + 2                history
cmd + alt + b                bookmark management
cmd + tab/ shifttab          next/prev tab
cmd + f1                     swith screen mode
============================ ==============================

Xcode
-----

================== ============
commands           description
================== ============
cmd + r            run
cmd + s            save
================== ============


Special keys
------------

alt + [0-9a-z] or other symbols can create special symbols

============== ==================
combo          symbols
============== ==================
1234567890-=   ¡™£¢∞§¶•ªº–≠
!@#$%^&*()_+   ⁄€‹›ﬁﬂ‡°·‚—±
qwertyuiop[]\  œ∑´®†\¨ˆøπ“‘«
QWERTYUIOP{}|  Œ„´‰ˇÁ¨ˆØ∏”’»
============== ==================

Terminal
--------

============== ==================
commands       description
============== ==================
cmd_t          create a tab
cmd_{/}        switch tabs
^a|e           front or end of line
============== ==================



Terminal beutify
----------------

`oh-my-zsh <https://github.com/robbyrussell/oh-my-zsh>`_

- install oh-my-zsh w/ 
    - ``sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"``
- install powerline-fonts 
    - ``git clone http://github.com/powerline/fonts``
    - import fonts to mac font lib manually
- change font at terminal preferences
    - not work well w/ macOS above 10.10
    - only work w/ font ``Ubuntu Mono derivative Powerline``
    

Issues
======

Cannot find bluetooth device
----------------------------

1. shutdown
2. reset **power management unit** : ``shift+ctrl+option+cmd`` 5sec
3. reset **NVRAM** : ``option+cmd+p+r`` 4 times bibi

Cann't detect smb server
------------------------

.. sidebar:: Note
    
    **<user>@** can be omitted if anonymous user.

input **smb://<user>@<ip>** at safari will start to mount it.




Softwares
=========

Safari
------

enable inspection mode: ``preferences --> advance --> developer``

glims -- safari enhancement
^^^^^^^^^^^^^^^^^^^^^^^^^^^

`official site <http://www.machangout.com>`_
not compatible w/ latest version safari




PopClip -- rightclick enhancement tool
--------------------------------------

It can install various of plugins, like `Paste and Match Stype <http://pilotmoon.com/popclip/extensions/page/PasteAndMatch>`_ , it can help mac to **Paste as Plain Text**



brew -- package management software
-----------------------------------

.. code-block:: bash

    curl -LsSf http://github.com/mxcl/homebrew/tarball/master | sudo tar xvz -C/usr/local --strip 1 


Chrome
------

.. code-block:: bash

    # assign proxy manually
    open -a /Applications/Google Chrome.app --args --proxy-server=host#:port#

    # ignore certificate errors
    /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --ignore-certificate-errors &> /dev/null &
    # or
    open -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --args --ignore-certificate-errors



Visual Studio Code & ASP.NET 5 [#]_
-----------------------------------

.. code-block:: bash
    :linenos:



Other Good Softwares
--------------------

- bartender -- mini icons management(upright corner)
- hyperdock -- windows like dock preview & screen split
- aircontrol -- graphical recognition for music ctrl



.. [#] http://www.itworld.com/article/2917266/development/how-to-install-and-use-visual-studio-code-and-aspnet-5-on-mac-os-x.html
