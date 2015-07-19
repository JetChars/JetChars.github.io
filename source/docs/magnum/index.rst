======
Magnum
======

Magnum is an OpenStack project which offers container orchestration engines for deploying and managing containers as first class resources in OpenStack.[#]_




- Bay: A collection of node objects where work is scheduled
- BayModel: An object stores template information about the bay which is used to create new bays consistently
- Node: A baremetal or virtual machine where work executes
- Pod: A collection of containers running on one physical or virtual machine
- Service: An abstraction which defines a logical set of pods and a policy by which to access them
- ReplicationController: An abstraction for managing a group of pods to ensure a specified number of resources are running
- Container: A Docker container



.. code-block:: bash
    :linenos:

    # Configure
    # ---------
    ADMIN_PASSWORD=123456

    # Get Admin Credit
    # ----------------
    source ~/devstack/openrc admin admin
    # Magnum has been tested with the Fedora Atomic micro-OS and CoreOS. Magnum will likely work with other micro-OS platforms, but each requires individual support in the heat template.
    # Store the Fedora Atomic micro-OS in glance. (The steps for updating Fedora Atomic images are a bit detailed. Fortunately one of the core developers has made Atomic images available at https://fedorapeople.org/groups/magnum):
    
    cd ~
    wget https://fedorapeople.org/groups/magnum/fedora-21-atomic-3.qcow2
    glance image-create --name fedora-21-atomic-3 \
                        --is-public True \
                        --disk-format qcow2 \
                        --property os_distro='fedora-atomic'\
                        --container-format bare < fedora-21-atomic-3.qcow2

    # Create a keypair for use with the baymodel:
    # -------------------------------------------    
    test -f ~/.ssh/id_rsa.pub || ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
    nova keypair-add --pub-key ~/.ssh/id_rsa.pub testkey

    # Create a database in MySQL for magnum:
    # --------------------------------------    
    mysql -h 127.0.0.1 -u root -p$ADMIN_PASSWORD mysql <<EOF
    CREATE DATABASE IF NOT EXISTS magnum DEFAULT CHARACTER SET utf8;
    GRANT ALL PRIVILEGES ON magnum.* TO
        'root'@'%' IDENTIFIED BY "$ADMIN_PASSWORD"
    EOF

    # Clone and install magnum:
    # -------------------------
    cd ~
    git clone https://git.openstack.org/openstack/magnum
    cd magnum
    git checkout stable/kilo   # should use same branch as current openstack
    sudo -E pip install -e .

    # Configure magnum:
    # -----------------
    sudo mkdir -p /etc/magnum   # create the magnum conf directory
    sudo cp etc/magnum/magnum.conf.sample /etc/magnum/magnum.conf   # copy sample config and modify it as necessary
    sudo sed -i "s/#debug\s*=.*/debug=true/" /etc/magnum/magnum.conf   # enable debugging output
    sudo sed -i "s/#verbose\s*=.*/verbose=true/" /etc/magnum/magnum.conf   # enable more verbose output
    sudo sed -i "s/#rabbit_userid\s*=.*/rabbit_userid=stackrabbit/" \
             /etc/magnum/magnum.conf   # set RabbitMQ userid
    sudo sed -i "s/#rabbit_password\s*=.*/rabbit_password=$ADMIN_PASSWORD/" \
             /etc/magnum/magnum.conf   # set RabbitMQ password
    sudo sed -i "s/#connection\s*=.*/connection=mysql:\/\/root:$ADMIN_PASSWORD@localhost\/magnum/" \
             /etc/magnum/magnum.conf   # set SQLAlchemy connection string to connect to MySQL
    sudo sed -i "s/#admin_user\s*=.*/admin_user=admin/" \
             /etc/magnum/magnum.conf   # set Keystone account username
    sudo sed -i "s/#admin_password\s*=.*/admin_password=$ADMIN_PASSWORD/" \
             /etc/magnum/magnum.conf   # set Keystone account password
    sudo sed -i "s/#identity_uri\s*=.*/identity_uri=http:\/\/127.0.0.1:35357/" \
             /etc/magnum/magnum.conf   # set admin Identity API endpoint
    sudo sed -i "s/#auth_uri\s*=.*/auth_uri=http:\/\/127.0.0.1:5000\/v2.0/" \
             /etc/magnum/magnum.conf   # set public Identity API endpoint

    # Clone and install the magnum client:
    # ------------------------------------
    cd ~
    git clone https://git.openstack.org/openstack/python-magnumclient
    cd python-magnumclient
    git checkout stable/kilo   # should use same branch as current openstack
    sudo -E pip install -e .

    # Configure the database for use with magnum:
    # -------------------------------------------
    magnum-db-manage upgrade

    # Configure the keystone endpoint:
    # --------------------------------
    keystone service-create --name=magnum \
                            --type=container \
                            --description="magnum Container Service"
    keystone endpoint-create --service=magnum \
                             --publicurl=http://127.0.0.1:9511/v1 \
                             --internalurl=http://127.0.0.1:9511/v1 \
                             --adminurl=http://127.0.0.1:9511/v1 \
                             --region RegionOne



.. [#] http://docs.openstack.org/developer/magnum/index.html
