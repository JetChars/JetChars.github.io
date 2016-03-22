===================
Python Applications
===================

pip
===

`get-pip.py <https://bootstrap.pypa.io/get-pip.py>`_


flask -- py based web framework
===============================


http://flask.pocoo.org/

sphinx
======

http://sphinx-doc.org/latest/index.html


fabric
======

http://www.fabfile.org/

http://docs.fabfile.org/en/1.8/

Fabric is a Python (2.5-2.7) library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks.

- write default script ``fabfile.py``, other scripts should use ``-f <fname>``

.. code-block:: python

    def hello():
        print "hello world!"

    def nv(name, value)
        print "%s = %s!" % (name, value)


.. code-block:: console

    $ fab -f test.py hello
    hello world!

    Done.
    $ fab -f test.py nv:name=age,value=20
    age = 20!

    Done.
    $ fab -f test.py nv:age,20
    age = 20!

    Done.


.. code-block:: python

    from fabric.api import local, lcd

    def lsfab():
        with lcd('~/tmp/fab'):
            local('ls')


.. code-block:: console

    $ fab -f test.py lsfab
    [localhost] local: cd ~/tmp/fab
    [localhost] local: ls
    fabfile.py  fabfile.pyc test.py     test.pyc

    Done.


- exec cmds remotely w/ ``run()``

.. code-block:: python

    from fabric.api import *


    env.hosts = ['root@192.168.56.111:22']
    env.password = '6666'


    def date():
        with cd('~'):
            run('whoami')
            run('date')

.. code-block:: console

    $  fab -f cmgt.py date
    [root@192.168.56.111:22] Executing task 'date'
    [root@192.168.56.111:22] run: whoami
    [root@192.168.56.111:22] out: root
    [root@192.168.56.111:22] out:

    [root@192.168.56.111:22] run: date
    [root@192.168.56.111:22] out: 2016年 03月 22日 星期二 09:54:59 CST
    [root@192.168.56.111:22] out:


    Done.
    Disconnecting from root@192.168.56.111... done.





virtualenv
==========


