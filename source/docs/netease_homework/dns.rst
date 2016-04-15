============
dns homework
============

domain basics
=============

- steamedfish.org. authority server, and chenxiaosheng.com.
	- ns{1..5}.linode.com.
	- f1g1ns{1,2}.dnspod.net.
- douban creation time
  	- 2004.09.19
- nie.netease.com.  TTL
	- 18000s
- www.wangyi.com / ns5.nease.net
	- wangyi.com. -- NO! -- owner is **eName Technology Co.,Ltd.**
	- neaae.net -- Yes! -- owner is **Netease, Inc.**, it's dns server
- judge wether or not exist a domain
  	- dig domain.  -- status will be NXDOMAIN
-
- right choice is 3rd.
- resolv.conf/``domain`` is **local domain name**, if ``search``not configured, ``domain`` will be the default value of search; if search configured variable ``domain`` will disposed.
- 5 Sec
- ``dig +tcp domain.``
- ``dig +short`` or ``dig +nocmd +nocomment +nostat``, 但是两种方法显示的结果仍然存在不同，后一种可能包含部分被注释掉的记录。

::

	# dig mail.163.com +short
	mail163.yxgslb.netease.com.
	123.125.50.26
	123.125.50.28
	123.125.50.7

	# dig mail.163.com +nocmd +nocomment +nostat

	; <<>> DiG 9.9.5-3ubuntu0.7-Ubuntu <<>> mail.163.com +nocmd +nocomment +nostat
	;; global options: +cmd
	;mail.163.com.                  IN      A
	mail.163.com.           1358    IN      CNAME   mail163.yxgslb.netease.com.
	mail163.yxgslb.netease.com. 24  IN      A       123.125.50.7
	mail163.yxgslb.netease.com. 24  IN      A       123.125.50.26
	mail163.yxgslb.netease.com. 24  IN      A       123.125.50.28



- TLD指的是顶级域名，而Public Suffix却只包含部分的顶级域以及这些域的子域。Public Suffix是用于提高网页安全性的解决方案。


- CNAME的值不应该包含协议http://
- 多了一列的值10
- 负载均衡的TTL时间太长了
- 不应该有两个CNAME
- 不应包含下划线

TTL
===

- a.163.com.
  	- 800s
  	- 800s
- c.163.com.
	- 18000s



Maintenance
===========

- d.163.com e.163.com 需要维护
- 域名调整
	- 添加主机时添加``d.163.com. 29000 IN A 1.2.3.5``
	- 测试成功后删除``d.163.com. 29000 IN A 1.2.3.4``
	- 添加完内存后添加``d.163.com. 29000 IN A 1.2.3.4``
	- 最终测试成功后删除``d.163.com. 29000 IN A 1.2.3.5``
- 如何在10min内实现修改？