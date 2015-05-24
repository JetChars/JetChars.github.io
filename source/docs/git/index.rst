============================================
`Git <http://git-scm.com>`_ -- Extraordinary version contrl software
============================================

`Interactive Tutorial <https://try.github.io/levels/1/challenges/1>`_

* CVS/SVN(SubVersion) both need need web connection, while git don't

Git Proxy Command
-----------------

| Git need extra configuration for url with “git://” scheme. Configure proxy command with netcat (/usr/bin/git-proxy) and add its link to the environment. 
|
::

    $ export GIT_PROXY_COMMAND=/usr/bin/git-proxy

| Create the file ``/usr/bin/git-proxy``
|

.. code-block:: shell
    :linenos:

    # create proxy script
    cat >> /usr/bin/git-proxy << EOF
    #!/bin/sh
    case $1 in
        *.intel.com|192.168.*|127.0.*|localhost|10.*)
            METHOD="-X connect"
        ;;
        *)
            METHOD="-X 5 -x proxy-shz.intel.com:1080"
        ;;
    esac
    /bin/nc.openbsd $METHOD $*
    EOF
    
    # make it executable
    chmod +x /usr/bin/git-proxy

    # let git know it
    cat >> /etc/gitconfig << EOF
    [core]
    gitproxy=/usr/bin/git-proxy
    EOF
