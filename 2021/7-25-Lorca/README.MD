
什么是Lorca？
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