================
Ceph RESTful API
================


.. code-block:: shell

    nohup ceph-rest-api -n client.admin &
    curl localhost:5000/api/v0.1/status   # same as ceph -s
    curl -X POST -H "Content-Type: application/json" -d '
    {
        "username": "jet",
        "password": "6666"
    }' http://127.0.0.1/api/v2/auth/login

