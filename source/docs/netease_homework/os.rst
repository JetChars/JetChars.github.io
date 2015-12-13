================
Operating System
================

Basics
======
======

bashrcbashrc与环境变量
----------------------

- bash的系统和个人配置文件的路径是什么? 
     - /etc/bashrc ~/.bashrc
- $PS1这个环境变量有什么用? 
     - 修改命令行提示符
- 在什么情况下需要修改 ``$PATH`` ,应该如何合理地修改它? 
     - 修改 ``$PATH`` 是为了运行可执行文件时省略文件的详细路径
     - 可以在 ``/etc/enviroment`` ``/etc/profile`` ``bashrc`` 等文件中进行修改
     - 可以使用 ``PATH=$PATH:<new_path>`` 这样的形式来添加新的路径
- 修改过~/.bashrc后,如何让改变立即生效? 
     - 修改 ``~/.bashrc`` 文件后可以使用命令 ``source ~/.bashrc`` 或 ``. ~/.bashrc`` 来进行导入
- bashrc与profile有什么异同点?两者的加载顺序如何?
    - profile文件仅在login shell中会读取
    - ``/etc/profile`` -> ``~/.profile`` (.bash_profile > .bash_login > .profile) -> ``~/.bashrc`` -> ``/etc/bashrc``
    
FHS与proc
---------

- 为什么系统命令会分别放到/bin, /sbin, /usr/bin, /usr/sbin这四个目录中? 这些目录间有什么区别?
    - bin和sbin路径是用来存放系统工具的，sbin中的工具是需要root权限才能执行的
    - usr 目录下的工具是用户自行安装的
- /var目录通常用来放哪些内容?/var和/tmp有什么区别?
- /boot目录里有哪些内容?
- /usr/include和/usr/lib有什么区别?
- /proc目录下的那些数字是什么东西?
- 如何在proc文件系统中查看CPU和内存信息?


cron
----

- 系统配置文件的路径是什么? 
    - /etc/cron{tab,.allow,.deny}
    - /etc/cron.{d,hourly,daily,weekly,monthly}
- cron时间描述里的'-'是什么意思, '/'是什么意思?
    - ``-`` 表示时间段
    - ``/`` 连接时间间隔
- @reboot会在什么时候执行?
    - 重启后立即执行
- cron的最小粒度是分钟, 如何用cron实现每分钟跑两次(例如, 分别在第0秒和第 30秒)运行的任务?
    - 自己写个脚本 ``sleep 30``


NTP与UTC
--------
- ntpdate和ntpd相比有什么优势和劣势. 
    - ntpdate会立即矫正时间，但会导致很多时间相关的系统冲突，如数据库
    - ntpd会慢慢的逐渐修正时间，可以避免ntpdate的问题
- 既然已经有了ntp, 为什么还需要有hwclock? 
    - 确保断电后时间也能保留
- UTC是什么? 
    - Universal Time Coordinated 世界统一时间
- Debian中如何修改系统时区?
    - tzselect/timadatectrl
    - ``ln -sf /usr/share/zoneinfo/posix/Asia/Shanghai /etc/localtime``
