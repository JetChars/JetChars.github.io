===================
Documentation Tools
===================


`Sphinx <http://sphinx-doc.org>`_ - Python Document Generator
==================================================================================


With this tool, we can extract manual from our python project's source code, convert rst file into html tex or pdf files, and so on ... 

.. warning:: html can be build with **svg**, but latex need to be converted into **png**

| `Chinese Documentation <http://www.pythondoc.com/sphinx/index.html>`_
| `Another Chinese Documentation <http://zh-sphinx-doc.readthedocs.org/en/latest/>`_
|
|


Configuration
-------------

`Built-in themes <http://sphinx-doc.org/theming.html>`_
^^^^^^^^^^^^^^^


- sphinx_rtd_theme -- mobile friendly theme, design for `readthedocs <http://docs.readthedocs.org/en/latest/>`_



Tips
----

- add ``?highlight=keywords`` at the end of url can **highlight** the keywords
- add ``id{num}`` after ``?highlight=keywords`` can goto reference line

Issues
------

1. ValueError: unknown locale: UTF-8 

| This error occurs in my **Macbook Air** (2011, OS X Yosemite)
|

.. code-block:: console

    # sphinx-build -b html -d build/doctrees source build/html
    Traceback (most recent call last):
      File "/usr/local/bin/sphinx-build", line 11, in <module>
        sys.exit(main())
      File "/Library/Python/2.7/site-packages/sphinx/__init__.py", line 51, in main
        sys.exit(build_main(argv))
      File "/Library/Python/2.7/site-packages/sphinx/__init__.py", line 61, in build_main
        from sphinx import cmdline
      File "/Library/Python/2.7/site-packages/sphinx/cmdline.py", line 19, in <module>
        from docutils.utils import SystemMessage
      File "/Library/Python/2.7/site-packages/docutils/utils/__init__.py", line 20, in <module>
        import docutils.io
      File "/Library/Python/2.7/site-packages/docutils/io.py", line 18, in <module>
        from docutils.utils.error_reporting import locale_encoding, ErrorString, ErrorOutput
      File "/Library/Python/2.7/site-packages/docutils/utils/error_reporting.py", line 47, in <module>
        locale_encoding = locale.getlocale()[1] or locale.getdefaultlocale()[1]
      File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/locale.py", line 511, in getdefaultlocale
        return _parse_localename(localename)
      File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/locale.py", line 443, in _parse_localename
        raise ValueError, 'unknown locale: %s' % localename

| **Solution**
|

.. code-block:: shell
    :linenos:

    export LC_ALL=es_ES.UTF-8
    export LANG=es_ES.UTF-8

2. avoid loading intersphinx inventory
    

`Pandoc <http://pandoc.org>`_ - Universal document converter
=================================================================================

`Download <https://github.com/jgm/pandoc/releases>`_

Useage:

.. code-block:: shell
    :linenos:

    # this command will transfer srcfile into dstfile according to suffix
    pandoc srcfile -o dstfile.suffix
One pic you can see how powerful it is.

.. image:: images/pandoc.jpg
