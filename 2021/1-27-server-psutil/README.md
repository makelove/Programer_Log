
## 监控服务器，并向钉钉报警

- 视频 [【编程】监控服务器，并向钉钉报警，Python  psutil DingtalkChatbot crontab](https://www.bilibili.com/video/BV1Yv411s73w/)

- 推荐图书
    - [Python自动化运维：技术与最佳实践](https://union-click.jd.com/jdc?e=&p=AyIGZRhfHQARDlMTWRUyEgZUGF8RAxQBVRNZHQIiQwpDBUoyS0IQWhkeHAxBFQQAQB1AWQkFGk1dRFkRdQtUWgxxAV4pVEBkRAtfGhtASEM7Qw4ZAhMGVh9fFAQUB10ZUxUVRUQLR1dHQ1AQAlgFSQ5ARhcrW09SVno0YBN3QBFVBxM7EUVVDlRGKxkOIgZlG1oUAxYOVh9SFzIiB1IrGnsCEwNSGF0UAyIGZRtcFQIbD1AfXRIAEg5lHFscMkJbBVADSlQRBlATayUyETdlK1slASJFO09aQgRCAgZLCBBQGgIGTw9GB0dUXR1fF1YVB1QTXBILIgVUGl8c)
    - [Python自动化运维快速入门](https://union-click.jd.com/jdc?e=&p=AyIGZRhYFQcQBFQTWRMyEgZUGFwUBxYCVRhTEAsiQwpDBUoyS0IQWhkeHAxBFQQAQB1AWQkFGk1dRFkRdQtUWgxxAV4pVEBkRAtfGhtASEM7Qw4ZAhMGVhxaEAYXB1YTXhwVRUQLR1dHQ1AQAlgFSQ5ARhcrIRBBSVojXQR1XRVPCEEuD39xbApBKxkOIgZlG1oUAxYOVh9SFzIiB1IrGnsCEwVRE1McByIGZRtcFQIbD1AcWhUAGwdlHFscMkJbBVADSlQRBlATayUyETdlK1slASJFO09aQgRCAgZLCBBQGgIGTw9GB0dUXR1fF1YVB1QTXBILIgVUGl8c)

- psutil https://pypi.org/project/psutil/
    - 安装
        - pip install psutil
    - 硬盘
        - disk = psutil.disk_usage('/')
    - 内存
        - mem = psutil.virtual_memory()
    - CPU
        - cpup = psutil.cpu_percent(interval=10)
    - IP
        - psutil.net_if_addrs()

- 钉钉 https://github.com/zhuifengshen/DingtalkChatbot
    - 新建 群聊
    - 新建 机器人
        - webhook
            - https://oapi.dingtalk.com/robot/send?access_token=xx
        - 密钥 可以重置
            - xx
    - api

- 服务器部署
    - 多台服务器，部署麻烦
        - Python跨平台打包 pyinstaller
        - 使用 docker 
        - golang 语言
        
    - 安装Python3
        - CentOS
            - yum  install python36u-pip
        - Ubuntu 
            - apt-get install python3.6
        - pip install virtualenv 
        - 找出python3的位置
            - which python3
                - /usr/bin/python3.6
    - 虚拟环境
        - virtualenv -p /usr/bin/python3.6 ~/py36
        - 激活虚拟环境 source ~/py36/bin/activate
        - 安装 lib
            - pip install psutil
            - pip install DingtalkChatbot
        - 测试 
            - which python3
            - /home/work/py36/bin/python3 /home/work/python/server_report.py
            
    - crontab 定时执行 [一文精通 crontab从入门到出坑](https://zhuanlan.zhihu.com/p/58719487)
        - crontab -e
        - 每隔20分钟执行
            - */20 * * * * /home/work/py36/bin/python3 /home/work/python/server_report.py
        - 早上9.00固定发送钉钉消息
            - * 9 * * * /home/work/py36/bin/python3 /home/work/python/server_report.py