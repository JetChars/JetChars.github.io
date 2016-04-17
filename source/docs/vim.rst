=========================
Vim - My Favourite Editor
=========================

vi's full name is visual editor

.. image:: /images/vi-vim-cheat-sheet.svg

- save file with sudo privilege: ``:w !sudo tee %``
- in windows ^v(paste) has been changed to ^p
- down vim vindows version -- http://www.vim.org/download.php

Commnd Mode
===========

Move
----

============ =====================
key          description
============ =====================
j/k/h/l      left/right/up/down
gg/G/nG      top/button/n row of file
H/M/L        top/middle/button row of currnet screen
^$(){}       line/paragraph/section's start or end
============ =====================


Ex Mode
=======

Set
===

mostly stop a switch with **no** in front of it.

=============== ======================
option          description
=============== ======================
paste/nopaste   no auto indent for paste
nu/nonu         nu short for number, show line number
hlsearch        high light search item
=============== ======================

Split
=====

``sp/vsp <filename>``




Shotcuts
========

.. image:: /images/vi-vim-tutorial-1.svg
.. image:: /images/vi-vim-tutorial-2.svg
.. image:: /images/vi-vim-tutorial-3.svg
.. image:: /images/vi-vim-tutorial-4.svg
.. image:: /images/vi-vim-tutorial-5.svg
.. image:: /images/vi-vim-tutorial-6.svg
.. image:: /images/vi-vim-tutorial-7.svg

`fisa-vim-config <https://github.com/fisadev/fisa-vim-config.git>`_ -- popular vim config file
===============

- **require module** ``vim_debug`` ``isort``

.. code-block:: shell
    
    sudo apt-get install vim exuberant-ctags git
    sudo pip install dbgp vim-debug pep8 flake8 pyflakes isort


`Sublime Text <http://www.sublimetext.com/>`_
=============================================
=============================================

Can be run in vi mode.

shortcuts
---------

======================= ===========================================
Combination             Description
======================= ===========================================
alt_shift_{1~9}         switch window layout
F6                      check spelling
^/                      comment selected lines
^b                      compile
^B                      compile and run
^l                      select line(reps can select lines below)
^L                      entering multi-line editing mode
^[/]                    indent left/right
^{/}                    fold/collapse code-block
^P                      sublime cmds
^f                      search
^d                      select same, can be batch replaced
^`                      exec py cmds
shift_rightclick        multi-line select&edit
opt_rightclick(mac)     multi-line select&edit
======================= ===========================================


config
------

.. code-block:: json
    :linenos:

    {
      "font_size": 16,
      "update_check": false,
      "ignored_packages": [],
      "http_proxy":"proxy-us.intel.com:911",
      "tab_size": 4,
      "translate_tabs_to_spaces": false
    }


install pkgmgt module
---------------------

- use ``^``` calling sublime cli
- entering codes below
- then restart the sublime.


- code for sublime text2

.. code-block:: python

    import urllib2,os; pf='Package Control.sublime-package'; ipp = sublime.installed_packages_path(); os.makedirs( ipp ) if not os.path.exists(ipp) else None; urllib2.install_opener( urllib2.build_opener( urllib2.ProxyHandler( ))); open( os.path.join( ipp, pf), 'wb' ).write( urllib2.urlopen( 'http://sublime.wbond.net/' +pf.replace( ' ','%20' )).read()); print( 'Please restart Sublime Text to finish installation') 


- code for sublime text 3

.. code-block:: python

    import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())


manage pkgs w/ pkgmgt
---------------------

- install pkgs -- ``^p`` --> search install --> query pkgs
- remove pkgs -- ``^p`` --> search remove --> query pkgs
- good pkgs
    - SublimeCodeIntel -- auto-completion tool(works for python)
    - PyLinter -- pep8 highlighter
    - reStructureText Snippets -- auto-completion for rst
    - reStructureText Improved -- highlighter
    - HTML/CSS/JS Prettify -- auto formater
    - sublime-rst-completion -- auto complete the rst


PyLinter
^^^^^^^^

https://github.com/biermeester/Pylinter


- module pylint must be installed
    - ``python -m pip install pylint`` -- install pylint
    - ``python -m pip show pylint`` -- get pylint's location

.. code-block:: json

    {
        "pylint_path": "C:\\Python27\\Lib\\site-packages\\pylint",
        "use_icons": true,
        "run_on_save": true,
        "message_stay": true
    }





Issues
======

can't use backspace in insert mode
----------------------------------


solution:

add a new setting in vimrc, ``set backspace=indent,eol,start``
