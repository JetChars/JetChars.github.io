=========
bootstrap
=========


Intro
=====
=====

BootStrap is Front-end Framework

- include HTML/CSS/JS framewrok for depeloping responsive, mobile first projects on the web.
- ready-to-use web elements: button, form, table, image, navbar, label, progress bar, alert etc.
- provide cdn for fast loading
- 4 sizes of bootstrap grid
- 


Example of Use
--------------

.. code-block:: html

    <!DOCTYPE html>
    <html lang="zh-CN">
      <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
        <title>Bootstrap 101 Template</title>
    
        <!-- Bootstrap -->
        <link href="css/bootstrap.min.css" rel="stylesheet">
    
        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
          <script src="//cdn.bootcss.com/html5shiv/3.7.2/html5shiv.min.js"></script>
          <script src="//cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->
      </head>
      <body>
        <h1>你好，世界！</h1>
    
        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="//cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <script src="js/bootstrap.min.js"></script>
      </body>
    </html>


Components
==========

Glyphicon
----------

.. code-block:: html

    <span class="glyphicon glyphicon-search" aria-hidden="true"></span>

- ``aria-hidden`` let browsers know its just icon
- ``glyphicon-align-*`` have 4 diff shapes
    - ``glyphicon-align-left``, ``glyphicon-align-center``, ``glyphicon-align-right`` and ``glyphicon-align-justify```

button
------

.. code-block:: html

    <button type="button" class="btn btn-default" aria-label="Left Align">
      <span class="glyphicon glyphicon-align-left" aria-hidden="true"></span>
    </button>

    <button type="button" class="btn btn-default btn-lg">
      <span class="glyphicon glyphicon-star" aria-hidden="true"></span> Star
    </button>

- ``btn`` defines a button
    - ``btn-default`` -- button w/ default size
    - ``btn-default btn-lg`` -- button w/ large size, there is also ``btn-sm`` & ``btn-xs``
    - ``btn-danger`` -- change btn color, also ``btn-warning`` , ``btn-info`` , ``btn-success`` and ``btn-primary``

button-menu
^^^^^^^^^^^


- button can used as dropdown/dropup menu

.. code-block:: html

    <!-- Single button -->
    <div class="btn-group">
      <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
        Action <span class="caret"></span>
      </button>
      <ul class="dropdown-menu">
        <li><a href="#">Action</a></li>
        <li><a href="#">Another action</a></li>
        <li><a href="#">Something else here</a></li>
        <li role="separator" class="divider"></li>
        <li><a href="#">Separated link</a></li>
      </ul>
    </div>

- we can split button
  
.. code-block:: html

    <!-- Split button -->
    <div class="btn-group">
      <button type="button" class="btn btn-danger">Action</button>
      <button type="button" class="btn btn-danger dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
        <span class="caret"></span>
        <span class="sr-only">Toggle Dropdown</span>
      </button>
      <ul class="dropdown-menu">
        <li><a href="#">Action</a></li>
        <li><a href="#">Another action</a></li>
        <li><a href="#">Something else here</a></li>
        <li role="separator" class="divider"></li>
        <li><a href="#">Separated link</a></li>
      </ul>
    </div>


image
-----

- chang img shapes via editing img class

.. code-block:: html

    <img alt="Brand" src="img/hadoop.png" class="img-thumbnail">
    <img alt="Brand" src="img/hadoop.png" class="img-rounded">
    <img alt="Brand" src="img/hadoop.png" class="img-circle">





Navbar
------

- navbar sytles -- ``nav-tabs`` or ``nav-pills``
- justify -- ``nav-justified``
- disable a item -- ``class="disable"`` in **li class**
- dropdown-menu can be nested in navbar
- fixed on top -- ``navbar-fixed-top``

.. code-block:: html

    <ul class="nav nav-tabs">
      <li role="presentation" class="active"><a href="#">Home</a></li>
      <li role="presentation"><a href="#">Profile</a></li>
      <li role="presentation"><a href="#">Messages</a></li>
    </ul>


.. code-block:: html

    <ul class="nav nav-tabs">
      ...
      <li role="presentation" class="dropdown">
        <a class="dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">
          Dropdown <span class="caret"></span>
        </a>
        <ul class="dropdown-menu">
          ...
        </ul>
      </li>
      ...
    </ul>    


- real navbar, ``div class="container-fluid"`` and ``<div class="navbar-header">`` are required
- add brand -- ``<img alt="Brand" src="/path/to/img">``


.. code-block:: html

    <nav class="navbar navbar-default">
      <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Brand</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
            <li><a href="#">Link</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
              <ul class="dropdown-menu">
                <li><a href="#">Action</a></li>
                <li><a href="#">Another action</a></li>
                <li><a href="#">Something else here</a></li>
                <li role="separator" class="divider"></li>
                <li><a href="#">Separated link</a></li>
                <li role="separator" class="divider"></li>
                <li><a href="#">One more separated link</a></li>
              </ul>
            </li>
          </ul>
          <form class="navbar-form navbar-left" role="search">
            <div class="form-group">
              <input type="text" class="form-control" placeholder="Search">
            </div>
            <button type="submit" class="btn btn-default">Submit</button>
          </form>
          <ul class="nav navbar-nav navbar-right">
            <li><a href="#">Link</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
              <ul class="dropdown-menu">
                <li><a href="#">Action</a></li>
                <li><a href="#">Another action</a></li>
                <li><a href="#">Something else here</a></li>
                <li role="separator" class="divider"></li>
                <li><a href="#">Separated link</a></li>
              </ul>
            </li>
          </ul>
        </div><!-- /.navbar-collapse -->
      </div><!-- /.container-fluid -->
    </nav>


form
----

- ``form-inline`` - makes elements within form allign inline


.. code-block:: html

    <form class="navbar-form navbar-left" role="search">
      <div class="form-group">
        <input type="text" class="form-control" placeholder="Search">
      </div>
      <button type="submit" class="btn btn-default">Submit</button>
    </form>



Div
---

alert box
^^^^^^^^^

.. code-block:: html

    <div class="alert alert-danger" role="alert">
      <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
      <span class="sr-only">Error:</span>
      Enter a valid email address
    </div>

- ``sr-only`` let browsers know the meaning.


dropdown menu
^^^^^^^^^^^^^

.. code-block:: html

    <div class="dropdown">
      <button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
        Dropdown
        <span class="caret"></span>
      </button>
      <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">
        <li><a href="#">Action</a></li>
        <li><a href="#">Another action</a></li>
        <li><a href="#">Something else here</a></li>
        <li><a href="#">Separated link</a></li>
      </ul>
    </div>

    <div class="dropup">
      <button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu2" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
        Dropup
        <span class="caret"></span>
      </button>
      <ul class="dropdown-menu dropdown-menu-right" aria-labelledby="dropdownMenu2">
        <li><a href="#">Action</a></li>
        <li><a href="#">Another action</a></li>
        <li><a href="#">Something else here</a></li>
        <li><a href="#">Separated link</a></li>
      </ul>
    </div>

- dropdown or dropup menu by edit **div class**
- set alignment by edit **ul class** -- ``class="dropdown-menu dropdown-menu-right"``, menu box will go far right!
- set dropdown header by edit **li class** -- ``class="dropdown-header"``
- set a split line -- ``<li role="separator" class="divider"></li>``
- disable a line -- ``<li class="disabled"><a href="#">Disabled link</a></li>``


Button group & toolbar
^^^^^^^^^^^^^^^^^^^^^^


- button-toolbar contains multi button-group
- change buttom size within button-group -- ``class="btn-group btn-group-lg"``, similarly ``sm`` , ``xs``
- dropdown menu can be nested into button-group
- align btn-group vertically -- ``class="btn-group-vertical"``
- both ends aligned -- ``btn-group btn-group-justified``


.. code-block:: html

    <div class="btn-group" role="group" aria-label="...">
      <button type="button" class="btn btn-default">Left</button>
      <button type="button" class="btn btn-default">Middle</button>
      <button type="button" class="btn btn-default">Right</button>
    </div>


.. code-block:: html

    <div class="btn-toolbar" role="toolbar" aria-label="...">
      <div class="btn-group" role="group" aria-label="...">...</div>
      <div class="btn-group" role="group" aria-label="...">...</div>
      <div class="btn-group" role="group" aria-label="...">...</div>
    </div>


Input
^^^^^

- encapsuled by div
- change size by adding ``input-group-lg`` in **div class**
- **checkbox** or **radio** can be nested in span
- add placeholder attribute can set **prompte phrases**
- can nest dropdown menu
- ``col-lg-6`` means using 6 out of 12 columns(vertically)
- can mimic button -- ``<input type="button" class="btn btn-success"/>``


.. code-block:: html

    <div class="row">
      <div class="col-lg-6">
        <div class="input-group">
          <span class="input-group-addon">
            <input type="checkbox" aria-label="...">
          </span>
          <input type="text" class="form-control" aria-label="...">
        </div><!-- /input-group -->
      </div><!-- /.col-lg-6 -->
      <div class="col-lg-6">
        <div class="input-group">
          <span class="input-group-addon">
            <input type="radio" aria-label="...">
          </span>
          <input type="text" class="form-control" aria-label="..." placeholder="helloworld">
        </div><!-- /input-group -->
      </div><!-- /.col-lg-6 -->
    </div><!-- /.row -->


Auxilarly Classes
=================

background color
----------------

- ``bg-danger`` , ``bg-success`` ...




References
==========
==========


.. [#] http://www.slideshare.net/ronreiter/bootstrap-26583904?qid=51b655bb-a6be-43d0-b305-e91147bf4f0e&v=&b=&from_search=6
.. [#] http://www.slideshare.net/CedricSpillebeen/bootstrap-3-twitter-bootstrap-3-cedric-spillebeen-deftig?qid=51b655bb-a6be-43d0-b305-e91147bf4f0e&v=&b=&from_search=5


