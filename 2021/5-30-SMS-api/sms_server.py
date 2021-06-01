# -*- encoding: utf-8 -*-
'''
@File    :   sms_server.py
@Time    :   2021/05/25 12:26:42
@Author  :   HG
@Desc    :   
'''

import re
import json
from flask import Flask, request, jsonify
from urllib.parse import unquote, quote

app = Flask(__name__)

smsD = dict()  # TODO 持久化


@app.route('/get_verify', methods=['GET'])
def get_verify():
    '''
    请求验证码
    http://192.168.4.237:8097/get_verify?phone=
    http://192.168.4.14:8097/get_verify
    https://play4fun.pythonanywhere.com/get_verify?phone=6505551212

    更新
    https://play4fun.pythonanywhere.com/get_verify?dID=140582940&slt=1
    https://play4fun.pythonanywhere.com/get_verify?dID=140582940&slt=1&source=拼多多
    http://0.0.0.0:8097/get_verify?dID=140582940&slt=1&source=拼多多
    http://0.0.0.0:8097/get_verify?dID=140582940&slt=1
    '''
    rt = {
        'status': 404  # 找不到
    }
    p = request.args.get('dID', "")
    slt = request.args.get('slt', "")
    source = request.args.get('source', "")
    if p:
        # print(smsD)
        # ph = f"{p}-{slt}-{source}"
        ph = p+'-'+slt  # +'-'+source
        # print(ph)
        if ph in smsD:
            rt['status'] = 200
            rt['data'] = smsD[ph]

    return jsonify(rt)
    pass


@app.route('/sms', methods=['GET'])  # , 'POST'
def sms():
    '''
    http://192.168.4.237:8097/sms?
    https://play4fun.pythonanywhere.com/sms

    测试
    js={
            "bd":"【拼多多】您正在登录拼多多，验证码是790892。请于5分钟内完成验证，若非本人操作，请忽略本短信。",
            "ph":"106551951134188852",
            "tm":"1621923596617",
            "slt":"1",
            "dId":"140582940"
        }
    p=quote(json.dumps(js))
    url='https://play4fun.pythonanywhere.com/sms?p='+p
    url='http://0.0.0.0:8097/sms?p='+p
    curl url
    '''
    # print('args: ', request.args)
    # print('form: ', request.form)
    rt = {
        'status': 404
    }

    p = request.args.get('p', "")
    print('paramer:', p)
    if p:
        js = json.loads(unquote(p))
        '''
        {
            "bd":"【拼多多】您正在登录拼多多，验证码是790892。请于5分钟内完成验证，若非本人操作，请忽略本短信。",
            "ph":"106551951134188852",
            "tm":"1621923596617",
            "slt":"1",
            "dId":"140582940"
        }
        '''
        # print(js)
        # dId：发出端设备ID；slt：发出端卡槽号； ph ：短信号码；bd：短信内容；tm：短信时间戳
        # print('短信号码', js['ph'])
        # print('短信内容', js['bd'])
        # print('时间戳', js['tm'])
        ''' 日志
        2021-05-25 05:15:15 短信号码 6505551212
        2021-05-25 05:15:15 短信内容 lvya test 02
        2021-05-25 05:15:15 时间戳 1576215934956
        '''

        content = js['bd']  # 正则
        rs = re.findall('【(.*)】', content)  # 哪个网站
        source = rs[0]
        rs = re.findall(r'\d{4,6}', content)  # 验证码
        vfCode = rs[0]
        # ph = f"{js['dId']}-{js['slt']}-{source}"
        ph = js['dId']+'-'+js['slt']  # +'-'+source
        sd = {
            'timestamp': int(js['tm']),
            'content': content,
            'source': source,
            'vfCode': vfCode,
        }
        smsD[ph] = sd
        # print(sd)
        # rt['status'] = 200
        return 'OK'  # 他们要求

    return jsonify(rt)
    pass


@app.route('/', methods=['GET'])  # , 'POST'
def index():
    rt = {
        'status': 200
    }
    return jsonify(rt)
    pass


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8097)
