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

Can be run in vi mode.

.. code-block:: json
    :linenos:

    {
      "font_size": 19,
      "update_check": false,
      "ignored_packages": []
    }
