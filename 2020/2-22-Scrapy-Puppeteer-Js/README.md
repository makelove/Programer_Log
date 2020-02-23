## Scrapy使用Puppeteer中间件抓取JS动态页面
- 视频 ？

## 1. JS动态页面

## 2. Go server
- go run js_server.go
- flask server
	- python3 js_server.py

## 3. Scrapy爬虫，中间件
- scrapy crawl example  -s CLOSESPIDER_ITEMCOUNT=1000
	- spider的parse函数要yield item

## 4. 运行测试
- 启动Docker
    - 运行 Puppeteer
        - docker run  -it --name renderer -p 8080:3000 zenato/puppeteer-renderer
    - 测试
        - curl http://localhost:8080/?url=http://192.168.0.222:8888/
    - scrapy shell 'http://192.168.0.222:8888/'
    - scrapy shell 'http://localhost:8080/?url=http://192.168.0.222:8888/'

## 5. 压力测试 ab
```
测试工具Apache ab
http://httpd.apache.org/docs/2.2/programs/ab.html
ab -q -c 50 -n 1000 http://192.168.0.222:8888/
－n表示请求数，－c表示并发数
Go:
Requests per second:    7109.04 [#/sec] (mean)
Flask:
Requests per second:    293.62 [#/sec] (mean)

ab  -c 50 -n 1000 http://localhost:8080/?url=http://192.168.0.222:8888/
ab  -c 32 -n 200 http://localhost:8080/?url=http://192.168.0.222:8888/
Go:
Requests per second:    8.82 [#/sec] (mean)
Flask:
Requests per second:    8.27 [#/sec] (mean)
```

## 6. 优化 ？瓶颈 ！
- 修改docker Puppeteer index.js
- 增大并发量
- 同时打开多个Chrome窗口，占用更多的内存
