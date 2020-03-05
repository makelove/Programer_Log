# -*- encoding: utf-8 -*-
'''
@File    :   verify_https.py
@Time    :   2020/03/05 16:23:06
@Author  :   play4fun
@Desc    :   https请求安全性，验证证书
'''

import requests
def main():
    
    url='https://httpbin.org/ip'
    proxy='http://127.0.0.1:8080'
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    try:
        rs = requests.get(url, proxies=proxies)
        print(rs.text)
        #报错 certificate verify failed
    except Exception as e:
        print(e)
    print('-'*30)

    rs = requests.get(url)
    print('正常:',rs.text)
    #正常
    print('-'*30)

    #取消证书验证
    rs = requests.get(url, proxies=proxies,verify=False)
    print(rs.text)
    pass

if __name__ == "__main__":
    main()
    pass