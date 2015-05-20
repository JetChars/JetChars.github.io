=======================
String Processing Tools
=======================

Regular Expression
==================


awk -- pattern-directed scanning and processing
===============================================

SYNOPSIS
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
