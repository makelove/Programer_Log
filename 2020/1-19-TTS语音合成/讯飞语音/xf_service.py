# -*- coding: utf-8 -*-
# @Time    : 2020-01-18 20:25
# @File    : xf_service.py


"""
xf_service.py:
"""

# import websocket
from websocket import create_connection
import datetime
import hashlib
import base64
import hmac
import json
from urllib.parse import urlencode
import os
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime


class XFtts(object):
    # 初始化
    def __init__(self, APPID, APIKey, APISecret, ):
        self.APPID = APPID
        self.APIKey = APIKey
        self.APISecret = APISecret
        # self.Text = Text

        # 公共参数(common)
        self.CommonArgs = {"app_id": self.APPID}
        # 业务参数(business)，更多个性化参数可在官网查看
        self.BusinessArgs = {"aue": "raw", "auf": "audio/L16;rate=16000", "vcn": "xiaoxue", "tte": "utf8", "ent": "aisound"}#TODO
        # self.Data = {"status": 2, "text": str(base64.b64encode(self.Text.encode('utf-8')), "UTF8")}

        # 使用小语种须使用以下方式，此处的unicode指的是 utf16小端的编码方式，即"UTF-16LE"”
        # self.Data = {"status": 2, "text": str(base64.b64encode(self.Text.encode('utf-16')), "UTF8")}

        #
        self.url = self.create_url()

    # 生成url
    def create_url(self):
        url = 'wss://tts-api.xfyun.cn/v2/tts'
        # 生成RFC1123格式的时间戳
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))

        # 拼接字符串
        signature_origin = "host: " + "ws-api.xfyun.cn" + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + "/v2/tts " + "HTTP/1.1"
        # 进行hmac-sha256进行加密
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()
        signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')

        authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
            self.APIKey, "hmac-sha256", "host date request-line", signature_sha)
        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
        # 将请求的鉴权参数组合为字典
        # authorization='YXBpX2tleT0iODc1YmQ5OGNmOTJmZTE0OGQxNDU5ODFiZjZmNGJhMGEiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0ia3RlelJoV2lMS2tvbW9rbXcxZDhvZ1Q5WE5Obld1ZWhqcjFWUVhleFZkTT0i'
        v = {
            "authorization": authorization,
            "date": date,
            "host": "ws-api.xfyun.cn"
        }
        # 拼接鉴权参数，生成url
        url = url + '?' + urlencode(v)
        # print("date: ", date)
        # print("v: ", v)
        # 此处打印出建立连接时候的url,参考本demo的时候可取消上方打印的注释，比对相同参数时生成的url与自己代码生成的url是否一致
        # print('websocket url :', url)
        # url='wss://tts-api.xfyun.cn/v2/tts?authorization=YXBpX2tleT0iODc1YmQ5OGNmOTJmZTE0OGQxNDU5ODFiZjZmNGJhMGEiLCBhbGdvcml0aG09ImhtYWMtc2hhMjU2IiwgaGVhZGVycz0iaG9zdCBkYXRlIHJlcXVlc3QtbGluZSIsIHNpZ25hdHVyZT0iU0hnZ1lLa2c4Y0xUV25BdTNTNGkwak90YzhYNnM1WENrTFFIUHRLekc0VT0i&date=Sat,%2004%20Jan%202020%2004:19:03%20GMT&host=ws-api.xfyun.cn'
        return url

    def say(self, sentens,speaker='xiaoxue'):#发音人
        print(sentens)
        text = str(base64.b64encode(sentens.encode('utf-8')), "UTF8")
        # print(text)
        self.BusinessArgs['vcn']=speaker

        Data = {"status": 2, "text": text}
        d = {"common": self.CommonArgs,
             "business": self.BusinessArgs,
             "data": Data,
             }#传参
        dt = json.dumps(d)
        print(d)
        # if not ws.connected:
        #     print('重新连接ws')
        #     # uri = wsParam.create_url()
        #     ws = create_connection(uri)
        ws = create_connection(self.create_url())
        ws.send(dt)
        print('-' * 30)

        print('接收信息')
        audiosum = bytes()
        while True:
            message = ws.recv()
            # print(message)
            try:
                message = json.loads(message)
                code = message["code"]
                sid = message["sid"]
                audio = message["data"]["audio"]
                audio = base64.b64decode(audio)
                status = message["data"]["status"]

                if status == 2:
                    audiosum += audio

                    print("ws is closed")
                    ws.close()

                    # wav_path = f'./wav-{index}.wav'
                    # wav_path = f'{dir}/{index}.wav'
                    # with wave.open(wav_path, 'wb') as wavfile:
                    #     wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))
                    #     wavfile.writeframes(audiosum)  # TODO byteIO ？
                    # print('写入 ', wav_path)
                    # rsd[index] = {'sentens': sentens, 'file': wav_path}

                    return audiosum
                    # break

                if code != 0:
                    errMsg = message["message"]
                    print("sid:%s call error:%s code is:%s" % (sid, errMsg, code))
                else:
                    audiosum += audio
                    continue

            except Exception as e:
                print("receive msg,but parse exception:", e)

        pass


def test1():
    import wave
    from config import APIKey, APISecret, APPID
    wsParam = XFtts(APPID=APPID,
                    APIKey=APIKey,
                    APISecret=APISecret, )
    text = '而除了靠免费盗版片获取流量，以广告等方式变现的途径外，更直接的盈利方式就是直接售卖盗版资源。2019年4月，媒体报道称河南公安机关已打击2个制作销售高清盗版电影的犯罪团伙，截止案发，这2个团伙共制作盗版影片320余部，初步估算非法获利700余万元。'
    audiosum = wsParam.say(text)
    wav_path = f'test1.wav'
    # audiosum += audio
    with wave.open(wav_path, 'wb') as wavfile:
        wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))
        wavfile.writeframes(audiosum)
    print('写入 ', wav_path)

    pass


def main():
    test1()
    pass


if __name__ == '__main__':
    main()
