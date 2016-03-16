======
Python
======


`online doc <https://docs.python.org/3/>`_


- python compilers: python,`cython <http://docs.cython.org/src/reference/language_basics.html>`_ ,Jython




Get Helps
=========

.. code-block:: python

    # can omit "" if module imported
    help("full path of module/class")
    help("re.compile")
    dir(<full path of module/class>)   # class should be imported first




HelloWorld
==========

shebang/sh-bang/sharp-bang
--------------------------

- **#!/usr/local/bin/python**
- **#!/usr/bin/env python** -- only work w/ OS have cmd env
- **bash test.sh** -- sh-bang will not take effect in this situation
- issues
    - **bad interpreter: Permission denied**
    - **bad interpreter: No such file or directory**
- realization of python
    - Cpython
    - Jython
    - IronPython
    - Stackless



Data Structures
===============
===============

Sequences
---------

list, tuple and str are sequences, shared some same methods






Statements
==========
==========




loop
----

- ``for i in range(a,b)``
- ``for k,v in dict``
- ``while True``
- ``pass`` -- do nothing, used to make sure the integrity of code block
- ``break/continue`` -- same as other languages


Capture of err
--------------

.. code-block:: python

    try:
        a = b
        b = c
    except Exception, e:
        print Exception, ":", e


    import sys
    try:
        a = b
        b = c
    except:
        info = sys.exec_info()
        print info[0], ":", info[1]

    import traceback
    try:
        a = b
        b = c
    except:
        f = open("log.txt", 'a')
        traceback.print_exc()
        f.flush()   # dump from internal I/O buffer



Iterator
--------

- Iterator class should have pre-defined function ``next()`` and ``__iter__``
- ``iter()`` can translate list into a iterator


.. code-block:: python

    lst = range(5)
    it = iter(lst)
    try:
        while True:
            val = it.next()
            print val
    except StopIteration:
        pass



    # define a iterator class
    class Fabs(object):
        def __init__(self, max):
            self.max = max
            self.n, self.a, self.b = 0, 0, 1
        def __iter__(self):
            return self
        def next(self):
            if self.n < self.max:
                r = self.b
                self.a, self.b = self.b, self.a + self.b
                self.n = self.n + 1
                return r
            raise StopIteration()

    print Fabs(5)
    for key in Fabs(5):
        print key



Judgement
---------

- ``if/elif/else`` -- there is no swith statement in python
- ``is/in/not`` -- not can cooperate w/ ``is/in``
    - ``is`` used to judge the obj's type
    - ``in`` used to judge including relationship

.. code-block:: python

    a is None
    a is b
    a is not b
    a in b
    a not in b



Generator
---------

``yield`` makes function a generator

.. code-block:: python

    def fab(max):
        n, a, b = 0, 0, 1
        while n < max:
            yield b
            a, b = b, a+b
            n = n + 1



Context manager
---------------

``with ... as ...:`` will help us to call the close() function.

.. code-block:: python

    # try except is hard to use
    # =========================
    try:
        f = open('xxx')
        do something
    except:
        do something
    finally:
        f.close()

    # correct format
    # ==============
    try:
        f = open('xxx')
    except:
        print 'fail to open'
        exit(-1)
    try:
        do something
    except:
        do something
    finally:
        f.close()

    # elegant way
    # ===========
    try:
        with open('xxx') as f:
            do something
    except xxxError:
        do something about err
     




Permanent storage
=================

pickle
------

- only support **ASCII string**, unicode not supported(will crash the pickle).
- cPicle -- enhanced version of pickle(faster)

PEPs -- Python Enhancement Proposals
====================================

`PEP 0 -- Index of PEPs <https://www.python.org/dev/peps/>`_
`PEP 0381 -- Mirroring infrastructure for PyPI <https://www.python.org/dev/peps/pep-0381/>`_
bandersnatch -- Mirroring tool that implements the client (mirror) side of PEP 381




Applications
============

pip
---

`get-pip.py <https://bootstrap.pypa.io/get-pip.py>`_


flask -- py based web framework
-------------------------------


http://flask.pocoo.org/

sphinx
------

http://sphinx-doc.org/latest/index.html


fabric
------

http://www.fabfile.org/

Fabric is a Python (2.5-2.7) library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks.


