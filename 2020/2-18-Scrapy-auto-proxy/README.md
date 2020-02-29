# Scrapy 爬虫自动调整IP代理
- 视频 [Scrapy爬虫自动调整IP代理，避免失效](https://www.bilibili.com/video/av89959782/)
- 问题
    - IP代理失效
    
    
## 启动Docker
- 参考 https://github.com/makelove/Programer_Log/tree/master/2020/2-7-Docker-Nginx-antiClawer
- 启动 http server
```shell script
(.py3) localhost:2-7-Docker-Nginx-antiClawer play$ go run server.go
Server starting on port 8080
curl http://127.0.0.1:8080/
curl http://192.168.0.222:8080/

```
- 启动Nginx
```shell script
(.py3) localhost:2-7-Docker-Nginx-antiClawer play$ docker run -it --rm -p 80:80 -v `pwd`/nginx1.conf:/etc/nginx/nginx.conf:ro nginx

172.17.0.1 - - [18/Feb/2020:11:44:54 +0000] "GET /api HTTP/1.1" 403 153 "-" "curl/7.64.1"
172.17.0.1 - - [18/Feb/2020:11:45:28 +0000] "GET /api HTTP/1.1" 200 49 "-" "iphone"

#测试
curl -A 'iphone'  http://192.168.0.222/api
```

- 启动 Squid 代理服务器
```shell script
docker run -it --rm -p 3121:3128  datadog/squid
docker run -it --rm -p 3122:3128  datadog/squid
docker run -it --rm -p 3123:3128  datadog/squid
docker run -it --rm -p 3124:3128  datadog/squid
```
- 测试代理
```shell script
curl -A 'iphone' -x 127.0.0.1:3121  http://192.168.0.222/api
curl -A 'iphone' -x 127.0.0.1:3121  http://httpbin.org/ip
```
- 启动Redis
    - 必须 Redis 5.0.7 64 bit
```shell script
docker run -it --rm -p 6379:6379  redis
#测试
redis-cli

```

- 编写Scrapy代码
    - 使用2-6-Spider-Speed-test 的scrapy_demo代码
    - 新建middlewares_proxy_redis.py
    - 在settings.py加入DOWNLOADER_MIDDLEWARES
        - 'scrapy_demo.middlewares_proxy_redis.redisProxy': 400,
    - 把代理插入Redis服务器
        - manage_proxy.py

- 运行爬虫测试
    -  scrapy crawl example -s CLOSESPIDER_ITEMCOUNT=1000
    
- 测试效果
    - Nginx 配置，要正确
        - limit_conn_zone $binary_remote_addr zone=perip:100k;
        - limit_conn_zone $server_name zone=perserver:100k;
    - 数值如果太大，就看不出效果