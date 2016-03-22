================
Ceph RESTful API
================


.. code-block:: shell

    nohup ceph-rest-api -n client.admin &
    curl localhost:5000/api/v0.1/status   # same as ceph -s
