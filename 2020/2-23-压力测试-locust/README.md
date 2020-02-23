# 2-23-压力测试-locust
- 参考 
    - [locust是一个易于使用的，分布式的，用户负载测试工具](http://blog.timd.cn/python-locust/)
- 常用的压力测试有
    - Apache ab 命令行工具
        - http://httpd.apache.org/docs/2.2/programs/ab.html
    - Locust 蝗虫 https://locust.io/
        - 案例文档 https://docs.locust.io/en/stable/quickstart.html
        - 安装 pip3 install locust
        - 好处是 可以编写Python程序，自定义测试流程。有后台界面

- 测试
    - ab －c表示并发数 －n表示请求数
        - ab -c 50 -n 200 http://127.0.0.1:8080/  
    -  Locust
        - locust -f locust-get.py 
            - 打开浏览器 http://127.0.0.1:8089/
        - 命令行运行
            - locust -f locust-get.py --no-web -c 50 -r 200