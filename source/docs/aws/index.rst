==========================
AWS -- Amazon Web Services
==========================

- `Amazon Video Center <http://aws.amazon.bokecc.com>`_
- `AWS CN Training <http://aws.amazon.com/cn/training>`_
- Hands-on
    - `CN Version <https://china-run.qwiklabs.com>`_ , `EN Version <https://qwiklabs.com>`_
    - Free Courses (16 ordered by myself)
        - AWS Identity and Access Management (IAM) Introductory
        - Amazon Elastic Compute Cloud (EC2) Introductory
        - Amazon Simple Storage Service (S3) Introductory
        - Amazon Elastic Block Store (Amazon EBS) Introductory
        - Amazon Elastic MapReduce Introductory
        - Amazon Relational Database Service (Amazon RDS) Introductory
        - Amazon Virtual Private Cloud (VPC) Introductory
        - Amazon Elastic Load Balancer (Amazon ELB) Introductory
        - Introduction to Amazon DynamoDB
        - Introduction to AWS Elastic Beanstalk
        - Introduction to AWS CloudFormation
        - Introduction to Amazon ElastiCache
        - Introduction to AWS OpsWorks
        - Introduction to Amazon CloudFront
        - Introduction to AWS CodeDeploy
        - Introduction to EC2 Spot Instances





BKM should be turned into script, let people doing job more creatively.

Storage
=======

- S3 -- Amazon Simple Storage Service
    - first create an bucket, can contain unlimit amount of file
    - each file size from 1B to 5TB
    - compare to EBS, no need resize bucket size
- EBS -- Elastic Block Storage


Compute
=======

- EC2 -- Elastic Computer Cloud
    - high storage instance, have 48TB
    - price competition instance(spot mode), at most 50% price off, will be take by force
    - nic opts -- low, medium, high, 10G
- EMR -- Elastic MapReduce
    - Components -- Master, Core, Task Node
    - Master/Core nodes cannot reduce.
    - Task Node not storage data for reason
    - src data in s3, intermedia data in hdfs, dst data in s3
    - ec2 support centos, emr not support it.
    - log to s3


Database
========

DynamoDB -- noSQL dataBase

apis: CreateTable, DeleteTable, UpdateTable, PutItem, GetItem, UpdateItem, DeleteItem, BatchGetItem, BatchWriteItem,Query, Scan (when no index exists, can use this to search all table)

RDB -- Relational DataBase


Commercial Case
===============

- NetFlix -- All services run in amazon, 1/3 of US network dataflow.




Terms
=====

- APN -- AWS Partner Network
- ELB -- Elastic Load Balance
- Elastic -- AutoScalable?
