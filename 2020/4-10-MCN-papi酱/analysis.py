# -*- encoding: utf-8 -*-
'''
@File    :   analysis.py
@Time    :   2020/04/10 09:11:05
@Desc    :   
'''

import requests
# from scrapy.http import HtmlResponse


def get网红(idx):
    rs = requests.get(f"https://mt.mttop.cn/miniprogram/blogger/{idx}",
                      headers={
                          "Accept": "application/json, text/javascript, */*; q=0.01",
                          "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                          "Connection": "keep-alive",
                          "Content-Type": "application/json;charset=UTF-8",
                          "DNT": "1",
                          "Origin": "https://www.mttop.cn",
                          "Referer": "https://www.mttop.cn/pages/bolggerMcn/index.html",
                          "Sec-Fetch-Dest": "empty",
                          "Sec-Fetch-Mode": "cors",
                          "Sec-Fetch-Site": "same-site",
                          "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
                      },
                      cookies={},
                      )
    js=rs.json()
    count=js['data']['allPlatformFansCount'] if js['data']['allPlatformFansCount'] else 0
    return count,js['data']['bloggerNickName'],js['data']['bloggerCalendarRemark']
    pass


def main():
    url = 'https://mt.mttop.cn/miniprogram/blogger/list'
    rs = requests.post("https://mt.mttop.cn/miniprogram/blogger/list",
                       data='{}',
                       headers={
                           "Accept": "application/json, text/javascript, */*; q=0.01",
                           "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                           "Connection": "keep-alive",
                           "Content-Type": "application/json;charset=UTF-8",
                           "DNT": "1",
                           "Origin": "https://www.mttop.cn",
                           "Referer": "https://www.mttop.cn/pages/bolggerMcn/index.html",
                           "Sec-Fetch-Dest": "empty",
                           "Sec-Fetch-Mode": "cors",
                           "Sec-Fetch-Site": "same-site",
                           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
                       },
                       cookies={},
                       )
    js = rs.json()
    # 签约了多少个网红
    print('签约了多少个网红:', len(js['data']))#187
    for d in js['data']:
        print(d['bloggerId'], d['bloggerNickName'])
        print(d['bloggerIntroduction'])
        print('-'*10)
    # 获取所有网红详情
    rtl=[]
    for d in js['data']:
        print(d['bloggerId'], d['bloggerNickName'])
        rtl.append(get网红(d['bloggerId']))
    #清理none
    rtl3=[]
    for fc,name,desc in rtl:
        if not fc:
            fc=0
        rtl3.append((fc,name,desc))
    #按【全网播放量】排序    
    rtl2=sorted(rtl,key=lambda x: x[0])#顺序
    rtl2=sorted(rtl,key=lambda x: -x[0])#倒序 从大到小
    for fc,name,desc in rtl2[:20]:
        print(fc,name,desc)
        print('-'*20)
    pass


def main2():
    # url='https://www.mttop.cn/pages/bolggerMcn/index.html'
    # rs=requests.get(url)
    # html=HtmlResponse(url=url,status=rs.status_code,body=rs.content)
    # html.xpath()
    pass


if __name__ == "__main__":
    main()
