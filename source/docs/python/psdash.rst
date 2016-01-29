======
psdash
======

`Git Repo <https://github.com/Jahaja/psdash>`

Install psdash
==============

start the psdash master and slave
---------------------------------

.. code-block:: bash

    sudo pip install psdash                          # installation using pip

    sudo PSDASH_CONFIG=/home/jet/master_config.py \  # starting psdash
        psdash --log /var/log/psdash.log        

    sudo psdash -a \                                 # starting a pasash agent
        --register-to http://192.168.0.101:5000/my_psdash \
        --register-as FBSD-node

.. side-bar::

    *------------------------*------------------------------------------------------*
    |option                  |description                                           |
    *========================*======================================================*
    |-h, --help              |show this help message and exit                       | 
    *------------------------*------------------------------------------------------*
    |-l path, --log path     |log files to make available for psdash. Patterns (e.g.|
    |                        |/var/log/**/*.log) are supported. This option can be  |
    |                        |used multiple times.                                  | 
    *------------------------*------------------------------------------------------*
    |-b host, --bind host    |host to bind to. Defaults to 0.0.0.0 (all interfaces).| 
    *------------------------*------------------------------------------------------*
    |-p port, --port port    |port to listen on. Defaults to 5000.                  | 
    *------------------------*------------------------------------------------------*
    |-d, --debug             |enables debug mode.                                   | 
    *------------------------*------------------------------------------------------*
    |-a, --agent             |Enables agent mode. This launches a RPC server, using |
    |                        |zerorpc, on given bind host and port.                 |
    *------------------------*------------------------------------------------------*
    |--register-to host:port |The psdash node running in web mode to register this  |
    |                        |agent to on start up. e.g 10.0.1.22:5000              |
    *------------------------*------------------------------------------------------*
    |--register-as name      |The name to register as. (This will default to the    | 
    |                        |node's hostname)                                      |
    *------------------------*------------------------------------------------------*


master node's config file
-------------------------

.. code-block:: python

    #PSDASH_AUTH_USERNAME = "jet"
    #PSDASH_AUTH_PASSWORD = "6666"
    PSDASH_ALLOWED_REMOTE_ADDRESSES = "127.0.0.1 192.168.0.102"
    PSDASH_URL_PREFIX = "/my_psdash"
    PSDASH_NODES = [{'name': 'fbsd_node', 'host': '192.168.0.102', 'port': 5000}]
    PSDASH_NET_IO_COUNTER_INTERVAL = 1
    PSDASH_LOGS_INTERVAL = 30
    PSDASH_REGISTER_INTERVAL = 30
    PSDASH_LOGS = ['/var/log/psdash_*.log']


slave node's config file
------------------------

.. code-block:: python

    
