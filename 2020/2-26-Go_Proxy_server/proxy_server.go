/*
@File    :   proxy_server1.go
@Time    :   2020/02/24 20:55:11
@Author  :   play4fun
@Desc    :   d

一个简单的Golang实现的HTTP Proxy
https://www.flysnow.org/2016/12/24/golang-http-proxy.html
使用HTTP／1.1协议中的CONNECT方法建立起来的隧道连接，实现的HTTP Proxy。
这种代理的好处就是不用知道客户端请求的数据，只需要原封不动的转发就可以了，
对于处理HTTPS的请求就非常方便了，不用解析他的内容，就可以实现代理。

测试
curl -x 127.0.0.1:8081  http://httpbin.org/ip
curl -x 127.0.0.1:8081  https://httpbin.org/ip

curl -x 42.56.89.102:8081  https://httpbin.org/ip
*/

package main

import (
	"bytes"
	"fmt"
	"io"
	"log"
	"net"
	"net/url"
	"strings"
)

func main() {
	log.SetFlags(log.LstdFlags | log.Lshortfile)
	l, err := net.Listen("tcp", ":8081") //监听端口
	if err != nil {
		log.Panic(err)
	}

	for {
		client, err := l.Accept() //阻塞

		log.Println("新请求")
		if err != nil {
			log.Panic(err)
		}

		go handleClientRequest(client)
	}
}

func handleClientRequest(client net.Conn) {
	if client == nil {
		return
	}
	defer client.Close()

	var b [1024]byte
	n, err := client.Read(b[:]) //读取请求
	if err != nil {
		log.Println(err)
		return
	}

	//解析请求参数
	var method, host, address string
	fmt.Sscanf(string(b[:bytes.IndexByte(b[:], '\n')]), "%s%s", &method, &host)
	log.Println("Visit: ", host)
	hostPortURL, err := url.Parse(host)
	if err != nil {
		log.Println(err)
		return
	}

	if hostPortURL.Opaque == "443" { //https访问
		address = hostPortURL.Scheme + ":443"
	} else { //http访问
		if strings.Index(hostPortURL.Host, ":") == -1 { //host不带端口， 默认80
			address = hostPortURL.Host + ":80"
		} else {
			address = hostPortURL.Host
		}
	}

	//获得了请求的host和port，就开始拨号吧
	server, err := net.Dial("tcp", address)
	if err != nil {
		log.Println(err)
		return
	}
	if method == "CONNECT" {
		fmt.Fprint(client, "HTTP/1.1 200 Connection established\r\n\r\n")
	} else {
		server.Write(b[:n])
	}
	//进行转发
	go io.Copy(server, client)
	io.Copy(client, server)
}
