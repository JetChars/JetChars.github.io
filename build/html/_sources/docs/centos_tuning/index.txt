=============
CentOS Tuning
=============

Unlimit Non-root User's Resources
=================================

.. code-block:: shell
    :linenos:

    sudo rm -rf /etc/security/limits.d
    sudo cat >> /etc/security/limits.conf << EOF
    *                -       nproc           100000
    *                -       nofile          100000
    *                -       memlock         unlimited
    EOF
