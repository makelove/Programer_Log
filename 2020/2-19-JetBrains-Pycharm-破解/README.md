# JetBrains全家桶 破解

- 视频  [JetBrains全家桶用不了？用VScode代替PyCharm](https://www.bilibili.com/video/av90073564/)

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

- 使用VScode编程Go语言
    - 参考 https://github.com/makelove/Programer_Log/tree/master/2020/2-18-Docker-Go-goProxy
    - 步骤
        - 设置环境变量
            - export GO111MODULE=on
            - export GOPROXY=https://goproxy.cn
        - 下载VScode的插件【Go for Visual Studio Code】
            - 参考 https://github.com/microsoft/vscode-go
        - 便可以自动import go 模块了
    - 另外，你在命令行 go build main.go时，Go 会自动下载模块