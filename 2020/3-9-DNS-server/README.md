## 编程实现DNS服务器 - 用来翻墙？

- 视频  [编程实现DNS服务器，Python+Go。代码很简单！](https://www.bilibili.com/video/av94972898/)
    - 上个视频  [先收藏！！Python编程获取【在线网页代理】的重定向地址](https://www.bilibili.com/video/av94486958/)

- 参考
    - [How to write a DNS server in Go](https://jameshfisher.com/2017/08/04/golang-dns-server/)
        - 使用到的Go库 https://github.com/miekg/dns
            - Go DNS example https://github.com/miekg/exdns
    - 完整的程序 [如何在Go编程语言中编写自己的DNS代理？](https://www.smartspate.com/write-dns-proxy-go-programming-language/)
        - 目的是：屏蔽广告
        - 代码 https://github.com/GoWebProd/goDNS
            - 也是使用上面的dns库
            - 问题 
                - 黑名单找不到 https://raw.githubusercontent.com/GoWebProd/openvpn-adBlock/master/list/black.list 
                - 使用Google DNS 8.8.8.8 在中国不能用
    - Python DNS 库 
        - https://github.com/rthalley/dnspython
        - http://www.dnspython.org/
            - dnspython是用于DNS的实用程序，/etc/hosts因此未使用。
            - 对于简单的正向DNS查找，最好使用socket.gethostbyname()
        - 文章 [python3之DNS处理模块dnspython](https://blog.csdn.net/xwl145/article/details/81746497) 详细 

- DNS记录类型
```
A记录，将主机名转换成IP地址；
MX记录，邮件交换记录，定义邮件服务器的域名；
CNAME记录，指别名记录，实现域名间的映射；
NS记录，标记区域的域名服务器及授权子域；
PTR记录，反向解析，与A记录相反，将IP转换成主机名；
SOA记录，SOA标记，一个起始授权区的定义。
```

- 我写的DNS 服务地址
    - https://play4fun.pythonanywhere.com/
    - https://play4fun.pythonanywhere.com/dns?domain=www.free-proxy.com

- 把mini_dns_server 设置为系统DNS服务器
    - 实现某些网站翻墙，例如在线网站代理
        - 不是所有的国外网站都能翻

- 测试
    - https://weboproxy.com/
    - https://www.free-proxy.com/
- 目标网站
    - https://www.reddit.com/r/golang
