
- WireShark 抓包
    - 演示，淘宝直播，博物馆云春游

- 视频 ？

- 下载
    - 版本 2.6？ 不需要最新的
    - https://www.wireshark.org/download.html
        - Go Spelunking。Past releases can be found by browsing the all-versions directories under each platform directory. 
        - 旧版本 ftp://ftp.uni-kl.de/pub/wireshark/osx/all-versions/

- 运行
    - 需要启用【无线网卡】，即使有【有线网卡】，否则不显示网卡接口

- 电脑开启【WiFi热点】，把流量分享给手机
    - WireShark监控无线网卡

- 解码HTTPS
    - 参考 ？
    - 从Chrome浏览器导出 SSLKEYLOGFILE
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
    - 参考 https://docs.mitmproxy.org/stable/howto-wireshark-tls/
    - 因为Charles无法导出SSLKEYLOGFILE
    - 手机WiFi代理设置，192.168.0.222  端口 8080
    - iPhone上要安装mitmproxy的ssl证书，提前装好
    - ping httpbin.org
        - 服务器IP 52.44.66.161
    - curl  https://httpbin.org/ip
    - 启动mitmproxy
        - SSLKEYLOGFILE="~/.mitmproxy/sslkeylogfile.txt" mitmproxy
    - 启动 WireShark，监听有线网卡
    - curl -k -x 127.0.0.1:8080 https://httpbin.org/ip
- 启动手机
    - 打开浏览器 
        - http://httpbin.org/ip
        - https://httpbin.org/ip
- WireShark过滤
    - dns
    - http
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
    
    - DNS livenging.alicdn.com
        - Queries
            - livenging.alicdn.com: type A, class IN
        - Answers
            - livenging.alicdn.com.danuoyi.alicdn.com: type A, class IN, addr 202.108.249.186
            - livenging.alicdn.com.danuoyi.alicdn.com: type A, class IN, addr 202.108.249.185
        - 然后 过滤
            - ip.dst == 202.108.249.186
            - ip.dst == 202.108.249.186
    - 找不到 m3u8文件
        - http contains ".m3u8"

