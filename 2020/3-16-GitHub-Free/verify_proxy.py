# -*- encoding: utf-8 -*-
'''
@File    :   verify_proxy.py
@Time    :   2020/03/15 09:49:45
@Author  :   play4fun
@Desc    :   https://github.com/jiangxianli/ProxyIpLib

https://www.freeip.top/?page=1&protocol=https
https://144.76.214.154:1080
'''

import requests
from time import time


def verify(proxy: str):
    print('-' * 20)

    start = time()
    proxies = {"http": proxy, "https": proxy}
    url = 'https://httpbin.org/ip'
    try:
        rs = requests.get(url, proxies=proxies, verify=True, timeout=10)
    except Exception as e:
        print(e)
        return False, proxy, 0
    spendT = time() - start

    # print(rs.text)
    request_time = rs.elapsed.total_seconds()
    print('花费时间', request_time, ':', spendT)
    js = rs.json()
    print(proxy, js['origin'])
    if js['origin'] in proxy:
        print('代理工作正常', True, proxy, request_time)
        return True, proxy, request_time
    return False, proxy, 0
    pass


def main():
    #  计算 花费的时间

    # proxy='https://144.76.214.154:1080'#不支持https ，可能是蜜罐
    proxy = 'https://121.237.149.238:3000'  # 延迟太长
    proxy = 'https://180.183.51.135:8080'  # 
    proxy = 'https://128.199.184.93:8080'  #

    rs = verify(proxy)
    print(rs)


if __name__ == "__main__":
    main()
