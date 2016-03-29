===========
RESTful API
===========


- **API** -- Application Programming Interface
- **REST** -- Representational State Transfer


- Advantages
    - can leverage cache to enhance response speed
    - easy to access


Http Requests [#]_
=============


- GET vs. POST [#]_
    - GET can be cached, while POST can't
    - GET have a restrictions on data length 2048 characters
    - GET only allow ASCII characters
    - POST data is not displayed in the url



================= ==================================
method            description
================= ==================================
OPTIONS           Returns the HTTP methods that the server supports
GET               Requests data from a specified resource
HEAD              Same as GET but returns only HTTP headers and no document body
POST              Submits data to be processed to a specified resource
PUT               Uploads a representation of the specified URI
DELETE            Deletes the specified resource
TRACE             
CONNECT           Converts the request connection to a transparent TCP/IP tunnel
xtension-method
================= ==================================



Using cURL to automate HTTP requests
====================================

https://curl.haxx.se/docs/httpscripting.html







Sources
=======

- `apigee <http://apigee.com>`_
- `ProgrammableWeb <http://www.programmableweb.com/>`_ -- The leading source of news & information about APIs
- `Example Google Maps API call <https://maps.googleapis.com/maps/api/geocode/json?address=disneyland,ca>`_
- `Using REST APIs in a web application(php) <https://github.com/jelled/geogram/blob/1-Basic-REST-Application/geogram.php>`_


.. [#] http://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html
.. [#] http://www.w3schools.com/tags/ref_httpmethods.asp
