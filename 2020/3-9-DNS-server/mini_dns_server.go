/*
@File    :   mini_dns_server.go
@Time    :   2020/03/08 20:17:26
@Author  :   play4fun
@Desc    :   https://jameshfisher.com/2017/08/04/golang-dns-server/

测试
go run mini_dns_server.go
dig @127.0.0.1 www.free-proxy.com

设置为系统DNS ，运行正常

本地缓存 OK

下一步
GitHub gfw list


*/

package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net"
	"net/http"
	"strconv"

	"github.com/miekg/dns"
)

var domainsToAddresses map[string]string = map[string]string{
	// "google.com.":         "172.217.9.206",
	// "jameshfisher.com.":   "104.198.14.52",
	// "www.free-proxy.com.": "148.72.168.34",
	// "us1.free-proxy.com.": "148.72.168.34",
	// "us2.free-proxy.com.": "148.72.169.80",
}

type handler struct{}

func (this *handler) ServeDNS(w dns.ResponseWriter, r *dns.Msg) {
	msg := dns.Msg{}
	msg.SetReply(r)
	switch r.Question[0].Qtype {
	case dns.TypeA:
		msg.Authoritative = true
		domain := msg.Question[0].Name

		address, ok := domainsToAddresses[domain] //获取DNS
		if !ok {                                  //本地没有
			//查询网上
			url2 := "https://play4fun.pythonanywhere.com/dns?domain=" + domain
			res, _ := http.Get(url2)
			resp, _ := ioutil.ReadAll(res.Body)
			// fmt.Println(resp)
			fmt.Printf("%s", resp)
			type DIP struct {
				Domain string
				IP     string
			}
			var dip DIP
			err := json.Unmarshal(resp, &dip)
			if err != nil {
				fmt.Println("error:", err)
			}
			domainsToAddresses[domain] = dip.IP
			address = dip.IP
		}

		log.Println("domain:\t", domain, address, ok)
		//生成回复
		msg.Answer = append(msg.Answer, &dns.A{
			Hdr: dns.RR_Header{Name: domain, Rrtype: dns.TypeA, Class: dns.ClassINET, Ttl: 60},
			A:   net.ParseIP(address),
		})
	}
	fmt.Println("---------")
	w.WriteMsg(&msg) //回复
}

func main() {

	srv := &dns.Server{Addr: ":" + strconv.Itoa(53), Net: "udp"}
	srv.Handler = &handler{}

	if err := srv.ListenAndServe(); err != nil {
		log.Fatalf("Failed to set udp listener %s\n", err.Error())
	}

	// fmt.Println("---------")
	// c := make(chan os.Signal, 1)
	// signal.Notify(c, os.Interrupt, os.Kill)
	// s := <-c
	// fmt.Println("Got signal:", s)

	// //打印map
	// for domain := range domainsToAddresses {
	// 	fmt.Println(domainsToAddresses[domain], " :\t", domain)
	// }
}
