========================
Linux Automizaiton Tools
========================

Puppet
======
======


chef
====
====




SaltStack
=========
=========

SaltStack is brand new automization management tool, used to manage configurations and exec cmds remotely.
- every config file in YAML format
- config files -- ``/etc/salt/``
    - ``/etc/salt/master`` -- interface(listening IP), auto_accept(True, will reduce the key adding work)
- log files -- ``/var/log/salt/``
- comm w/ zeromq's pub-sub&req-rep mode, conn w/ tcp and ipc

Master and Minion
-----------------

- minino will create ``/etc/salt/pki/minion/minion.{pem,pub}`` when first started. then send ``pub`` file to master
- after accept the ``pub`` key from minion, master should use cmd ``salt-key -a <minion>`` to accept this key. then put this key under ``/etc/salt/pki/master/minions``
- master will use port 4505 and 4506 -- 4505 will keep conn w/ minions



.. code-block:: shell

    # install and start the salt master
    # =================================
    apt-get install salt-master -y
    salt-master -l debug
    salt-master -d
    salt-master status
    salt-master restart --log-level=debug

    # install and  start minion
    # =========================
    apt-get install salt-minion -y
    salt-minion -l debug
    salt-minion -d

    # key management
    # ==============
    salt-key -a <minion>
    salt-key -L

    # test
    # ====
    salt '*' cmd.run ls        # run ls in all minion
    salt <minion> test.ping    # built-in script, will report OK if pingable




