# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 10:09
# @File    : 监听1.py


"""
监听1.py:

找不出来 智能插排的传送方式

插排在路由器显示为
BroadLink_OEM
项目合作 - 杭州博联智能科技股份有限公司 - BroadLink
http://www.broadlink.com.cn/cooperation.html


也可以
nc -ul 127.0.0.1 5005
"""
from socket import *

# HOST = '192.168.0.222'
HOST = ''  # 广播地址 255.255.255.255

# HOST = '224.0.0.251'
# 组播地址 224.0.0.251:5353
# mDNS-client : 客户端(组播请求), 带缓存(过期时间)
# mDNS-server : 服务器(组播/单播响应)

PORT = 80

s = socket(AF_INET, SOCK_DGRAM)
s.bind((HOST, PORT))


def main():
    print('开始监听')
    while True:
        data, address = s.recvfrom(1024)
        print(data)
        print(address)
    pass


if __name__ == '__main__':
    main()
