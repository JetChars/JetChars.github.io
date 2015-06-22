====================================
`Hadoop <http://hadoop.apache.org>`_
====================================

`wiki <http://wiki.apache.org/hadoop/>`_

.. image:: images/hadoop_evolve.jpg

Unlimit Non-root User's Resources
=================================

.. code-block:: shell
    :linenos:

    sudo rm -rf /etc/security/limits.d
    sudo cat >> /etc/security/limits.conf << EOF
    *                -       nproc           100000
    *                -       nofile          100000
    *                -       memlock         unlimited
    EOF



crunch
======

`CDAP <http://cdap.io>`_
========================


Issues
======

::
    
    15/06/16 14:59:24 INFO ipc.Client: Retrying connect to server: localhost/127.0.0.1:54645. Already tried 0 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=3, sleepTime=1000 MILLISECONDS)
    15/06/16 14:59:25 INFO ipc.Client: Retrying connect to server: localhost/127.0.0.1:54645. Already tried 1 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=3, sleepTime=1000 MILLISECONDS)
    15/06/16 14:59:26 INFO ipc.Client: Retrying connect to server: localhost/127.0.0.1:54645. Already tried 2 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=3, sleepTime=1000 MILLISECONDS)



.. code-block:: bash
    :linenos:

    lsof -i   # see which version ip protocol uses


