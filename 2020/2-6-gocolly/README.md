## gocolly 爬虫 入门和案例

- 视频：

- 参考
    - https://github.com/gocolly/colly
    - 官网 http://go-colly.org/
    - 官网文档 http://go-colly.org/docs/

- 安装
    - go get -u github.com/gocolly/colly/v2/...

- 案例
    - 解析HTML
        - CSS Selector
        - 京东-商品列表
    - 异步并发请求
        - colly.Async(true),
        - c.Wait()
    - 使用多个Collector解析器
        - detailCollector := c.Clone()
        - context传参

            var ctx=colly.NewContext()
            ctx.Put("cc", js.Cc) 
            c.Request("GET", url, nil, ctx, header)

    - 使用代理
        - httpbin get.go
        - 启动Squid代理服务器
    - 分布式抓取，连接Redis
        - 1