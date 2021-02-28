# [Programer_Log 我的程序员日志](https://github.com/makelove/Programer_Log)


- 有问题，请写到issue里面
    - 加我微信WeChat: sexy8dream

- 因为raw.githubusercontent.com被墙了，你们会看到图片挂了
    - 加入/etc/hosts
        - 151.101.156.133 raw.githubusercontent.com
            - India印度服务器
- 下载download
    - Download ZIP
    - git
        - git clone https://github.com/makelove/Programer_Log.git
        - 更新 git fetch origin master  

- Donate点赞打赏，助人为乐^_^
    - <img src="wechat_donate.jpg" width = "200" height = "261" alt="wechat_donate"  />


- 重要列表
    - [越狱？最简单的代理服务器Go，翻墙，Chrome插件](2020/2-26-Go_Proxy_server)
        - 在国外服务器Azure测试了，不能直接使用，需要加密算法，。很容易被识别,被拦截
            - curl -x 168.62.xxx.xxx:8081 https://httpbin.org/ip
                - 正常返回IP
            - curl -x 168.62.xxx.xxx:8081 https://kh.google.com
                - curl: (56) Recv failure: Connection reset by peer