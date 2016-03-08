=============
MicroServices
=============



The microservice architectural style [1] is an approach to developing a single application as a suite of small services, each running in its own process and communicating with lightweight mechanisms, often an HTTP resource API. These services are built around business capabilities and independently deployable by fully automated deployment machinery. There is a bare minimum of centralized management of these services, which may be written in different programming languages and use different data storage technologies. [mar2014]_


I think the style 'microservices' is a good architechture  for distributed software.

- default style for building enterprise applications
- RESTful api for client/server communications
- AMQP for communications between services
- different language would be better for diff platform/problem



- subset of SOA
- componentization via serveces (can be upgrade independently, c/s comm via RESTful)
- organized around business capabilities(we're the users)
- smart endpoints and dumb pipes(comm between services via amqp)
- decentralization management
- decentralization database(each service have own datastore?)

chaos monkey(netflix) and k8s(google) are major users of microservices






monolith vs. microservices

======================= =========================
monolith                microservices
======================= =========================
simple                  partial deployment
                        availability
======================= =========================





.. [mar2014] http://martinfowler.com/articles/microservices.html










