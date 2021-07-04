# -*- encoding: utf-8 -*-
'''
@File    :   diskcache1.py
@Time    :   2021/07/04 12:47:38
@Author  :   GH
@Desc    :   
'''
import requests
from functools import lru_cache

from diskcache import Cache
cache = Cache('cachedir')


# @lru_cache()  # Flask 服务器使用，才行
@cache.memoize()
def get_ip(a):  # 需要很多计算，计算一次就可以了
    print('不使用缓存')
    url = 'https://httpbin.org/ip'
    rs = requests.get(url)
    print('get IP:', rs.text)

    return rs.json()['origin']


def main():
    ip = get_ip(a=1)
    print(ip)
    pass


if __name__ == "__main__":
    main()
