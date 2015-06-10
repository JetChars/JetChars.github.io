=======================
reStructured Text (rst)
=======================

.. image:: images/rst.png
    :align: right
    :width: 200px
    :alt: rst logo


reStructuredText is an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax and parser system. It is useful for in-line program documentation (such as Python docstrings), for quickly creating simple web pages, and for standalone documents. reStructuredText is designed for extensibility for specific application domains. The reStructuredText parser is a component of Docutils. reStructuredText is a *revision* and *reinterpretation* of the **StructuredText** and **Setext** lightweight markup systems. [#]_


.. sidebar:: Note

    "reStructuredText" is ONE word, not two!

| `quick start <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_
| `alternatives <http://docutils.sourceforge.net/docs/dev/rst/alternatives.html>`_
| `fruit doc <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html>`_
|
|
|
|
|

Standard rST
============

Headings
--------

- \# with overline, for parts
- \* with overline, for chapters
- \= for sections
- \- for subsections
- \^ for subsubsections
- \" for paragraphs



Inline mark
-----------

.. raw:: html     
    
    <div class="sidebar">

| *italic*
| **bold**
| ``inline literal``

.. raw:: html     
    
    </div>

| Inline markup allows words and phrases within text to have character styles (like italics and boldface) and functionality (like hyperlinks).
|

.. code-block:: rst

    *italic*
    **bold**
    ``inline literal``



Directives
==========

.. code-block:: rst

    .. <name>:: <arguments>
        :<option>: <option values>
    
         content

Photos
------

.. sidebar:: Note

    - suffix of image is required
    - png file not support distortion, so resize it only need to change width or height
    - ``align`` can be ``left`` , ``right`` or ``center``

.. code-block:: rst

    .. image:: images/rst.png
        :align: right
        :width: 400px
        :height: 100px
        :alt: alternate text
       
|
|
|
|



SideBar
-------

.. sidebar:: Sidebar Title
    :subtitle: Optional Sidebar Subtitle
 
    Subsequent indented lines comprise
    the body of the sidebar, and are
    interpreted as body elements.

.. code-block:: rst

    .. sidebar:: Sidebar Title
       :subtitle: Optional Sidebar Subtitle
    
       Subsequent indented lines comprise
       the body of the sidebar, and are
       interpreted as body elements.

|
|
|


HTML
----

.. raw:: html     
    
    <div class="sidebar">

rst contents with no titlebar

.. code-block:: guess

    hello world!
 
.. raw:: html    
    
    </div>



.. code-block:: html

    .. raw:: html
    
        <div class="sidebar">
    
    rst contents with no titlebar

    .. code-block:: guess
    
        hello world!
    
    .. raw:: html
    
        </div>



Sphinx Customized rST
=====================


Table of Content Tree (toctree)
-------------------------------


.. sidebar:: Example

    - menu depth 2
    - add numbers to titles
    - one file only one title
    - linux glob matching 
    - hidden title


| Usually put in index.rst file at root dir
|

.. code-block:: rst

    .. toctree::
        :maxdepth: 2
        :numbered:
        :titlesonly:
        :glob:
        :hidden:


Paragraph Mark
--------------

.. code-block:: rst

    .. note:: paragraph of note
    .. warning:: paragraph of warning

.. note:: paragraph of note
.. warning:: paragraph of warning


Code Block
----------
.. code-block:: rst

    .. code-block:: c
        :linenos:
        :emphasize-lines: 3,5-7
    
        #include<stdio.h>
        int Q[93],a[8],c=0,m=-1,i,t;
        void qne(int rw,int l,int r){
            if(rw!=255)
                for(int pos=255&~(rw|l|r),p;pos;pos-=p){
                    for(t=p=pos&-pos,a[++m]=1;t>>=1;++a[m]);
                    qne(rw+p,(l+p)<<1,(r+p)>>1);
                }
            else for(Q[++c]=i=0;i<8;Q[c]=Q[c]*10+a[i++]);
            --m;
        }
        void main(){for(qne(0,0,0),scanf("%d",&m);m--;printf("%d\n",Q[c]))scanf("%d",&c);}



.. code-block:: c
    :linenos:
    :emphasize-lines: 3,5-7

    #include<stdio.h>
    int Q[93],a[8],c=0,m=-1,i,t;
    void qne(int rw,int l,int r){
        if(rw!=255)
            for(int pos=255&~(rw|l|r),p;pos;pos-=p){
                for(t=p=pos&-pos,a[++m]=1;t>>=1;++a[m]);
                qne(rw+p,(l+p)<<1,(r+p)>>1);
            }
        else for(Q[++c]=i=0;i<8;Q[c]=Q[c]*10+a[i++]);
        --m;
    }
    void main(){for(qne(0,0,0),scanf("%d",&m);m--;printf("%d\n",Q[c]))scanf("%d",&c);}


Intersect Index
---------------

Download
^^^^^^^^

.. sidebar:: Example

    :download:`rst.png <images/rst.png>`

| Referenced file will be copied to folder ``build/html/_downloads/``
|

.. code-block:: rst

    :download:`rst.png <images/rst.png>`

Maths & Equttions w/ LaTeX
--------------------------

.. sidebar:: Example

    :math:`\alpha > \beta`

.. code-block:: rst

    :math:`\alpha > \beta`



.. [#] http://docutils.sourceforge.net/rst.html
