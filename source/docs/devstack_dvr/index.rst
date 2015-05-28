
========================
Enable DVR with DevStack
========================

| DVR is short for distributed virtual router, with this feature enabled packets flow with floating IP will no longer send to network node. It helps to alleviate network node's pressure greatly when large amount of north-south data flow occurs. [#]_
| But, SNAT packets still need 
|



Brief Intro
===========

| In order to enable distributed router on each compute-node, Neutron-metadata-agent and Neutron-L3-agent are both needed. So we need to add **q-meta** and **q-l3** as well as *q-agt* on each computer node's ``local.conf`` file. 
|

.. image:: images/image1.png

.. warning:: Currently devstack doesn't support deploying DVR on GRE tunnel [#]_ , and tunnel type has been hard coded to vxlan mode, the following is a part of devstack's code ``lib/neutron_plugins/ml2``:

.. image:: images/image2.png

| With DVR, floating IPs can be accessed directly from each compute node, but SNAT still need to be centralized to network node.
|

.. image:: images/image3.png




Configure Network Node
======================

| Here's the neutron configuration part of ``local.conf`` on network node.
|

.. code-block:: shell
    :linenos:
    :emphasize-lines: 16-18

    # Neutron-vxlan-tunnel-DVR
    ##########################
    ENABLED_SERVICES+=,q-svc,q-agt,q-dhcp,q-l3,q-meta,neutron
    Q_FLOATING_ALLOCATION_POOL=start=192.168.137.166,end=192.168.137.253
    Q_ROUTER_NAME=default_router
    PUBLIC_NETWORK_GATEWAY=192.168.137.254
    FLOATING_RANGE=192.168.0.0/16
    
    FIXED_RANGE=10.1.1.0/24
    FIXED_NETWORK_SIZE=256
    NETWORK_GATEWAY=10.1.1.1
    
    Q_PLUGIN=ml2
    Q_ML2_TENANT_NETWORK_TYPE=vxlan
    TUNNEL_ENDPOINT_IP=192.168.1.37
    Q_DVR_MODE=dvr_snat
    Q_SERVICE_PLUGIN_CLASSES=neutron.services.l3_router.l3_router_plugin.L3RouterPlugin
    Q_ML2_PLUGIN_MECHANISM_DRIVERS=openvswitch,linuxbridge,l2population

.. note:: DVR mode can be **dvr_snat** , **dvr** or **legacy**. *Legacy* is Q_DVR_MODE 's default value, *dvr_snat* is for network node which enables snat router, and *dvr* mode is for compute node. 

| **L2population** is needed by DVR. The L2 Population driver enables broadcast, multicast, and unicast traffic to scale out on large overlay networks. This traffic is sent to the relevant agent via encapsulation as a targeted unicast. [#]_
|

.. image:: images/image4.png

| After Installation you might see 3 bridges and 4 namespaces on network node.
|

.. image:: images/image5.png

.. image:: images/image6.png

| Namespace fip* is for floating IP accessing. qdhcp* is for allocating IP addresses. snat* is for SNAT function. qrouter* only serves VM in current host.
|



Configure Compute Node
======================

| The following is the neutron configuration part of ``local.conf`` on compute node
|

.. code-block:: shell
    :linenos:
    :emphasize-lines: 7-9

    # Neutron-vxlan-tunnel-DVR
    ##########################
    ENABLED_SERVICES+= q-agt,q-l3,q-meta, neutron
    Q_PLUGIN=ml2
    Q_ML2_TENANT_NETWORK_TYPE=vxlan
    TUNNEL_ENDPOINT_IP=192.168.1.34
    Q_DVR_MODE=dvr
    Q_SERVICE_PLUGIN_CLASSES=neutron.services.l3_router.l3_router_plugin.L3RouterPlugin
    Q_ML2_PLUGIN_MECHANISM_DRIVERS=openvswitch,linuxbridge,l2population


| After installation you might see 3 bridges and 2 namespaces.
|

.. image:: images/image7.png

.. image:: images/image8.png

| fip* and qrouter* did the same job as two virtual devices on network node.
| We still need to do some configurations manually.
|

1. Add an free physical device(NIC) to br-ex

.. code-block:: shell

    $ sudo ovs-vsctl add-port br-ex eth1

2. Allocate an IP for br-ex as a gateway

.. code-block:: shell

    $ sudo ifconfig br-ex 192.168.137.253

3. Add a route to floating network via fip*

| Before we adding this route, we need to know fip's IP address.
|

.. image:: images/image9.png


| We use the IP on fg* . 
|

.. code-block:: shell

    $ sudo ip route add 192.168.0.0/16 via 192.168.137.171





.. [#] https://wiki.openstack.org/wiki/Neutron/DVR/HowTo
.. [#] https://blueprints.launchpad.net/neutron/+spec/neutron-ovs-dvr
.. [#] https://wiki.openstack.org/wiki/Neutron/DVR_L2_Agent
