=====
Shell
=====



Variables
=========

Parameter Expansion
-------------------

expansion operators
^^^^^^^^^^^^^^^^^^^

- substitute operator

==================== ========================
operator             substitute
==================== ========================
${varname:-word}     if null, return word
${varname:=word}     if null, set word to varname, then return word
${varname:+word}     if not null, return word
${varname:?message}  if null, print message then exit
==================== ========================


- pattern matching mode

positional parameter
^^^^^^^^^^^^^^^^^^^^

special parameter
^^^^^^^^^^^^^^^^^

Arithmetic Expansion
--------------------

No need of escape charactor

=================== =============================  ========
operator            description                    sequence
=================== =============================  ========
++ --               auto add/minus                 LR
\+ \- ! ~           unary +/- , AND/OPPISITE       RL
=================== =============================  ========





Shell at windows
================


xshell
------



`cygwin <https://www.cygwin.com/>`_
-----------------------------------



.. code-block:: bash

    cygrunsrv -h
    cygrunsrv -S sshd   # same as ``net start sshd``




config sshd
^^^^^^^^^^^

- before running sshd at windows, cygwin need run as admin for sshd configuration.


.. code-block:: console
    :linenos:
    :emphasize-lines: 4,6,18,26,30,31,56

    $ ssh-host-config

    *** Info: Generating missing SSH host keys
    *** Query: Overwrite existing /etc/ssh_config file? (yes/no) yes
    *** Info: Creating default /etc/ssh_config file
    *** Query: Overwrite existing /etc/sshd_config file? (yes/no) yes
    *** Info: Creating default /etc/sshd_config file

    *** Info: StrictModes is set to 'yes' by default.
    *** Info: This is the recommended setting, but it requires that the POSIX
    *** Info: permissions of the user's home directory, the user's .ssh
    *** Info: directory, and the user's ssh key files are tight so that
    *** Info: only the user has write permissions.
    *** Info: On the other hand, StrictModes don't work well with default
    *** Info: Windows permissions of a home directory mounted with the
    *** Info: 'noacl' option, and they don't work at all if the home
    *** Info: directory is on a FAT or FAT32 partition.
    *** Query: Should StrictModes be used? (yes/no) no

    *** Info: Privilege separation is set to 'sandbox' by default since
    *** Info: OpenSSH 6.1.  This is unsupported by Cygwin and has to be set
    *** Info: to 'yes' or 'no'.
    *** Info: However, using privilege separation requires a non-privileged account
    *** Info: called 'sshd'.
    *** Info: For more info on privilege separation read /usr/share/doc/openssh/README.privsep.
    *** Query: Should privilege separation be used? (yes/no) no
    *** Info: Updating /etc/sshd_config file

    *** Query: Do you want to install sshd as a service?
    *** Query: (Say "no" if it is already installed as a service) (yes/no) yes
    *** Query: Enter the value of CYGWIN for the daemon: [] binmode ntsec
    *** Info: On Windows Server 2003, Windows Vista, and above, the
    *** Info: SYSTEM account cannot setuid to other users -- a capability
    *** Info: sshd requires.  You need to have or to create a privileged
    *** Info: account.  This script will help you do so.

    *** Info: It's not possible to use the LocalSystem account for services
    *** Info: that can change the user id without an explicit password
    *** Info: (such as passwordless logins [e.g. public key authentication]
    *** Info: via sshd) when having to create the user token from scratch.
    *** Info: For more information on this requirement, see
    *** Info: https://cygwin.com/cygwin-ug-net/ntsec.html#ntsec-nopasswd1

    *** Info: If you want to enable that functionality, it's required to create
    *** Info: a new account with special privileges (unless such an account
    *** Info: already exists). This account is then used to run these special
    *** Info: servers.

    *** Info: Note that creating a new user requires that the current account
    *** Info: have Administrator privileges itself.

    *** Info: No privileged account could be found.

    *** Info: This script plans to use 'cyg_server'.
    *** Info: 'cyg_server' will only be used by registered services.
    *** Query: Do you want to use a different name? (yes/no) yes
    *** Query: Enter the new user name: root
    *** Query: Reenter: root

    *** Query: Create new privileged user account 'WENJIECA-MOBL1\root' (Cygwin name: 'wenjieca-mobl1+root')? (yes/no) yes
    *** Info: Please enter a password for new user wenjieca-mobl1+root.  Please be sure
    *** Info: that this password matches the password rules given on your system.
    *** Info: Entering no password will exit the configuration.
    *** Query: Please enter the password:
    *** Query: Reenter:

    *** Info: User 'wenjieca-mobl1+root' has been created with password 'Calebjay@12'.
    *** Info: If you change the password, please remember also to change the
    *** Info: password for the installed services which use (or will soon use)
    *** Info: the 'wenjieca-mobl1+root' account.


    *** Info: The sshd service has been installed under the 'wenjieca-mobl1+root'
    *** Info: account.  To start the service now, call `net start sshd' or
    *** Info: `cygrunsrv -S sshd'.  Otherwise, it will start automatically
    *** Info: after the next reboot.

    *** Info: Host configuration finished. Have fun!

