
# DNS查询 nameserver
- 视频 [DNS查询nameserver，用WireShark检查DNS报文，Python编程](https://www.bilibili.com/video/av96180822/)
- 参考 
    - [一个强大的基于 Go 的 DNS 库](https://zhengyinyong.com/post/go-dns-library/)

- DNS设置
    - cat /etc/resolv.conf

- 打开 WireShark
    - 过滤 dns
    - DNS 报文格式
    - 测试 
        - dig @114.114.114.114 www.free-proxy.com

- Python编程
```
import socket
host='www.bilibili.com'
socket.gethostbyname(host)
#'120.92.113.99'
```
- 指定 nameserver
    - https://github.com/rthalley/dnspython/tree/master/examples
```
import dns.resolver
resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['8.8.8.8']
answer = resolver.query('amazon.com', 'A')
for ans in answer.response.answer:
    print(ans)
    for rec in ans.items:
        print('ip ',rec)
```
- Go 编程
    - [一个强大的基于 Go 的 DNS 库](https://zhengyinyong.com/post/go-dns-library/)