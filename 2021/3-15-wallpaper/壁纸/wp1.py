# -*- coding:utf-8 -*-
'''
# @FileName  :wp1.py
# @Time      :2021/3/4 10:27
# @Author    :play4fun
#
https://cloud.tencent.com/developer/article/1661753
五行Python代码自动换你的电脑桌面壁纸（内附源码和exe）

https://blog.csdn.net/theplayerwuliang/article/details/6049934
设置桌面背景墙纸，SystemParametersInfo(20, True, 图片路径, 1)

具体文档
https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-systemparametersinfow

API
返回json
https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1
努沙杜瓦海岸与防波堤，印度尼西亚巴厘岛 (© Dkart/Getty Images)

返回XML
https://cn.bing.com/HPImageArchive.aspx?idx=0&n=1
图片地址
https://cn.bing.com/th?id=OHR.Comma_ZH-CN3584865247_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp
'''

import requests
import ctypes
import os


def main():
    path = os.getcwd()
    print(path)
    # return

    # ctypes.windll.user32.SystemParametersInfoW(20, 0, r'C:\Users\work\Downloads\th.jfif'
    # , 0)  # 设置桌面,可以

    url = 'https://area.sinaapp.com/bingImg/'
    rs = requests.get(url)
    print('壁纸地址：', rs.url)
    fp = f'{path}/bingImg.jpg'
    with open(fp, 'wb') as f:
        f.write(rs.content)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, fp, 0)

    pass


if __name__ == "__main__":
    main()
