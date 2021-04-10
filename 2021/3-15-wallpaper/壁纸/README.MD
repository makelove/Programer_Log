

- golang 设置 墙纸 win10
    - https://blog.csdn.net/singleyellow/article/details/83714790
    - https://blog.csdn.net/CodyGuo/article/details/73013557
    
    
- Windows 下执行wp2.exe 每次将会更换墙纸

- 编译
    - go build -v -o wp_macos wp2.go
    - CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build -v -o wp_win10.exe wp2.go