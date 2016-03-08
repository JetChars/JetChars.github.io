======
Python
======


`online doc <https://docs.python.org/3/>`_


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
