
================================
SQL -- Structured Query Language
================================

* Clinet / Server Structured

Grammar
=======

* Case Insensitive
* Each command end w/ ";"

Data Manipulation Language (DML)
================================

INSERT
======

.. code-block:: sql
    :linenos:

    insert into tbl_name valuse(all vals);
    insert into tbl_name(keys) valuse(vals);


UPDATE
======




Data Definition Language (DDL)
==============================

CREATE
======

.. code-block:: sql
    :linenos:

    create database db_name;
    create database if not exists db_name;
    create database samp_db character set gbk;
    create table table_name();

DROP
====

.. code-block:: sql
    :linenos:

    drop database db_name;
    drop database if exists db_name;


USE
===

.. code-block:: sql
    :linenos:

    use db_name   # change currnet db
    use information_schema   # built-in db



DQL
===

DCL
===



MySQL
=====

.. sidebar:: Windows Verison

    ::

        net stop mysql
        net start mysql
        # uninstall 
        sc delete mysql



* default use port 3306
* default data location ``/var/lib/mysql``

``mysql -uuname -ppasswd -hhost -Ddb_name -e "SQL cmds"``

.. code-block:: sql
    :linenos:

    \s   #show status
    show databases;
    show variables;
    show variables like "max_connections";
    show tables;
    show create table tbl_name;   # show how table created
    desc/describe tbl_name;   # show table structure
    ?/help contents   # get help from top level
    help keyword   # show more detail about cmd


PostgreSQL
==========


Developed by UC Berkely, is an ORDBMS, support most of SQL standards.

- using command ``psql``

- `PostgreSQL 8.1 manual_cn <http://www.php100.com/manual/PostgreSQL8/>`_

