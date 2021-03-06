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

- Context Management Protocol -- defines function include ``__enter__()`` and ``__exit__()``
- Context Managet -- an implementation of CMP
    - use ``with context_expression [as targets]: with-body`` enter&exit context
    - ``__enter__()`` -- enter context before with-body
    - ``__exit__()`` -- exit context after with-body
    - like ``try/finally`` -- can make sure context exit correctly

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
     
contextlib
^^^^^^^^^^

Utilities for with-statement contexts.

- contextlib.contextmanager(func) -- decorator can be used to define a factory function for with statement context manager, w/o creating ``__enter__()`` or ``__exit__()``


.. code-block:: python

    from contextlib import contextmanager

    @contextmanager
    def tag(name):
        print "<%s>" % name
        yield
        print "</%s>" % name

.. code-block:: console

    >>> with tag("h1"):
    ...    print "foo"
    ...
    <h1>
    foo
    </h1>


.. code-block:: python


    from contextlib import contextmanager

    @contextmanager
    def closing(thing):
        try:
            yield thing
        finally:
            thing.close()



    from contextlib import closing
    import urllib

    with closing(urllib.urlopen('http://www.python.org')) as page:
        for line in page:
            print line




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



