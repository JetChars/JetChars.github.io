====
PEP8
====

Python Enhancement Proposal [#]_  8 is a Style guide for python code [#]_









Pylint
======
======

pylint is a python code analysing tool
- can analys faults in python code.
- find codes ummet pep8

pylint in vim
-------------

.. code-block:: shell

    set makeprg=pylint\ --reports=n\ --output-format=parseable\ %:p
    set errorformat=%f:%l:\ %m    

.. code-block:: shell

    autocmd FileType python set makeprg=pylint\ --reports=n\ --msg-template=\"{path}:{line}:\ {msg_id}\ {symbol},\ {obj}\ {msg}\"\ %:p
    autocmd FileType python set errorformat=%f:%l:\ %m


- add either of above config to /etc/vim/vimrc
- exec **pylint** by using cmd ``:make`` within vim




issues
------

- invalid constant name -- should be changed to upper case






References
==========
==========


.. [#] https://www.python.org/dev/peps/
.. [#] https://www.python.org/dev/peps/pep-0008/
.. [#] http://www.ibm.com/developerworks/cn/linux/l-cn-pylint/
