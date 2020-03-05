
- WireShark 抓包 解密 https
    - 演示，淘宝直播，博物馆云春游，抓取视频回放网址

- 视频  [云春游？WireShark抓包，解密https，跟踪互联网7层协议](https://www.bilibili.com/video/av93598800/)
- 参考
    - [通过 wireshark 抓包了解直播流媒体RTMP协议基本过程](https://blog.csdn.net/tanningzhong/article/details/92987585)
    - [Wireshark 抓包理解 HTTPS 请求流程（2） - TLS/SSL 握手](https://ukscott.blogspot.com/2019/03/wireshark-https-2-tlsssl.html)
    - [针对自己的移动端App，可以在客户端调用OpenSSL握手的过程中使用如下代码将ClientRandom和MasterKey导出](https://zhuanlan.zhihu.com/p/64947416)

- 下载
    - 版本 2.6.1 不需要最新的
    - https://www.wireshark.org/download.html
        - Go Spelunking。Past releases can be found by browsing the all-versions directories under each platform directory. 
        - 旧版本 ftp://ftp.uni-kl.de/pub/wireshark/osx/all-versions/

- 运行
    - 需要启用【无线网卡】，即使有【有线网卡】，否则不显示网卡接口

- 电脑开启【WiFi热点】，把流量分享给手机
    - 参考 [Mac端WireShark抓移动端包](https://www.jianshu.com/p/82bcdb1decf7)
    - WireShark监控无线网卡
    - curl  https://httpbin.org/ip
    - curl  http://httpbin.org/ip
        - ip.src == 52.44.66.161
        - ip.dst == 3.214.162.152
        - 服务器IP会改变

- 解码HTTPS
    - 参考 
        - [Mac中wireshark如何抓取HTTPS流量？](https://www.cnblogs.com/rainmote/p/8320369.html)
        - [【技术流】Wireshark对HTTPS数据的解密
网易云信](https://zhuanlan.zhihu.com/p/36669377)
    - 从Chrome浏览器导出 SSLKEYLOGFILE
        - [MacOS 下 Wireshark 抓取 Chrome HTTPS](https://segmentfault.com/a/1190000021142289)
        - sudo /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --ssl-key-log-file=/Users/`whoami`/sslkeylog.log
    - Chromium
        - /usr/local/lib/node_modules/puppeteer/.local-chromium/mac-674921/chrome-mac/Chromium.app/Contents/MacOS/Chromium  --ssl-key-log-file=/Users/play/sslkeylog22.log
    - 配置WireShark
        - 打开【Preferences】
            - 选择 Protocols
            - 选择 SSL (最新版本选择TLS)
                - (Pre)-Master-Secret 添加sslkeylog文件

- 本机IP
    - ifconfig |grep 192
        - inet 192.168.0.222 netmask 0xffffff00 broadcast 192.168.0.255

- 抓包手机流量，iPhone。使用mitmproxy
    - 参考 [Wireshark and SSL/TLS Master Secrets](https://docs.mitmproxy.org/stable/howto-wireshark-tls/)
    - 因为Charles无法导出SSLKEYLOGFILE
    - 手机WiFi代理设置，192.168.0.222  端口 8080
    - iPhone上要安装mitmproxy的ssl证书，提前装好
    - ping httpbin.org
        - 服务器IP 52.44.66.161

    - 启动mitmproxy
        - SSLKEYLOGFILE="~/.mitmproxy/sslkeylogfile.txt" mitmproxy
    - 启动 WireShark，监听有线网卡
    - curl -k -x 127.0.0.1:8080 https://httpbin.org/ip
- 启动手机
    - 打开浏览器 
        - http://httpbin.org/ip
        - https://httpbin.org/ip
- WireShark过滤
    - 参考 
        - [wireshark过滤规则及使用方法](https://blog.csdn.net/wojiaopanpan/article/details/69944970)
        - [Wireshark 跟踪TCP流](https://blog.csdn.net/bcbobo21cn/article/details/91349077)
    - dns
    - http
        - http contains "ip"
    - ssl
    - http2
    - tcp.port==443 
    - 网络层协议，Apply as Filter
        - ip.host == "192.168.0.222"
        - ip.src == 192.168.0.222
        - ip.dst == 52.44.66.161
    - Follow
        - Follow TCP Stream
        - Follow SSL Stream


- 淘宝直播 m3u8文件，视频流
    - 微博 https://weibo.com/1855335174/IwzGdF4mZ
    - 参考 
        - [使用Wireshark抓取淘宝直播回放源地址并下载](https://www.jianshu.com/p/8333d90dc83e)
        - [WireShark提取天猫魔盒请求链接](https://blog.csdn.net/zengraoli/article/details/104085906)
    - 布达拉宫直播回放地址 https://h5.m.taobao.com/taolive/video.html?id=254225007624&type=473&livetype=replay&screenOrientation=landscape&vrType=0&livesource=anchorInfo
    - DNS livenging.alicdn.com
        - Queries
            - livenging.alicdn.com: type A, class IN
        - Answers
            - livenging.alicdn.com.danuoyi.alicdn.com: type A, class IN, addr 202.108.249.186
            - livenging.alicdn.com.danuoyi.alicdn.com: type A, class IN, addr 202.108.249.185
        - 然后 过滤
            - ip.dst == 202.108.249.185
            - ip.dst == 202.108.249.186
    - 找不到 m3u8文件
        - http contains ".m3u8"

