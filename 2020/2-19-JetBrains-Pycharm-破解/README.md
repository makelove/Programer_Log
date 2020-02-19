# JetBrains全家桶 破解

- 常用 PyCharm 、GoLand、WebStorm、IntelliJ IDEA
    - Clion、AppCode、Kotlin
- 免费领取正版，不用破解
    - 教育网后缀的email
    - 开源项目 https://zhuanlan.zhihu.com/p/87370573

- 怎样破解
    - 不需要断网
    - 不需要改host
        - 0.0.0.0 account.jetbrains.com
    - 把jetbrains-agent.jar放到pycharm的lib目录
    - 启动pycharm，输入激活码
    - 上面的步骤对JetBrains全家桶都有效。
        - 本人测试了GoLand破解，没问题

- 如果PyCharm 专业版不能激活，可以用【社区版】

- 代替
    - VScode
        - 免费
        - 功能齐全

- VScode 调试程序
- Python
```
        {
            "name": "pyLaunch",
            "type": "python",
            "request": "launch",
            "mode": "auto",
            "pythonPath": "${config:python.pythonPath}",
            "program": "${file}",
            "env": {},
            "args": []
        }
```

- Go
```
        {
            "name": "goLaunch",
            "type": "go",
            "request": "launch",
            "mode": "auto",
            "program": "${fileDirname}",
            "env": {},
            "args": []
        }
然后要创建mod文件
go mod init example.com/m
```
