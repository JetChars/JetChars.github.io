
==================
Regular Expression
==================

Intro
=====

Commonly used in linux shell、python and some other programming languages.

=========================== ========================= ===========================
regex                       support tools             comments
=========================== ========================= ===========================
BRE, Basic Regular Express  grep sed ed ex/vi more    brackets need transfer {}()
ERE, Extend Regular Express egrep awk lex
=========================== ========================= ===========================

Basic Regular Express
---------------------
+---------+--------------------------------+----------------------------------------------------+
|meta-char|descriptio                      |example                                             |
+=========+================================+====================================================+
|.        |matchs every char               |                                                    |
+---------+--------------------------------+----------------------------------------------------+
|? / +    |repeat any / at least one times | ? only used for ERE                                |
+---------+--------------------------------+----------------------------------------------------+
|^ / $    |head / end of line              |``^.$`` line of one char                            |
|         |                                |``^$`` empty line                                   |
+---------+--------------------------------+----------------------------------------------------+
|\\       |transfer char                   || ``\d`` == ``[0-9]`` , ``\D`` == ``[^\d]``         |
|         |                                || ``\w`` == ``[a-zA-Z0-9]`` , ``\W`` == ``[^\w]``   |
|         |                                || ``\s`` ==empty-char , ``\S`` == ``[^\s]``         |
|         |                                || ``\b`` ==space between words , ``\B`` == ``[^\b]``|
|         |                                || ``\bhello\b`` only match 'hello' not 'helloworld' |
+---------+--------------------------------+----------------------------------------------------+
|[] / [^] |designate range of a single char| ``[0-9a-z]`` ``[^0-9a-z]``                         |
+---------+--------------------------------+----------------------------------------------------+
| \|      |or                              |                                                    |
+---------+--------------------------------+----------------------------------------------------+

.. image:: images/regex_cn.png

grep -- Globally search a Regular Expression and Print
======================================================


awk -- pattern-directed scanning and processing
===============================================

Synopsis
--------
``awk [ -F field-separator ] [ -v var=value ] [ 'prog' | -f progfile ] [ file ...  ]``

* FS' default val is white space, it should be a regex
* The fields are denoted $1, $2, ..., while $0 refers to the entire line

Predefined variables
--------------------




Examples
--------

.. code-block:: shell
    :linenos:

    # Get column 1 if column 3 equals 0
    awk -F: '$3==0 {print $1}' /etc/passwd
    # Print row 12 column 1
    awk -F: '{if(NR==12) print $1}' /etc/passwd
    # Print lines longer than 72 characters.
    length($0) > 72
    # Print first two fields in opposite order.
    { print $2, $1 }
    # Same, with input fields separated by comma and/or blanks and tabs.
    BEGIN { FS = ",[ \t]*|[ \t]+" }{ print $2, $1 }
    # Add up first column, print sum and average.
    { s += $1 }  END  { print "sum is", s, " average is", s/NR }
    # Print all lines between start/stop pairs.
    /start/, /stop/
    # More complicate actions
    BEGIN     {    # Simulate echo(1)
              for (i = 1; i < ARGC; i++) printf "%s ", ARGV[i]
              printf "\n"
              exit }


sed -- stream editor
====================

Synopsis
--------
``sed [-Ealn] cmd [file ...]``

``sed [-Ealn] [-e cmd] [-f cmd_file] [-i extension] [file ...]``

* support regex
* escape charactor \\ can be applied to " but not '
* edit cmds ``[addr1[,addr2]]function``, seperated by ";"
    * ``sed -n '/expr/'p FILE``    print all lines match expr
    * ``sed -n '4,/expr/'p FILE``  print start from line 4 till line match expr



+-------+------------------+----------------------------------------------------------------------------+
|options & description     |examples                                                                    |
+=======+==================+============================================================================+
|n      |output with ``p`` |``sed -n '3p' datafile``     only print line 3                              |
+-------+------------------+----------------------------------------------------------------------------+
|e      |exec multiple cmds|``sed -e 'regex1' -e 'regex2' FILE``                                        |
+-------+------------------+----------------------------------------------------------------------------+
|i      |edit in file      |``sudo sed -i '/^RSYNC_ENABLED=false/ {s/false/true/ }' /etc/default/rsync``|
+-------+------------------+----------------------------------------------------------------------------+
|f      |exec cmds in file |                                                                            |
+-------+------------------+----------------------------------------------------------------------------+

Functions
---------
+-------------------------+------------------------------------+-------------------------------------------------+
|name                     |description                         |examples                                         |
+=========================+====================================+=================================================+
|s/regex/replace/flags    || switch lines                      || ``sed 's/aaa/bbb/g' FILE`` substitute golbally |
|                         || flags can be 'val' 'g'            || ``sed '1,50s/aaa/bbb/g' FILE`` substitue 1-50  |
+-------------------------+------------------------------------+-------------------------------------------------+
|n/d/p                    || next/del/print line               || ``sed -n 'p;n' file`` output odd-numbered line |
|                         |                                    || ``sed -n 'n;p' file`` output even-numbered line|
|                         |                                    || ``sed '2,5d' datafile`` not print line 2-5     |
+-------------------------+------------------------------------+-------------------------------------------------+
|!function                || apply the func only               |                                                 | 
|                         || to the lines that                 |                                                 | 
|                         || are not selected                  |                                                 | 
+-------------------------+------------------------------------+-------------------------------------------------+



Examples
--------

.. code-block:: shell
    :linenos:

    # add # to the front of line 1,2
    # not print last line
    sed '$d' file
    # not print first line is not applicable
    sed '^d' file
    # not print empty lines
    sed -e '/^$/d'
