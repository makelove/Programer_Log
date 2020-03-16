# -*- encoding: utf-8 -*-
'''
@File    :   bot1.py
@Time    :   2020/03/15 11:21:27
@Author  :   play4fun
@Desc    :   https://github.com/MakDon/we-work-bot
'''
from weworkbot import Bot as wBot
def main():
    url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=2a599e1c-9ec7-4f64-ad18-cf7cdfdca8249'   

    rs=wBot(url).set_text("hello from  Python3,使用vscode编辑").send()
    wBot(url).set_text('<font color="info">markdown HTML文本，测试</font>', type='markdown').send()
    print('发送成功？')
    pass

if __name__ == "__main__":
    main()
