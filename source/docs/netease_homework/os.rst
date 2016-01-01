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
    - hwclock保留的硬件时钟在保证持续供电的情况下，时间信息将一直保存
    - 而ntp获得的系统时钟是软件时钟，断电后将会失效。
- UTC是什么? 
    - Universal Time Coordinated 世界统一时间
- Debian中如何修改系统时区?
    - tzselect/timadatectrl
    - ``ln -sf /usr/share/zoneinfo/posix/Asia/Shanghai /etc/localtime``


文件的权限
----------
- /usr/bin下某命令abc的文件权限为744, 非属主应如何运行这个命令?
    - 非属主不论是组内其他用户，还是其他非组内用户都是可以读取该文件的。``bash filepath``
- 对于目录, 文件权限里的w和x各是什么意思?
    - w 代表是时写入权限，x代表的是执行权限
- rwsr-xr-x代表什么权限?
    - 表示当前用户可读写执行，且仅以所属用户身份执行
    - 组内其他用户可以读取或执行
    - 其他用户可以读取执行


管道与重定向
------------

- 重定向中的0, 1, 2各代表什么意思?
    - 0表示标准输入
    - 1表示标准输出
    - 2表示标准错误
- 请简述管道是如何让程序能够互相协同工作的.
    - 将前面语句的执行结果作为后面语句的输入内容
- 命名管道是什么东西? 如何创建一个有名管道?
- 请简述一个场景, 其中使用命名管道是必要的.


用户管理
--------

- 新用户创建时, 如果选择自动创建用户home目录, 此时home目录中自动生成的 内容是从哪儿来的?
    - ``useradd -D`` 查看变量SKEL，默认值是 ``/etc/skel``
- 删除一个用户时, 系统会执行那些操作, 改变哪些文件?
    - 清除该用户的家目录
- 用户的密码存储在哪个文件里?
    - ``/etc/shadow``
- 禁止用户登录的方式有哪些?
    - 修改 ``/etc/passwd`` 中用户的login shell成nologin
    - 修改 ``/etc/shadow`` 中保存的密码，在其前面添加!或者*可以使密码暂时失效
- 如何踢用户下线
    - ``skill -9 username``


apt-get与Debian软件包管理
-------------------------

- 请尽量详细地描述在执行apt-get update && apt-get install mtr 的过程中, apt-get是如何工作的.
- 怎么升级一个软件. 
- apt-get install 是如何处理已安装但需要升级的软件(例如openssh)的升级的?
- apt-cache



