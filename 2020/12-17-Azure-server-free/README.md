## 免费Azure服务器

- 视频 [【亲测有效】申请微软Azure服务器免费12个月](https://www.bilibili.com/video/BV12p4y1q7t7/)

- 参考
    - [申请微软Azure服务免费12个月+$200 额度+永久免费(25+项服务)](https://www.daniao.org/7057.html)
        - 首月送200美金，10T流量随意用
        - vps免费资源为1G内存/40G空间/15G月流量，持续一年。
        - 套路
            - 需要试用完200美元或者过了30天后，必须升级即用即付后，才能享受12个月免费服务
            - 免费12个月期间，如果产生扣费（比如流量超了）会在下个月账单中直接信用卡扣费。
            - 免费12个月到期后，订阅不会停止，已开通的免费资源会直接产生扣费
- 注册
    - 活动 [通过 12 个月的免费服务开始使用](https://azure.microsoft.com/zh-cn/free/)
    - 一张信用卡，验证卡的时候扣费1美刀！（VISA或者万事达，且没有激活过其他账号）
- 创建虚拟机vps
    - 选择配置的时候一定要选择标准 B1s这个配置
        - 只有它才免费
    - 创建用户时，建议使用 【ssh密钥】，到时登录不需要密码，很方便
    - 创建完成后
        - 【网络】添加【入站端口】
    - 登录服务器
        - ssh 【你的账号】@【你的IP】
            - ssh ms@168.62.xxx.xxx
- 翻墙
    - Nginx反向代理
    - Squid代理
        - 用来做爬虫
        - 参考 
            - 搭建 https://www.linuxidc.com/Linux/2019-08/159960.htm
            - squid搭建高匿名代理服务 https://www.jianshu.com/p/96c8f1f7fd17
        - 测试
            - curl -x 你的IP:3128 http://httpbin.org/ip
    - SSR
        - 比较复杂
        - 微软发公告禁止翻墙
    - ssh 隧道
        - 最简单
        - 先登录服务器 ssh -f -NC -D 2345 ms@168.62.xxx.xxx
            - sock5代理，端口是2345
            - 然后在Chrome浏览器的【Proxy SwitchyOmega】插件设置代理
                - 代理协议是SOCKS5,IP是127.0.0.1，端口是2345
            - 测试
                - curl --socks5 localhost:2345 http://httpbin.org/ip

- Python 虚拟环境
    - sudo apt-get install python3-pip
    - pip3 install virtualenv
    - virtualenv  -p /usr/bin/python3.6 .py3
    - 把source ~/.py3/bin/activate 
        - 加到~/.bashrc末尾
        - 这样，每次登录服务器，就能自动使用Python 虚拟环境
        
- YouTube视频
    - pip3 install youtube_dl
    - sudo apt  install ffmpeg
    - pip3 install python-ffmpeg-video-streaming
    - 下载视频
        - 从服务器到本机
            - 使用Nginx
                - sudo ln -s /home/ms/video/ /var/www/html/video
                - 修改Nginx配置，添加【目录遍历】
                    - 参考 https://blog.csdn.net/ddazz0621/article/details/85338671
                - 打开 http://服务器IP/video/
            - 可以使用ftp，比较慢
            - 使用Flask ，比较快，1 m/s
                - response=send_file(fp,as_attachment=True,attachment_filename=filename)
    - 使用m3u8在线观看，hls流式播放
        - https://github.com/newnewcoder/flask-hls-demo
        - https://github.com/aminyazdanpanah/python-ffmpeg-video-streaming
        - 问题，ts文件大，网速慢，体验差
```
(.py3) ms@f1:~/video$ youtube-dl https://www.youtube.com/watch?v=79aP7BhrbuI
[youtube] 79aP7BhrbuI: Downloading webpage
[youtube] 79aP7BhrbuI: Downloading MPD manifest
[download] Destination: The world's top 10 ultimate travel experiences-79aP7BhrbuI.mp4
[download] 100% of 29.18MiB in 00:01
```
- Google Earth Studio
    - 翻墙后，配置Chrome浏览器的【Proxy SwitchyOmega】插件
        - 打开 https://earth.google.com/studio/
        - 需要申请，很快通过，当天
        - 新建工程，然后调整视角，地点
        - 渲染，它会自动导出高分辨率的图片到你的电脑
            - 然后使用【视频剪辑软件】合并成视频
                - 使用FFmpeg命令行
                    - 参考 https://blog.csdn.net/wangshuainan/article/details/77914508
                    - ffmpeg  -i  测试1_%03d.jpeg -vcodec libx264 -r 30  test.mp4
                        - 【测试1】 为工程名称
                        - 图片：测试1_441.jpeg
                        - -r 30 帧率
                        - -vcodec libx264 编码器
                        - 视频[【测试】Google Earth Studio 样片，使用ffmpeg合成，无声](https://www.bilibili.com/video/BV1yp4y1q7Nw/)

                - 使用moviepy
                