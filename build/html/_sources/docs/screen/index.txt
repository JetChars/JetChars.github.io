===================================
Screen - Full-screen window manager
===================================

It's useful tool for multi terminal management, process within screen will not be killed even ssh session closed.

* If you find dotted lines surround a window, which indicates this window is now been viewed by other client who has smaller screen resolution


Command List
============

Commands out of screen
----------------------

============== ======================================================
options        descriptions
============== ======================================================
-d             detach screen elsewhere
-d -m          start a screen in detached mode
-r             reattach here
-S sessionname name the new session
-x             attach to a not detached screen(multi display mode)
-ls            show screen list under current user
-t title       set title
-X             send the specified command to a running screen session
============== ======================================================


Commands inside screen
----------------------
these commands start with ``screen -S session_name [-p window_name] -X``

=========== ===================================
options     descriptions
=========== ===================================
hardstatus  customize hardstatus on each window
quit        quit session
stuff       simulate keyboard input
sessionname change session name
=========== ===================================



**Examples :**

.. code-block:: shell
    :linenos:

    # create an session named dstat
    screen -S dstat -d -m
    # change screen dstat's hardstatus
    screen -S dstat -X hardstatus alwayslastline '%{= .} %-Lw%{= .}%> %n%f %t*%{= .}%+Lw%< %-=%{g}(%{d}%H/%l%{g})'
    screen -S dstat -p $host-dstat -X stuff "ssh $host dstat -tam --output ~/$host-dstat-$timestamp.csv | tee $logpath/$host-dstat-$timestamp.log"
    # `echo -ne '\015'` equivalent to **Enter key**
    screen -S dstat -p $host-dstat -X stuff `echo -ne '\015'`
    # or you can store **Enter key**
    NL = `echo -ne '\015'`
    screen -S dstat -X screen -t window_name
    screen -S dstat -p window_name -X stuff "shell cmds $NL" 

Shortcuts Keys
==============

It start with ^a (^ is short for ctrl)

========== ==================================================================================
combos      descriptions
========== ==================================================================================
d          detach
s          split screen  (TAB -- tranfer between screens)
c/n/p/k    create/next/previous/kill window  (kill the only window will kill the session too)
\" / \'    select window from list / by index
A          change window's name
^a         previous window viewed
\\ or ^\\  quit session (close all windows)
[/]        edit mode, press space bar to start select, press again to complete copy; paste
?          help
========== ==================================================================================

Configuration Files
===================

Screen will first search ``~/.screenrc`` then ``/etc/screenrc``

We can customize our own status bar by adding this to conf file ::

    caption always '%{=b cw}%-w%{=rb db}%>%n %t%{-}%+w%{-b}%< %{= kG}%-=%D %c%{-}'
    shelltitle '$ |bash'
