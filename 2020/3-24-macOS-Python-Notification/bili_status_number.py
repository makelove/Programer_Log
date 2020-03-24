# -*- encoding: utf-8 -*-
'''
@File    :   bili-status-number.py
@Time    :   2020/03/05 21:55:27
@Desc    :   获取我的账号状态，数据
https://biandan.me/877.html

粉丝:	 2130
播放:	 23.1542 万
点赞:	 2377
'''
from random_useragent.random_useragent import Randomize
import requests

mid = '180948619'
follow_url = 'https://api.bilibili.com/x/relation/stat?vmid=' + mid
play_up_url = 'https://api.bilibili.com/x/space/upstat?mid=' + mid

r_agent = Randomize()


def bili_stat():
    # 粉丝
    headers = {"User-Agent": r_agent.random_agent('desktop', 'windows'),
               "X-Requested-With": "XMLHttpRequest"}
    rs = requests.get(follow_url, headers=headers)
    js = rs.json()
    follower = js['data']['follower']  # 粉丝
    #
    headers = {"User-Agent": r_agent.random_agent('desktop', 'windows'),
               "X-Requested-With": "XMLHttpRequest"}
    rs = requests.get(play_up_url, headers=headers)
    js = rs.json()
    viewer = js['data']['archive']['view']  # 播放数
    likes = js['data']['likes']  # 点赞

    return follower, viewer / 10000, likes


def main():
    follower, viewer, likes = bili_stat()
    print('粉丝:\t', follower)
    print('播放:\t', viewer, '万')
    print('点赞:\t', likes)
    pass


if __name__ == "__main__":
    main()
    pass
