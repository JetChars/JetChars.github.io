===================================
HiBench - The Hadoop BenchMark Suit
===================================

Most of my hadoop tuning data derived with this benchmark tool.


What is HiBench? [#]_ 
================

This benchmark suite contains 10 typical Hadoop workloads (including micro benchmarks, HDFS benchmarks, web search benchmarks, machine learning benchmarks, and data analytics benchmarks). [#]_

Advantages:

* Realistic and comprehensive
* Quantitive characteriztion of different workload
* Evaluation of different deployment


BenchMark Types
===============

HiBench Contains 5 different types of benchmark.

#. micro benchmarks: ``Sort`` ``WordCount`` ``TeraSort``
#. HDFS benchmarks: ``enhanced DFSIO`` ``Sleep``
#. web search benchmarks: ``Nutching indexing`` ``PageRank``
#. machine learning benchmarks: ``Bayes Classification`` ``K-means`` ``Clustering``
#. data analytics benchmarks: ``Hive`` ``Query`` ``Benchmark``


Configuration & Running scripts
===============================

Global enviroment variable in ``bin/hibench-config.sh``

Each workload can run separately:

* ``conf/configure.sh``	 Configuration file contains all parameters such as data size and test options.
* ``bin/prepare*.sh``  	 Generate or copy each workload's prepare data into HDFS.
* ``bin/run*.sh``        Execute the workload


Default Configurations
======================

Default configurations' data size normally very small.

DFSIOE
------

.. code-block:: shell
    :linenos:
    :emphasize-lines: 9,10,13,14

    ## paths
    INPUT_HDFS=${DATA_HDFS}/benchmarks/TestDFSIO-Enh
    
    export HADOOP_OPTS="$HADOOP_OPTS -Dtest.build.data=${INPUT_HDFS}"
    MAP_JAVA_OPTS=`cat $HADOOP_CONF_DIR/mapred-site.xml | grep "mapreduce.map.java.opts" | awk -F\< '{print $5}' | awk -F\> '{print $NF}'`
    RED_JAVA_OPTS=`cat $HADOOP_CONF_DIR/mapred-site.xml | grep "mapreduce.reduce.java.opts" | awk -F\< '{print $5}' | awk -F\> '{print $NF}'`
    
    # dfsioe-read
    RD_NUM_OF_FILES=256
    RD_FILE_SIZE=200 #2000
    
    # dfsioe-write
    WT_NUM_OF_FILES=256
    WT_FILE_SIZE=100 #1000


Sort
----

.. code-block:: shell
    :linenos:
    :emphasize-lines: 16,17,20

    # compress
    COMPRESS=$COMPRESS_GLOBAL
    COMPRESS_CODEC=$COMPRESS_CODEC_GLOBAL
    
    # paths
    INPUT_HDFS=${DATA_HDFS}/Sort/Input
    OUTPUT_HDFS=${DATA_HDFS}/Sort/Output
    
    if [ $COMPRESS -eq 1 ]; then
        INPUT_HDFS=${INPUT_HDFS}-comp
        OUTPUT_HDFS=${OUTPUT_HDFS}-comp
    fi
    
    # for prepare (per node) - 24G/node
    #DATASIZE=24000000000
    DATASIZE=2400000000
    NUM_MAPS=16
    
    # for running (in total)
    NUM_REDS=48


WordCount
---------

.. code-block:: shell
    :linenos:
    :emphasize-lines: 17,18,21

    # compress
    # for best performance set COMPRESS=1 for MR1 and COMPRESS=0 for MR2 (for WordCount)
    COMPRESS=$COMPRESS_GLOBAL
    COMPRESS_CODEC=$COMPRESS_CODEC_GLOBAL
    
    # paths
    INPUT_HDFS=${DATA_HDFS}/Wordcount/Input
    OUTPUT_HDFS=${DATA_HDFS}/Wordcount/Output
    
    if [ $COMPRESS -eq 1 ]; then
        INPUT_HDFS=${INPUT_HDFS}-comp
        OUTPUT_HDFS=${OUTPUT_HDFS}-comp
    fi
    
    # for preparation (per node) - 32G
    #DATASIZE=32000000000
    DATASIZE=3200000000
    NUM_MAPS=16
    
    # for running (in total)
    NUM_REDS=48


k-means
-------

.. code-block:: shell
    :linenos:
    :emphasize-lines: 16,18,20,21,24

    # compress
    COMPRESS=$COMPRESS_GLOBAL
    COMPRESS_CODEC=$COMPRESS_CODEC_GLOBAL
    
    # paths
    INPUT_HDFS=${DATA_HDFS}/KMeans/Input
    OUTPUT_HDFS=${DATA_HDFS}/KMeans/Output
    if [ $COMPRESS -eq 1 ]; then
        INPUT_HDFS=${INPUT_HDFS}-comp
        OUTPUT_HDFS=${OUTPUT_HDFS}-comp
    fi
    INPUT_SAMPLE=${INPUT_HDFS}/samples
    INPUT_CLUSTER=${INPUT_HDFS}/cluster
    
    # for prepare
    NUM_OF_CLUSTERS=5
    #NUM_OF_SAMPLES=20000000
    NUM_OF_SAMPLES=3000000
    #SAMPLES_PER_INPUTFILE=4000000
    SAMPLES_PER_INPUTFILE=600000
    DIMENSIONS=20
    
    # for running
    MAX_ITERATION=5



References
==========

.. [#] https://github.com/intel-hadoop/Hibench
.. [#] http://ieeexplore.ieee.org/xpl/articleDetails.jsp?reload=true&arnumber=5452747
