========================================
GitHub -- Git repository hosting service
========================================

github.com
==========

| Download: `windows <https://windows.github.com>`_
| `JetChars' HomePage <https://github.com/JetChars>`_
| `GitCafe <https://gitcafe.com>`_ -- substitue for github
| `CODING <https://coding.net>`_ -- another substitue


shortcuts
---------

=== ==================
key description
=== ==================
t   open a file browser
w   enter branch option
s   search bar
=== ==================

search engine
-------------

* Only files smaller than 384 KB are searchable

========= =========================================================
options   description
========= =========================================================
in        scope search fields(file, path, or both) ``in:file,path``
language  xml,markdown,python,...    ``language:xml``
size      file size (byte)           ``size:100`` ``size:>100``
filename  search by filename         ``filename:analysis.sh``
extension search by entension        ``extension:sh``
========= =========================================================

url customization
-----------------

========= =====================================================
url args  description
========= =====================================================
ts        tab space(indent length) ``url?ts=4``
author    designate author at commits's url ``author=JetChars``
#         hight lines(include start&end)  ``#L20-L30``
========= =====================================================



github.io -- github pages
=========================

.. sidebar:: `Domain Name Terms <http://en.wikipedia.org/wiki/Domain_Name_System>`_

    * **A/ANAME/ALIAS** -- Fixed IP
    * **CNAME** -- Canonical Name
    * **MX** -- Mail service server
    * **URL** -- jump to other site
    * **SRV** -- build dns server


* 300M free space
* Steps
    * create project at github, name as username.github.io
    * create empty file ``.nojerky`` at root if any folder start with '_'
    * create `404.html <http://www.qq.com/404/>`_ at root for customized 404 page
    * create `CNAME <https://help.github.com/articles/adding-a-cname-file-to-your-repository/>`_ at root record one of your own domain name
        * `A Record <https://help.github.com/articles/tips-for-configuring-an-a-record-with-your-dns-provider/>`_
        * `CNAME Record <https://help.github.com/articles/tips-for-configuring-a-cname-record-with-your-dns-provider/>`_
* official recomment build with `jekyll <http://jekyllrb.com>`_


`git.io <http://git.io>`_ -- short addr service
============================

.. code-block:: shell
    :linenos:

    $ curl -i http://git.io -F "url=https://github.com/jetchars"
    HTTP/1.1 100 Continue
    
    HTTP/1.1 201 Created
    Server: Cowboy
    Connection: keep-alive
    Date: Thu, 21 May 2015 11:47:10 GMT
    Status: 201 Created
    Content-Type: text/html;charset=utf-8
    Location: http://git.io/vUWJq
    Content-Length: 27
    X-Xss-Protection: 1; mode=block
    X-Content-Type-Options: nosniff
    X-Frame-Options: SAMEORIGIN
    X-Runtime: 0.302445
    X-Node: bf14801c-e7d1-4e46-91e7-04b0ff90e8aa
    X-Revision: 919f50eaf1146910dfe9e30b209c253a1a1cc217
    Via: 1.1 vegur


