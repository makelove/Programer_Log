# Docker+Puppeteer抓取动态页面
- 视频 https://www.bilibili.com/video/av81253564/

### 问题
爬虫怎样抓取Js动态页面？例如电商网站的价格，销量

## 常规解决方案
安装firefox selenium python

- 问题
    - 1 安装麻烦，配置麻烦
    - 2 本地配置好了，不方便部署到服务器
    - 3 效率低下

## 解决
Docker+Puppeteer(Chrome headless node API) 

1. 自定义脚本
    - https://hub.docker.com/r/alekzonder/puppeteer

    - 下载
        - docker pull alekzonder/puppeteer

    - 运行
        - docker run --shm-size 1G --rm -v /Users/play/Temp/puppeteer/docker-puppeteer-pdf.js:/app/index.js -v /Users/play/Temp/puppeteer:/puppeteer alekzonder/puppeteer:latest
    - 查看PDF



2. 渲染中间件-动态网页
    - https://hub.docker.com/r/zenato/puppeteer-renderer
    - 源代码 https://github.com/zenato/puppeteer-renderer

- 运行
    - docker run  -it --name renderer -p 8080:3000 zenato/puppeteer-renderer

- 测试
    - curl http://localhost:8080/?url=https://ip.cn/

## Scrapy 爬虫 抓取Js动态页面
- 参考  [scrapy如何在中间件修改请求url](https://blog.csdn.net/wang785994599/article/details/97887294)
- 在middlewares.py编写中间件

```
from urllib.parse import quote
class Puppeteer(object):
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls(crawler)
        # crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def __init__(self, crawler):
        self.host = 'http://localhost:8080/?url='

    def process_request(self, request, spider):
        request.meta['url'] = request.url
        
        url = self.host + quote(request.url)
        request._set_url(url)
        pass

    def process_response(self, request, response, spider):
        response._set_url(request.meta['url'])
        return response

    pass
```

- 在settings.py 加入

```
DOWNLOADER_MIDDLEWARES = {
   'demo.middlewares.Puppeteer': 543,
}
```

- 缺点
    - 不能更改Puppeteer的UserAgent ？！！
        - 只能修改index.js 源代码
