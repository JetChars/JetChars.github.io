=======================
String Processing Tools
=======================

Regular Expression
==================


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
    * ``sed -n '3p' datafile``     only print line 3
    * ``sed -n '/expr/'p FILE``    print all lines match expr
    * ``sed -n '4,/expr/'p FILE``  print start from line 4 till line match expr
    * ``sed -n 'p;n' file`` output odd-numbered line
    * ``sed -n 'n;p' file`` output even-numbered line



================= =======================================================
options           description
================= =======================================================
n                 only output with function ``p``
e                 exec multiple cmds ``sed -e 'regex1' -e 'regex2' FILE``
i                 edit in file ``sudo sed -i '/^RSYNC_ENABLED=false/ {s/false/true/ }' /etc/default/rsync``
f                 exec cmds stores in cmd_file
================= =======================================================

Functions
---------
========================= ======================================================
name                      description
========================= ======================================================
s/regex/replacement/flags switch lines, flags can be 'val' 'g'
n/d/p                     next/delete/print line
!function                 apply the func only to the lines that are not selected
========================= ======================================================



Examples
--------

.. code-block:: shell
    :linenos:

    # substitute all aaa into bbb
    sed 's/aaa/bbb/g' FILE  
    # only substitute form line 1 to 50
    sed '1,50s/aaa/bbb/g' FILE
    # add # to the front of line 1,2

    # not print line 2 to 5
    sed '2,5d' datafile
    # not print last line
    sed '$d' file
    # not print first line is not applicable
    sed '^d' file
    # not print empty lines
    sed -e '/^$/d'
