# 使用docker运行OpenCV+golang
- 参考
    - https://github.com/hybridgroup/gocv
    - https://hub.docker.com/r/hybridgroup/gocv

- 结论
    - docker+gocv 可以作为服务器程序，在服务器上高速执行

- 首先 pull docker
    - docker pull hybridgroup/gocv
    - 运行后
        - 发现golang版本太低，不能执行代码，需要升级   
    
下载 go1.13.3.linux-amd64.tar.gz
https://dl.google.com/go/go1.13.3.linux-amd64.tar.gz 不行
https://studygolang.com/dl/golang/go1.13.3.linux-amd64.tar.gz

docker run -it  -v /Users/play/github/gocv:/gocv hybridgroup/gocv
进入后，解压，即可
```shell script
    1  cd /gocv/
    2  rm -rf /usr/local/go
    3  tar -C /usr/local -xzf go1.13.3.linux-amd64.tar.gz
    4  go version

```
退出
```shell script
(.py3) pro:~ play$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES
f2dc43cabe71        hybridgroup/gocv    "/bin/bash"         12 minutes ago      Exited (0) 2 seconds ago                       hopeful_lehmann
ec9d94cacbe1        pypy:3.6            "pypy3"             16 hours ago        Exited (0) 16 hours ago                        admiring_vaughan

#将容器打包成一个新的镜像
(.py3) pro:~ play$ docker commit  f2dc43cabe71 gocv:go1.13
sha256:033be3d5044d7f84ff552255e0c7f3d1da7c92d3a462342d37799b3f02f519fa
(.py3) pro:~ play$ docker image ls |grep gocv
gocv 				go1.13              033be3d5044d        16 seconds ago      1.5GB
hybridgroup/gocv    latest              f236ffa190b7        7 weeks ago         1.14GB


#测试
docker run -it  -v /Users/play/github/gocv:/gocv  gocv:go1.13
root@d7b692fdda37:/gocv/cmd/version# go run main.go
gocv version: 0.21.0
opencv lib version: 4.0.1
root@d7b692fdda37:/gocv/cmd/version# go version
go version go1.13.3 linux/amd64

```

- 执行脸部识别程序
```shell script
root@d7b692fdda37:/gocv/cmd/facedetect# cd /gocv/cmd/facedetect-from-url/
root@d7b692fdda37:/gocv/cmd/facedetect-from-url# go build  -o facedetect main.go
root@d7b692fdda37:/gocv/cmd/facedetect-from-url# ll -h
total 8.3M
drwxr-xr-x  4 root root  128 Jan  1 03:36 ./
drwxr-xr-x 30 root root  960 Dec  2 10:39 ../
-rwxr-xr-x  1 root root 8.3M Jan  1 03:36 facedetect*
-rw-r--r--  1 root root 1.9K Dec  2 11:04 main.go
root@d7b692fdda37:/gocv/cmd/facedetect-from-url# ./facedetect
How to run:
	facedetect-from-url [image URL] [classifier XML file] [image file]

root@d7b692fdda37:/gocv/cmd/facedetect-from-url# ./facedetect https://raw.githubusercontent.com/hybridgroup/gocv/master/images/face.jpg  ../../data/haarcascade_frontalface_default.xml output2.jpg

[./facedetect https://raw.githubusercontent.com/hybridgroup/gocv/master/images/face.jpg ../../data/haarcascade_frontalface_default.xml output2.jpg]
Get(imageURL)
found 1 faces
saved to output2.jpg

root@d7b692fdda37:/gocv/cmd/facedetect-from-url# ll -h
total 8.3M
drwxr-xr-x  5 root root  160 Jan  1 03:38 ./
drwxr-xr-x 31 root root  992 Jan  1 03:38 ../
-rwxr-xr-x  1 root root 8.3M Jan  1 03:36 facedetect*
-rw-r--r--  1 root root 1.9K Dec  2 11:04 main.go
-rw-r--r--  1 root root  39K Jan  1 03:38 output2.jpg
```


- 大问题：不能编译跨平台程序，因为OpenCV
    - 在Linux编译macOS程序
```shell script
root@d7b692fdda37:/gocv/cmd/showimage# CGO_ENABLED=0 GOOS=darwin GOARCH=amd64 go build main.go
# gocv.io/x/gocv
/gocv/dnn_ext.go:9:28: undefined: Mat
/gocv/dnn_ext.go:16:12: undefined: NewMatWithSize
/gocv/dnn_ext.go:42:2: undefined: Resize
/gocv/dnn_ext.go:42:38: undefined: InterpolationDefault
/gocv/dnn_ext.go:45:3: undefined: CvtColor
/gocv/dnn_ext.go:48:15: undefined: NewMat
/gocv/dnn_ext.go:51:31: undefined: MatTypeCV32F

```