# -*- coding: utf-8 -*-
'''
要全部下载
'''

from urllib.request import urlretrieve
import os
# from data import hotranklist as soundList
from data import recommendlist as soundList
import requests
bdurl='http://bird.snowyevening.com:8008/api/birddetail'

headers={
    'Content-Type':'application/json;charset=UTF-8',
    'User-Agent':'LDBird/3.2.4 (iPod touch; iOS 13.4; Scale/2.00)',
}
def createfiles(filepathname):
    try:
        os.makedirs(filepathname)
    except Exception as err:
        print(str(filepathname) + "已经存在！")


def cbk(a,b,c):  
    '''''回调函数 
    @a:已经下载的数据块 
    @b:数据块的大小 
    @c:远程文件的大小 
    '''  
    per=100.0*a*b/c  
    if per>100:  
        per=100  
    # print('%.2f%%' % per)
    print('\r %.2f%%' % per,end="")


def main():
    for it in soundList['result']:#[5:]:
        print(it['id'])
        dt={
            "applan": "zh-Hans",
            "appvision": "3.2.4",
            "birdId": f"{it['id']}"
        }
        rs=requests.post(headers=headers,url=bdurl,json=dt)
        # print(rs.text)
        js=rs.json()
        sound=js['result']['soundList'][1]#只下载第一个音频
        mp3address=sound['mp3address']
        # fn=f"sounds/{mp3address.split('/')[-2]}.mp3"
        fn=f"sounds/{mp3address.replace('https://','').replace('http://','')}"
        print(fn)
        #如果不存在
        pn='/'.join(fn.split('/')[:-1])
        createfiles(pn)

        urlretrieve(mp3address,fn,cbk)
        print()#空行
        print('下载完毕',mp3address)
        print('-'*30)

        # break
    pass

if __name__ == "__main__":
    main()
    pass