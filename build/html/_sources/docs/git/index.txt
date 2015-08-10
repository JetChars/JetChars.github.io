============================================
`Git <http://git-scm.com>`_ -- Extraordinary version contrl software
============================================

`Interactive Tutorial <https://try.github.io/levels/1/challenges/1>`_

* CVS/SVN(SubVersion) both need need web connection, while git don't


`Official Doc <http://git-scm.com/doc>`_



Configuration
=============

Config -- Get and set repository or global options
--------------------------------------------------

`git-congfig guide <https://www.kernel.org/pub/software/scm/git/docs/git-config.html>`_

``git config --global section_name.param value``

::

    git config --global user.email "calebjay@live.cn"
    git config --global user.name "JetChars"
    git config --list   # check git configuration

- global configuration: ``~/.gitconfig`` , ini format. (``/etc/gitconfig`` for all user)
- On Windows, Git stores its configuration file ``.gitconfig`` in the directory ``%HOMEDRIVE%%HOMEPATH%`` 
    - eg: ``C:\Users\Jet\.gitconfig``

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
    [push]
        default = simple



* Project configuration: 
    * ``.git/config`` storage project info, ``url = http://username:passwd@url.git`` can help avoid passwd input
    * ``.gitignore`` store files exclude from project.
    * ``push.default`` specifies push mode
        * matching mode -- git will push local branches to the remote branches that already exist with same name
        * simple mode -- only pushes the current branch to the corresponding remote branch that 'git pull' uses to update the current branch

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


Repository Management
=====================

Clone -- Clone a repository into a new directory
------------------------------------------------

::

    git clone [-o <name>] [uname:passwd@]<repository> [<directory>]

git supports various of scheme::

    git clone http[s]://example.com/path/to/repo.git/
    git clone ssh://example.com/path/to/repo.git/
    git clone git://example.com/path/to/repo.git/
    git clone /opt/git/project.git 
    git clone file:///opt/git/project.git
    git clone ftp[s]://example.com/path/to/repo.git/
    git clone rsync://example.com/path/to/repo.git/

Remote -- Manage set of tracked repositories
--------------------------------------------

.. code-block:: bash

    git remote show <host>
    git remote add <host> <addr>
    git remote rm <host>
    git remote rename <old_host> <new_host>



Branch Management
=================


Branch -- List, create, or delete branches
------------------------------------------

.. code-block:: bash

    git branch  # show local branch info when no option selected
    git branch <branchname> [<start-point>]  # copy start point into a new branch, default is current branch


====== =====================
option description
====== =====================
-a     List both remote-tracking branches and local branches
-r     List or delete (if used with -d) the remote-tracking branches
-d     delete a branch
====== =====================

Merge -- Join two or more development histories together
--------------------------------------------------------

.. code-block:: bash

    git merge anotherbanch  # merge another branch into current branch


Checkout -- Checkout a branch or paths to the working tree
----------------------------------------------------------

.. code-block:: bash

    git checkout   # show current stat, M means changes brought from old branch
    git checkout -  # switch to previous branch




Submit
======

Add/rm -- Add file contents to the index (stage files)
------------------------------------------------------

.. code-block:: bash

    git add -A  # can replaced w/ --all, stage all changes, include removed files
    git add '*.txt'  # remove all files have suffix .txt, within this project

Reset -- Reset current HEAD to the specified state (unstage files)
------------------------------------------------------------------

.. code-block:: bash

    git reset [-q] [<tree-ish>] [--] <paths>...
    git reset (--patch | -p) [<tree-ish>] [--] [<paths>...]
    git reset [--soft | --mixed | --hard | --merge | --keep] [-q] [<commit>]

======== ======================
options  descripton
======== ======================
hard     Resets the index and working tree
soft     This leaves all your changed files "Changes to be committed"
mixed    Resets the index but not the working tree (keep changed codes)
======== ======================


.. code-block:: bash

   git reset filename  # unstage a file


Commit -- Record changes to the repository

.. code-block:: bash

    git commit -am 'commit message'  # -a means stage all changed files, but not new file
    git commit --amend -m "New commit message"  # change commit message

Push -- Update remote refs along with associated objects
--------------------------------------------------------


.. code-block:: bash

    git push  # submit code to default server
    git push --set-upstream origin wenjie  # update branch bind info
    git push origin branch-name  # add upstream reference


Review -- The tool to submit code patches
-----------------------------------------


Rebase -- Forward-port local commits to the updated upstream head
-----------------------------------------------------------------






Check Infos
===========

.. sidebar:: Note

    | **HEAD** -- latest commit
    | **HEAD^** -- commit before latest one

.. code-block:: bash

    git status -sb  # 's' means shot output, 'b' shows branch info
    git log  # show commit log
    git diff  # show changes between commits
    git diff HEAD  # show recent changes
    git diff --staged  # show local changes



Init a project
==============

.. code-block:: bash

    echo "# myho" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin https://github.com/JetChars/myho.git
    git push -u origin master  # -u tells git to remember the parameters







