====
HTML
====


Hyper Text Markup Language

2008 w3c release the HTML5 

`Tutorials from w3c <http://www.w3school.com.cn/html/index.asp>`_


- ``#`` after url, used to locate a anchor point identified by ``id``



Status codes
============
============


- 200 -- ok
- 301 -- permantly redirect
- 302 -- temporary redirect






Elements
========
========

grammar
-------

- comments: ``<!--comment_contents-->``
- conditional comments
    - <!--[if !IE]><!--> 除IE外都可识别 <!--<![endif]-->
    - <!--[if IE]> 所有的IE可识别 <![endif]-->
    - <!--[if IE 6]> 仅IE6可识别 <![endif]-->
    - <!--[if !(IE 6)]> 非IE6可识别 <![endif]-->
    - <!--[if lt IE 6]> IE6以下版本可识别 <![endif]-->
    - <!--[if lte IE 6]> IE6以及IE6以下版本可识别 <![endif]-->
    - <!--[if gt IE 6]> IE6以上版本可识别 <![endif]-->
    - <!--[if gte IE 6]> IE6以及IE6以上版本可识别 <![endif]-->
    - <!--[if (IE 6)&(IE 7)]> IE6和IE7可识别 <![endif]-->
    - <!--[if (IE 6)|(IE 7)]> IE6或IE7可识别 <![endif]-->
- element format: ``<type/>`` or ``<type> ... </type>``
- text: surrounded by ``""`` or ``''``
- file suffix : ``html`` or ``htm``
- path : document root is ``http://ip:port/``
- script triggered by event
    - ``onkeydown="test()"``
- entity symbols
    - space : ``&nbsp``
    - dash ``-`` : ``&mdash;``
- global attributes
    - class -- spceified one or multiple classname of one element
    - id -- each element have a unique ID
    - style -- specify CSS style in specified element
    - lang -- specify language
    - dir -- specify direction of text
    - data-* -- only works w/ HTML5
- html files start w/ document type
    - html 4.01 have 3 kinds of document type
    - html 5 have only one document type ``<!DOCTYPE html>``


elements
--------

- <head>
    - meta
        - viewport -- viewing mode

- <style> -- define within <head> to specify stles
  
.. code-block:: html

    <style>
      div:{
          width:200px;
          height:200px;
          background:blue;
      }
    </style>



Examples
========
========








