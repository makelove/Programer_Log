# -*- encoding: utf-8 -*-
'''
@File    :   demo2.py
@Time    :   2020/03/07 20:32:21
@Author  :   play4fun
@Desc    :   
'''
import requests
from urllib.parse import quote_plus

def main():
    url='https://www.reddit.com/r/java'
    quote_url=quote_plus(url)
    print(quote_url)

    rs=requests.post("https://ca.weboproxy.com/index.php",
    # data='url=https%3A%2F%2Fwww.reddit.com%2Fr%2Fpython',
    data='url='+quote_url,
    allow_redirects=False,#禁止重定向
    headers={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://weboproxy.com",
        "Referer": "https://weboproxy.com/",
        # "Sec-Fetch-Dest": "document",
        # "Sec-Fetch-Mode": "navigate",
        # "Sec-Fetch-Site": "same-site",
        # "Sec-Fetch-User": "?1",
        # "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        },
        cookies={},
    )
    print(rs.text)
    print('-'*40)
    print(rs.headers)
    print('-'*40)
    print(rs.headers['Location'])
    pass

if __name__ == "__main__":
    main()
