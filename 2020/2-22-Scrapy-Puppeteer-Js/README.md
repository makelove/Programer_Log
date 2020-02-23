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
    - express ?
- 增大并发量
- 同时打开多个Chrome窗口，占用更多的内存
```
(.py3) localhost:~ play$ docker ps
CONTAINER ID        IMAGE                       COMMAND                  CREATED             STATUS              PORTS                    NAMES
c7fb712736d3        zenato/puppeteer-renderer   "/bin/sh -c 'npm run…"   7 weeks ago         Up About an hour    0.0.0.0:8080->3000/tcp   renderer

#进入docker镜像
(.py3) localhost:~ play$ docker exec -it renderer /bin/bash
root@c7fb712736d3:/app# cat Dockerfile
FROM zenato/puppeteer

USER root

COPY . /app

RUN cd /app && npm install --quiet

EXPOSE 3000

WORKDIR /app

CMD npm run start
root@c7fb712736d3:/app# ls -l
total 144
-rw-r--r--   1 root root    128 Dec 18 23:52 Dockerfile
-rw-r--r--   1 root root   1091 Dec 18 23:52 LICENSE
-rw-r--r--   1 root root   3293 Dec 18 23:52 README.md
drwxr-xr-x   3 root root   4096 Dec 18 23:52 middleware
drwxr-xr-x 266 root root  12288 Dec 18 23:58 node_modules
-rw-r--r--   1 root root     23 Dec 18 23:52 now.json
-rw-r--r--   1 root root 101140 Dec 18 23:58 package-lock.json
-rw-r--r--   1 root root    737 Dec 18 23:52 package.json
drwxr-xr-x   2 root root   4096 Dec 18 23:52 src
drwxr-xr-x   2 root root   4096 Dec 18 23:52 test
root@c7fb712736d3:/app# ls src/
index.js  renderer.js

#源代码
root@c7fb712736d3:/app# cat src/index.js
'use strict'

const express = require('express')
const qs = require('qs')
const { URL } = require('url')
const contentDisposition = require('content-disposition')
const createRenderer = require('./renderer')

const port = process.env.PORT || 3000

const app = express()

let renderer = null

// Configure.
app.set('query parser', s => qs.parse(s, { allowDots: true }))
app.disable('x-powered-by')

// Render url.
app.use(async (req, res, next) => {
  console.log(req.query)
  let { url, type, filename, ...options } = req.query

  if (!url) {
    return res.status(400).send('Search with url parameter. For eaxample, ?url=http://yourdomain')
  }

  if (!url.includes('://')) {
    url = `http://${url}`
  }

  try {
    switch (type) {
      case 'pdf':
        const urlObj = new URL(url)
        if (!filename) {
          filename = urlObj.hostname
          if (urlObj.pathname !== '/') {
            filename = urlObj.pathname.split('/').pop()
            if (filename === '') filename = urlObj.pathname.replace(/\//g, '')
            const extDotPosition = filename.lastIndexOf('.')
            if (extDotPosition > 0) filename = filename.substring(0, extDotPosition)
          }
        }
        if(!filename.toLowerCase().endsWith('.pdf')) {
          filename += '.pdf';
        }
        const pdf = await renderer.pdf(url, options)
        res
          .set({
            'Content-Type': 'application/pdf',
            'Content-Length': pdf.length,
            'Content-Disposition': contentDisposition(filename),
          })
          .send(pdf)
        break

      case 'screenshot':
        const { screenshotType, buffer } = await renderer.screenshot(url, options)
        res
          .set({
            'Content-Type': `image/${screenshotType}`,
            'Content-Length': buffer.length,
          })
          .send(buffer)
        break

      default:
        const html = await renderer.render(url, options)
        res.status(200).send(html)
    }
  } catch (e) {
    next(e)
  }
})

// Error page.
app.use((err, req, res, next) => {
  console.error(err)
  res.status(500).send('Oops, An expected error seems to have occurred.')
})

// Create renderer and start server.
createRenderer({
  ignoreHTTPSErrors: !!process.env.IGNORE_HTTPS_ERRORS,
})
  .then(createdRenderer => {
    renderer = createdRenderer
    console.info('Initialized renderer.')

    app.listen(port, () => {
      console.info(`Listen port on ${port}.`)
    })
  })
  .catch(e => {
    console.error('Fail to initialze renderer.', e)
  })

// Terminate process
process.on('SIGINT', () => {
  process.exit(0)
})
root@c7fb712736d3:/app#
```

