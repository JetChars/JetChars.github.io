==================
OpenStack & Docker
==================


Docker can work in different ways at openstack, eg: nova-docker, kubernetes, ...



Nova Docker
===========

nstall docker&nova-docker
--------------------------

.. code-block:: bash

    usermod -G docker nova
    pip install -e git+https://github.com/stackforge/nova-docker#egg=novadocker
    cd src/novadocker/
    python setup.py install

Install latest docker
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    curl -sSL http://get.docker.com | sh
    systemctl start docker
    systemctl enable docker
    # test whether docker is available
    docker run -it busybox



Prepare Nova-Docker
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    sudo apt-get update
    sudo apt-get install -y python-pip python-dev
    
    rm -rf /opt/stack/nova-docker
    sudo mkdir -p /opt/stack
    sudo git clone https://git.openstack.org/stackforge/nova-docker /opt/stack/nova-docker
    cd /opt/stack/nova-docker
    # Check out a different version if not using master, i.e:
    # sudo git checkout stable/kilo && sudo git pull --ff-only origin stable/kilo
    sudo pip install .  # The linecache2 error appears to be benign



Config local.conf
^^^^^^^^^^^^^^^^^

.. code-block:: ini

    [[local|localrc]]
    VIRT_DRIVER=novadocker.virt.docker.DockerDriver
    
    
    [[post-config|$NOVA_CONF]]
    [DEFAULT]
    compute_driver=novadocker.virt.docker.DockerDriver
    

    [[post-config|$GLANCE_API_CONF]]
    [DEFAULT]
    container_formats=ami,ari,aki,bare,ovf,ova,docker


Testing Nova-Docker
-------------------

copy the fileter
^^^^^^^^^^^^^^^^

.. code-block:: bash

    sudo cp novadocker/etc/nova/rootwrap.d/docker.filters /etc/nova/rootwrap.d/


start a Container
^^^^^^^^^^^^^^^^^

.. code-block:: bash

    . openrc admin

    INSTANCE=d1
    IMAGE=cirros
    
    docker pull cirros
    docker save cirros |
        glance image-create --name ${IMAGE} --is-public true \
        --container-format docker --disk-format raw
    
    nova boot --image ${IMAGE} --flavor m1.tiny ${INSTANCE}
    sleep 10
    nova list
    nova show ${INSTANCE}


