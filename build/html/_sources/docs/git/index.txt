============================================
`Git <http://git-scm.com>`_ -- Extraordinary version contrl software
============================================

`Interactive Tutorial <https://try.github.io/levels/1/challenges/1>`_

* CVS/SVN(SubVersion) both need need web connection, while git don't


Configuration
=============

git_config
----------

``git config --global section_name.param value``

::

    git config --global user.email "calebjay@live.cn"
    git config --global user.name "JetChars"
    git config --list   # check git configuration

* global configuration: ``~/.gitconfig`` , ini format. (``/etc/gitconfig`` for all user)

.. code-block:: ini
    :linenos:

    [core]
        gitproxy = /usr/bin/git-proxy
    [http]
        proxy = http://proxy-shz.intel.com:911
        sslverify = false
    [user]
    	name = JetChars
    	email = calebjay@live.cn
    [alias]
    	df = diff
    	st = status
    	co = checkout
    	ci = commit
    	br = branch
    	last = log -3
    	lg = log --color --graph --abbrev-commit --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s%Cgreen(%cr) %C(bold blue)<%an>%Creset'
    [filter "lfs"]
    	clean = git lfs clean %f
    	smudge = git lfs smudge %f
    	required = true
    [gitreview]
        username = gerrit_user_name
        scheme = https
        port = 443




* Project configuration: 
    * ``.git/config`` storage project info, ``url = http://username:passwd@url.git`` can help avoid passwd input
    * ``.gitignore`` store files exclude from project.


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

