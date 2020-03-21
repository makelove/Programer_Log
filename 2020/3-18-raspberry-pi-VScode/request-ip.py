# -*- encoding: utf-8 -*-
'''
@File    :   request-ip.py
@Time    :   2020/03/19 18:07:01
@Author  :   play4fun
@Desc    :   测试文件
vscode 安装 Python 插件
然后 断点调试
'''

import requests


def main():
    url = 'http://httpbin.org/ip'
    rs = requests.get(url)
    print(rs.headers)
    print(rs.text)
    js = rs.json()
    print(js['origin'])
    pass


if __name__ == "__main__":
    main()
