======
psdash
======

psdash is a system information web dashboard for linux using data mainly served by psutil - hence the name

`Git Repo <https://github.com/Jahaja/psdash>`_

Configure psdash
================
================

psdash_help
-----------

+------------------------+------------------------------------------------------+
|option                  |description                                           |
+========================+======================================================+
|-h, --help              |show this help message and exit                       | 
+------------------------+------------------------------------------------------+
|-l path, --log path     |log files to make available for psdash. Patterns (e.g.|
|                        |/var/log/**/*.log) are supported. This option can be  |
|                        |used multiple times.                                  | 
+------------------------+------------------------------------------------------+
|-b host, --bind host    |host to bind to. Defaults to 0.0.0.0 (all interfaces).| 
+------------------------+------------------------------------------------------+
|-p port, --port port    |port to listen on. Defaults to 5000.                  | 
+------------------------+------------------------------------------------------+
|-d, --debug             |enables debug mode.                                   | 
+------------------------+------------------------------------------------------+
|-a, --agent             |Enables agent mode. This launches a RPC server, using |
|                        |zerorpc, on given bind host and port.                 |
+------------------------+------------------------------------------------------+
|--register-to host:port |The psdash node running in web mode to register this  |
|                        |agent to on start up. e.g 10.0.1.22:5000              |
+------------------------+------------------------------------------------------+
|--register-as name      |The name to register as. (This will default to the    | 
|                        |node's hostname)                                      |
+------------------------+------------------------------------------------------+


start the psdash master and slave
---------------------------------

.. code-block:: shell

    sudo pip install psdash                          # installation using pip

    sudo PSDASH_CONFIG=/home/jet/master_config.py \  # starting psdash
        psdash --log /var/log/psdash.log        
        -b 192.168.0.101 -p 5001

    sudo psdash -a \                                 # starting a pasash agent
        --register-to http://192.168.0.101:5001/my_psdash \
        --register-as FBSD-node



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


Use supervisord to maintain psdash
==================================
==================================

start the supervisord
---------------------

.. code-block:: shell

    pip install supervisor
    echo_supervisord_conf > /etc/supervisord.conf   # init the config file



supervisord config file
-----------------------

.. code-block:: guess

    [unix_http_server]
    file=/tmp/supervisor.sock
    
    [supervisord]
    logfile=/tmp/supervisord.log
    logfile_maxbytes=50MB       
    logfile_backups=10          
    loglevel=info               
    pidfile=/tmp/supervisord.pid
    nodaemon=false              
    minfds=1024                 
    minprocs=200                
    
    [rpcinterface:supervisor]
    supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
    
    [supervisorctl]
    serverurl=unix:///tmp/supervisor.sock
   
    [program:padash]
    command=sudo PSDASH_CONFIG=/home/jet/master_config.py psdash --log /var/log/psdash.log -b 192.168.0.101 -p 5001
    numprocs=1                   
    autostart=true               
    startsecs=2                  
    startretries=5               
    autorestart=unexpected       
    user=root                    
    stdout_logfile=/var/log/supervisord/stdout.log
    stdout_logfile_maxbytes=100MB
    stdout_logfile_backups=10     
    stdout_capture_maxbytes=1MB   
    stdout_events_enabled=true    
    stderr_logfile=/var/log/supervisord/stderr.log
    stderr_logfile_maxbytes=100MB
    stderr_logfile_backups=10    
    stderr_capture_maxbytes=1MB  
    stderr_events_enabled=true   


    
