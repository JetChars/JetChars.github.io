=========================================
AMQP -- Advanced Message Queuing Protocol
=========================================

- binary application layer protocol
- Asynchronos communiction between processes, 松耦合性, managed by a middle ware, no need to know the location of other nodes.
- message format -- bare-message?, contains ID, theme, create time, data.
- extensible ability
    - don't need to konw location of sender and receiver. and don't need know how.
    - can choose to reclient or accept message
    - multiple subscriber, can take strategy of competition or non-competition to determine which one to handle it.
    - can add/del nodes
    - can add filter to choose subscriptions

RabbitMQ
========

Nova is main user of rabbitmq in openstack projects

has 2 types of rpc call, rpc.call & rpc.cast, to request/response

- rpc.call 
    - Direct Exchange -- server send ack message, one queue each exchanger
    - Topic Exchange  -- client start request, multi-queue each exchanger
        - topic/topic.host -- two types of theme, later one can designate which host to response
- rpc.cast -- no response needed.


- Components
    - Topic Publisher
    - Direct Consumer
    - Topic Consuer
    - Direct Publisher
    - Topic Exchange
    - Direct Exchange

