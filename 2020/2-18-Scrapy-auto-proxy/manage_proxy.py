# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 20:20
# @File    : manage_proxy.py


"""
manage_proxy.py:
"""
import redis

r = redis.Redis(decode_responses=True)
proxy_key = 'proxy'
error_proxy_key = 'error_proxy'


def main():
    http_proxy = [
        # 'http://127.0.0.1:3121',
        # 'http://127.0.0.1:3122',
        # 'http://127.0.0.1:3123',
        # 'http://127.0.0.1:3124',

        'http://172.17.0.4:3128',
        'http://172.17.0.5:3128',
        'http://172.17.0.6:3128',
        'http://172.17.0.7:3128',
    ]  #

    init_value = 10000  # 1000000  # 1百万
    for idx, ip in enumerate(http_proxy):
        # r.zincrby(proxy_key, init_value, ip)
        # r.zincrby(error_proxy_key, 0, ip)

        r.zadd(proxy_key, {ip: init_value+idx})
        r.zadd(error_proxy_key, {ip: 0})
    print('插入完毕')
    pass


def scan():
    count = r.zcard(proxy_key)
    print(proxy_key, count)
    rs = r.zscan(proxy_key, count=count)  # 288
    for ip, value in rs[1]:
        print(ip, '\t', value)
    print('-' * 40)

    # 错误
    count = r.zcard(error_proxy_key)
    print(error_proxy_key, count)
    rs = r.zscan(error_proxy_key, count=count)
    for ip, value in rs[1]:
        print(ip, '\t', value)
        # break


if __name__ == '__main__':
    # main()
    scan()
