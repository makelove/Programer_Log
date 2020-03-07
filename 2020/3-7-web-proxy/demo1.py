# -*- encoding: utf-8 -*-
'''
@File    :   demo1.py
@Time    :   2020/03/07 19:34:52
@Author  :   play4fun
@Desc    :   
'''
from urllib.parse import quote_plus
import json
import requests
host='https://ca.weboproxy.com/index.php'

def main():
    target_url='https://www.reddit.com/r/python'
    # d={'url':target_url}
    # data=json.dumps(d)
    data='url='+quote_plus(target_url)
    print(data)
    rs=requests.post("https://ca.weboproxy.com/index.php",
        # data=data,#'url=https%3A%2F%2Fwww.reddit.com%2Fr%2Fcoronavirus',
        allow_redirects=False,
        data=data,
        headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            # "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            # "DNT": "1",
            "Origin": "https://weboproxy.com",
            "Referer": "https://weboproxy.com/",
            # "Sec-Fetch-Dest": "document",
            # "Sec-Fetch-Mode": "navigate",
            # "Sec-Fetch-Site": "same-site",
            # "Sec-Fetch-User": "?1",
            # "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        },
        # cookies={
        #     "_ga": "GA1.2.1357799465.1583580644",
        #     "_gat_gtag_UA_139843171_1": "1",
        #     "_gid": "GA1.2.509039750.1583580644"
        # },
    )
    print(rs.text)
    print('-'*40)
    print(rs.headers)
    print('-'*40)
    print(rs.headers['Location'])
    print('-'*40)
    print(rs.url)
    pass

if __name__ == "__main__":
    main()
