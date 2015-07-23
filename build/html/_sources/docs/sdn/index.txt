========================
Software-Defined Network
========================


ONF
===


`Open Networking Foundation (ONF) <https://www.opennetworking.org/index.php>`_ is a nonprofit, mutually beneficial trade organization, funded by prominent companies such as Deutsche Telekom, Facebook, Google, Microsoft, Verizon, and Yahoo! 
aimed at improving networking through **software-defined networking** (SDN) and standardizing the **OpenFlow protocol** and **related technologies**. [#]_
The standards-setting and SDN-promotion group was formed out of recognition that cloud computing will blur the distinctions between computers and networks. [#]_
By June 2014 ONF had grown to over 150 member companies including 24 start-up companies in Software Defined Networking

- 2008 -- ONF releases OpenFlow (Standford University) and NOX (Nicira)
- 2012 -- Google's system-wide adoption of ONF's OpenFlow softwared



SDN
===

The physical separation of the network control plane from the forwarding plane, and where a control plane controls several devices. [#]_


Components
----------

Two different kind of nodes: core/edge.

- Concept borrowed from MPLS. 
- Core: Transport packets among edge nodes.
- Edges: nodes connected to hosts. 
    - Edge nodes became Software Edges.
    - SDN Controller need to talk only to edge nodes.
    - Actually part of the SDN work can be done by the software edges.
- All functionalities can be moved to edges while core can focus on transport.





OpenFlow
========

The OpenFlow™ protocol is a foundational element for building SDN solutions.




Open vSwitch
============

.. image:: images/2host-4vm-2nic-tunnel.png


.. [#] http://archive.openflow.org/wp/2011/03/open-networking-foundation-formed-to-speed-network-innovation/
.. [#] http://www.nytimes.com/2011/03/22/technology/internet/22internet.html
.. [#] https://www.opennetworking.org/sdn-resources/sdn-definition