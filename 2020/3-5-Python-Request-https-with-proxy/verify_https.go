/*
@File    :   verify_https.go
@Time    :   2020/03/07 09:38:20
@Author  :   play4fun
@Desc    :   同样的逻辑，用Go语言实现
*/

package main

import (
	"crypto/tls"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"net/url"
)

func main() {
	url2 := "https://httpbin.org/ip" // 小心同名 "net/url"
	proxy := "http://127.0.0.1:8080" //mitmproxy
	// proxy := "http://42.56.89.102:6159" //代理服务器Squid,OK

	urli := url.URL{}
	urlproxy, _ := urli.Parse(proxy)
	c := http.Client{
		Transport: &http.Transport{
			Proxy:           http.ProxyURL(urlproxy),               //设置代理
			TLSClientConfig: &tls.Config{InsecureSkipVerify: true}, //跳过证书验证
		},
	}
	if resp, err := c.Get(url2); err != nil {
		log.Fatalln(err)
		//2020/03/07 09:45:58 Get https://httpbin.org/ip: x509: certificate signed by unknown authority
		//exit status 1
	} else {
		defer resp.Body.Close()
		body, _ := ioutil.ReadAll(resp.Body)
		fmt.Printf("%s\n", body)
	}
}
