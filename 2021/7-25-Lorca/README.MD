
- 视频 [【编程】Lorca-Go语言-跨平台-桌面应用开发框架-比Electron好用，在 Go + HTML5 中构建跨平台的现代桌面应用程序](https://www.bilibili.com/video/BV1Tg411779a/)

## 什么是Lorca？
Go语言的桌面应用开发框架

- 对比Electron
    - Go语言，执行效率快。二进制程序
        - Node.js 需要V8引擎 Chome
    - 结构简单
    - 代码加密，很难破解
        - 还可以加壳
        - Electron可以混扰代码，增加阅读难度，但是代码可以恢复，只要花点时间 assr
    - 打包方便，一个文件搞定
        - 文件很小，不到10M
        - Electron即使是最小应用，也有100M
            - Electron会打包 node_modules
    - 跨平台方便
    - 唯一的问题
        - Lorca依赖Chrome浏览器，需要在系统里提前安装

- 特征
    - 带有非常简单的 API 的纯 Go 库（无 cgo）
    - 小应用程序大小（通常 5-10MB）
    - 两全其美 - HTML/CSS 的全部力量使您的 UI 看起来不错，结合 Go 性能和易于开发
    - 公开 Go 函数/方法并从 JavaScript 调用它们
    - 从 Go 调用任意 JavaScript 代码
    - 两种语言的 UI 和主应用程序之间的异步流（async/await 和 Goroutines）
    - 支持从本地 Web 服务器或通过数据 URL 加载 Web UI
    - 支持在无头模式下使用 UI 测试您的应用
    - 支持多个应用程序窗口
    - 支持包装和品牌（例如自定义应用程序图标）。可以使用 GOOS 和 GOARCH 变量在一台机器上完成所有三个操作系统的打包。
- 此外，设计限制：
    - 需要安装 Chrome/Chromium >= 70。
    - 尚无法控制 Chrome 窗口（例如，您无法移除边框、使其透明、控制位置或大小）。
    - 没有窗口菜单（托盘菜单和本机操作系统对话框仍然可以通过 3rd-party 库）



网址 ？
https://github.com/zserge/lorca/tree/master/examples
https://github.com/zserge/lorca/tree/master/examples/counter


错误
go run main.go 
build command-line-arguments: cannot load embed: malformed module path "embed": missing dot in first path element

需要安装 Go 1.16 RC1 才能运行它。

运行
go1.16 mod init counter
go1.16 get github.com/zserge/lorca
go1.16 run main.go 

chmod -R  777  Example.app/
go1.16 build -o Example.app/Contents/MacOS/lorca-example
编译Windows CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go1.16 build -v -o counter_win10 main.go 