=========================
Vim - My Favourite Editor
=========================

.. image:: images/vi-vim-cheat-sheet.svg

- save file with sudo privilege: ``:w !sudo tee %``


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

.. image:: images/vi-vim-tutorial-1.svg
.. image:: images/vi-vim-tutorial-2.svg
.. image:: images/vi-vim-tutorial-3.svg
.. image:: images/vi-vim-tutorial-4.svg
.. image:: images/vi-vim-tutorial-5.svg
.. image:: images/vi-vim-tutorial-6.svg
.. image:: images/vi-vim-tutorial-7.svg

`fisa-vim-config <https://github.com/fisadev/fisa-vim-config.git>`_ -- popular vim config file
===============

- **require module** ``vim_debug`` ``isort``


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

