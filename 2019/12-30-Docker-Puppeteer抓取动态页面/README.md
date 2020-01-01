# Docker+Puppeteer抓取动态页面
- 视频 https://www.bilibili.com/video/av81253564/
### 问题
爬虫怎样抓取动态页面？例如电商网站的价格，销量

### 常规解决方案
安装firefox selenium python
问题
1 安装麻烦，配置麻烦
2 本地配置好了，不方便部署到服务器
3 效率低下

### 解决
Docker+Puppeteer(Chrome headless node API) 

1. 自定义脚本
https://hub.docker.com/r/alekzonder/puppeteer

下载
docker pull alekzonder/puppeteer

运行
docker run --shm-size 1G --rm -v /Users/play/Temp/puppeteer/docker-puppeteer-pdf.js:/app/index.js -v /Users/play/Temp/puppeteer:/puppeteer alekzonder/puppeteer:latest
查看PDF



2. 渲染中间件-动态网页
https://hub.docker.com/r/zenato/puppeteer-renderer
源代码 https://github.com/zenato/puppeteer-renderer

运行
docker run  -it --name renderer -p 8080:3000 zenato/puppeteer-renderer

测试
curl http://localhost:8080/?url=https://ip.cn/
