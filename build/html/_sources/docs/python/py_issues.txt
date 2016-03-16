=============
Python Issues
=============


This chapter will include issue around python


Install python modules
======================




Python.h No such file or directory
----------------------------------

.. code-block:: console

    psutil/_psutil_linux.c:12:20: fatal error: Python.h: No such file or directory
    
     #include <Python.h>
    
                        ^
    
    compilation terminated.
    
    error: command 'x86_64-linux-gnu-gcc' failed with exit status 1



- solution -- install ``python-dev`` or ``python-devel`` w/ apt-get or yum



