# Nginx反爬虫
- 视频 https://www.bilibili.com/video/av87302823/
- 参考 
    - https://blog.csdn.net/weixin_34341117/article/details/85848963
    - agent_deny.conf https://blog.csdn.net/markchiu/article/details/52512106
    - Nginx 服务器之速率限制 https://cloud.tencent.com/developer/news/35222

- 启动Docker

- 禁止某UserAgent
    - curl访问

- 限制同一个ip的访问频率
    速率限制主要有2个主要指令，limit_req_zone和limit_req。


- 运行
    - 启动server
        - go run server.go
    - docker run -it --rm -p 80:80 -v /path/nginx1.conf:/etc/nginx/nginx.conf:ro nginx

- 测试
    - curl  http://192.168.0.222/api
    - curl -A 'iphone'  http://192.168.0.222/api

- 限制IP
    - 之前 
        - 速度: 9970.065281182719  item/minute , 314 0.03149427723333333
    - 之后
        - 速度: 2134.1611919528164  item/minute , 61 0.02858265825
        - Nginx日志
            - 2020/02/07 06:29:34 [error] 6#6: *422 limiting connections by zone "perip", client: 172.17.0.1, server: localhost, request: "GET /api HTTP/1.1", host: "127.0.0.1"