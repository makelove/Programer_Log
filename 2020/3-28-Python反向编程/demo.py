# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 13:33
# @File    : demo.py


"""
demo.py:
"""
import requests


def main():
    pass


def verify(ip, port):
    url = 'https://httpbin.org/ip'
    proxy = f'http://{ip}:{port}'

    proxies = {"http": proxy, "https": proxy}

    try:
        # 耗时太长 超时报错
        rs = requests.get(url, proxies=proxies, timeout=5, )
        # TODO  https 验证证书，防止中间人攻击。蜜罐
        # verify=True
    except Exception as e:
        print(e)
        return False
    print(rs.text)
    dstIP = rs.json()['origin']

    if dstIP == ip:
        return True
    return False
    pass


if __name__ == '__main__':
    ip = '61.5.17.143'  # '95.217.34.209'
    port = 8080  # 3128
    rt = verify(ip, port)
    print('是否有效？', rt)
    # main()
