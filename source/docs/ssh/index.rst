============
Secure Shell
============



- config files:
    - ``~/.ssh/config``
    - /etc/ssh/ssh_config
        - StrictHostKeyChecking no

**Example ~/.ssh/config** :

.. code-block:: guess

    Host    alias
        HostName        ipaddr
        Port            port
        User            username
        IdentityFile    keypath

**Example ssh_config** :

.. code-block:: guess

    # abandon yes/no prompt
    StrictHostKeyChecking no



3 most powerful ssh tunnel
--------------------------

.. code-block:: bash
    
    ssh -C -f -N -g -L listen_port:DST_Host:DST_port user@Tunnel_Host 
    ssh -C -f -N -g -R listen_port:DST_Host:DST_port user@Tunnel_Host 
    ssh -C -f -N -g -D listen_port user@Tunnel_Host
