# 用docker模拟Nginx限制同一个爬虫ip的访问频率

- Nginx配置
https://blog.csdn.net/weixin_34341117/article/details/85848963
使用golang的tollbooth模块代替
https://github.com/didip/tollbooth

- Docker

1.启动busybox
docker run -it -p 84:4000 --volume /Users/play/CODE/GO/HTTP请求限流/tollbooth1:/go busybox
cd /go/
/go # ./demo3_linux
网址
curl http://192.168.0.111:84/ip
查看IP
docker exec -it container1 ip addr
172.17.0.2

2.启动代理
docker run -it -p 3129:3128 --name=squid3  datadog/squid
测试
curl -x localhost:3129 http://172.17.0.2:4000/ip

3.批量测试
```shell script
#!/bin/bash

for((i=1;i<=10;i++));
do
curl -x localhost:3129 http://172.17.0.2:4000/ip ;
echo ""
echo "-------"
done
```

4. Python测试
```python
import requests
from time import sleep
url='http://172.17.0.2:4000/ip'
proxies = {
  "http": "http://localhost:3129",
  "https": "http://localhost:3129",
}
for i in range(200):
    rs=requests.get(url,proxies=proxies)
    print(rs.status_code,rs.text)
    if rs.status_code==429:
        sleep(0.3)
```