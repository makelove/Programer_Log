# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 13:37
# @Author  : play4fun
# @File    : translate_api.py
# @Software: PyCharm

"""
translate_api.py:
语言列表
源语言语种不确定时可设置为 auto，目标语言语种不可设置为 auto。
http://api.fanyi.baidu.com/api/trans/product/apidoc
"""
# import httplib
# import md5
from hashlib import md5
# import urllib
from urllib.parse import quote, quote_plus
import random
import requests
import json

from config import baidu_appid as appid
from config import baidu_secretKey as secretKey

myurl = '/api/trans/vip/translate'  # https://fanyi-api.baidu.com/api/trans/vip/translate
q = 'He could turn off all the power to the building'
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)


def translate(sub, froml=None, tol='zh'):
    q = sub
    if froml is None:
        froml = 'auto'
    # toLang=tol

    sign = appid + q + str(salt) + secretKey
    # m1 = md5.new()
    m1 = md5()
    m1.update(sign.encode('utf-8'))
    sign = m1.hexdigest()
    myurl = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    myurl = myurl + '?appid=' + appid + '&q=' + quote_plus(q) + '&from=' + froml + '&to=' + tol + '&salt=' + str(salt) + '&sign=' + sign
    # print(myurl)

    #
    rs = requests.get(myurl)
    # print(rs.text)
    js = json.loads(rs.text)
    return js['trans_result'][0]['dst']


def test():
    # sub = 'Zeker, we hebben de verantwoordelijkheid om voor onze blauwe planeet te zorgen.'
    # rs = translate(sub, froml='nl')  # 荷兰
    # sub = 'She must leave the safety of her marine world'
    # 无法翻译多行？
    sub = '''The best and the worst thing about love is that it cannot be expressed in words.   "\n" When you truly love someone, it may be hard to 
    express those emotions through words. "\n"    In fact, real love may make you feel weak in the knees and unable to speak.
    '''
    # 爱的最好和最坏之处在于它不能用语言表达。当你真的爱一个人时，可能很难用言语表达这些情感。事实上，真正的爱情可能会让你感到膝盖无力，无法说话。

    sub = '早上好，你吃饭了吗'
    rs = translate(sub, froml='zh', tol='en')  # 不支持 印度

    print('翻译结果：', rs)


if __name__ == '__main__':
    test()
