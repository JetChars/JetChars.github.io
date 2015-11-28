========
梦幻西游
========

使用工具wireshark
netstat
直接查看源文件（可以查到分区服务器的IP/PORT）
手游还可以使用工具surge或者使用代理服务器到pc然后通过桌面工具来进行分析


1. 打开游戏客户端后, 游戏客户端要连接哪些服务器和端口?
    - 打开客户端 xyq.163.com 
        - 58.221.78.39 80
    - 更新服务器 update.xyq.163.com
    - 补丁服务器 autopatch.xyq.163.com
        - xy-cache.163.com
        - snaly.nie.163.com
    - 补丁下载服务器 xyq.gph0{1-3}.netease.com
        - lst.dlmix.ourdvs.com(xyq.gph02.netease.com) 122.228.237.175 62078
    - 新闻、广告服务器 gad.netease.com
    - 游戏下载？ xyq.gdl.netease.com
    - 更新api？ api.ku.163.com
    - a.tool.netease.com
    - a.game.163.com
    - pic.x1.126.net
    - analytics.163.com
    - pr.tool.netease.com
    - pr.game.netease.com

2. 游戏客户端如何得到游戏服务器的IP地址和端口?
    - 从配置文件server.ini中读取
3. 用户密码的校验过程中, 会连接哪些服务器和端口?
4. 登录进入游戏后, 在游戏过程中, 游戏客户端会连接哪些服务器和端口? 
5. 退出客户端时, 客户端访问了哪些服务器和端口?
6. 游戏里有哪些分区和服,向导师讲述你对分区和服这两个概念的理解?
7. 玩家看到的游戏服,背后由多少台物理服务器组成?
    - 有57个分区，具体的列表可以从server.ini文件中获得
8. 如果玩家连不上游戏,客户端提供哪些途径让玩家反馈问题? 尝试运行这样的工具,看看输
