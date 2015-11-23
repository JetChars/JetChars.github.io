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
    

