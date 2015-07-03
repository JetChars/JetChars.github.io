=====
Shell
=====



Variables
=========

Parameter Expansion
-------------------

expansion operators
^^^^^^^^^^^^^^^^^^^

- substitute operator

==================== ========================
operator             substitute
==================== ========================
${varname:-word}     if null, return word
${varname:=word}     if null, set word to varname, then return word
${varname:+word}     if not null, return word
${varname:?message}  if null, print message then exit
==================== ========================


- pattern matching mode

positional parameter
^^^^^^^^^^^^^^^^^^^^

special parameter
^^^^^^^^^^^^^^^^^

Arithmetic Expansion
--------------------

No need of escape charactor

=================== =============================  ========
operator            description                    sequence
=================== =============================  ========
++ --               auto add/minus                 LR
+ - ! ~             unary +/- , AND/OPPISITE       RL
=================== =============================  ========






