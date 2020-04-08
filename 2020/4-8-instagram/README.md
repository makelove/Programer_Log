
# Instagram 爬虫

- 视频 ？

- 参考
    - GitHub
        - 搜索 https://github.com/search?l=Python&o=desc&q=instagram&s=stars&type=Repositories
        - 机器人 [Instagram Bot - Tool for automated Instagram interactions](https://github.com/timgrossmann/InstaPy)
        - 爬虫 [Instagram Scraper](https://github.com/rarcega/instagram-scraper)

- 观察网页，api
    - 俄罗斯美女 https://www.instagram.com/sabinaskerova/
        - 查看网页源代码，查找 _sharedData
        - 打开DevTool，Network面板，过滤 graphql/query

- 使用 Instagram Scraper 爬虫
    - 安装pip install instagram-scraper
    - 私人账号，必须是她的粉丝
        - `instagram-scraper <username> -u <your username> -p <your password> `    
    - instagram-scraper sabinaskerova --maximum 10 --proxies '{"http": "http://127.0.0.1:8118", "https": "http://127.0.0.1:8118" }'
    - instagram-scraper stationcdrkelly --maximum 10 
        - 美国宇航员 https://www.instagram.com/stationcdrkelly/


