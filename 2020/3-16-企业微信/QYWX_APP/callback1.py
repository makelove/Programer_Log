# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 15:41
# @File    : callback1.py


"""
callback1.py:
"""
import time
from flask import Flask, request, jsonify
import xml.etree.cElementTree as ET

from config import CorpID, Secret, Token, EncodingAESKey
from WXBizMsgCrypt import WXBizMsgCrypt, ResponseMessage, generateNonce

app = Flask(__name__)
wxcpt = WXBizMsgCrypt(Token, EncodingAESKey, CorpID)


@app.route('/')
def hello_world():
    d = {'msg': 'Hello from Flask! play for fun!'}
    return jsonify(d)


@app.route('/weixin', methods=['GET'])
def weixin():
    print('/weixin')

    # 获取输入参数
    if request.method == 'GET':
        try:
            args = request.args
            print(args)
            # print request.args.get('kw', "")
            sVerifyMsgSig = request.args.get('msg_signature', "")
            sVerifyTimeStamp = request.args.get('timestamp', "")
            sVerifyNonce = request.args.get('nonce', "")
            sVerifyEchoStr = request.args.get('echostr', "")

            ret, sEchoStr = wxcpt.VerifyURL(sVerifyMsgSig, sVerifyTimeStamp, sVerifyNonce, sVerifyEchoStr)
            print(ret, sEchoStr)
            if ret != 0:
                print("ERR: VerifyURL ret: " + str(ret))
                return "ERR: VerifyURL ret: " + str(ret)

            return sEchoStr

        except ValueError as e:
            print("ValueError", e)
            # abort(404)      # 返回 404
            return "NULL"

    return 'NULL'


@app.route('/weixin', methods=['POST'])
def reply():
    if request.method == 'POST':
        data = request.data      
        # data=b'<xml><ToUserName><![CDATA[wwefbaf556aed20639]]></ToUserName><Encrypt><![CDATA[bBEQ8PazeD7W/IQz61kBUNTGpl4Epv2OzER3NKOyMKHKddYtpXvzmuL8jMgMA6Tg5odxj+T8f+yYbC8bxubV2RbzKQaeJvgcbx8ekzCn1pLXOB+17kcZYD2Bf65FTjhtTdMrdTqBFH4yZTzY/Jf3C5PBz08U8TAxp/x+zmZmFZEGhbfFdWUC2OYhxyXV8aemoLBnkixJdMyP8zFXnlyPvk2WtRxOf+UJb/yX+SbIXwnUDPODj03lgPKSkZj6jpwLv/o6H3wLVifpFTqWwU5ICu5S/tJwO1acyL0yc2oEswZhB2ZdTFCrCGJCjWIT+9abkd9jseb0G9o4dBY/kLuTQhdZIJemofcl0HWUTGLnAPNSQ51sYvfLejz8IKIrQFai11YKrsImyQz5QXLZpe8YVkA+zpDb8SHfZkhKfxP5daM=]]></Encrypt><AgentID><![CDATA[1000003]]></AgentID></xml>'
        #测试 curl -X POST 'http://127.0.0.1:5000/weixin?msg_signature=4e411db7d0507473882bb5718438364ab5a17bec&timestamp=1584351579&nonce=1584033068'
        print(data)

        encrypted_xml = data
        sVerifyMsgSig = request.args.get('msg_signature')
        sVerifyNonce = request.args.get('nonce')
        sVerifyTimeStamp = request.args.get('timestamp')

        ret, xml_content = wxcpt.DecryptMsg(encrypted_xml, sVerifyMsgSig, sVerifyTimeStamp, sVerifyNonce)
        if ret != 0:
            print("ERR: VerifyURL ret: " + str(ret))
            return "ERR: VerifyURL ret: " + str(ret)
        #
        type_fields = {
            "text": ["ToUserName", "FromUserName", "CreateTime", "MsgType", "Content", "MsgId", "AgentID"],
            "image": ["ToUserName", "FromUserName", "CreateTime", "MsgType", "PicUrl", "MediaId", "MsgId", "AgentID"],
            "voice": ["ToUserName", "FromUserName", "CreateTime", "MsgType", "Format", "MediaId", "MsgId", "AgentID"],
            "video": ["ToUserName", "FromUserName", "CreateTime", "MsgType", "ThumbMediaId", "MediaId", "MsgId", "AgentID"],
            "location": ["ToUserName", "FromUserName", "CreateTime", "MsgType", "Location_X", "Location_Y", "Scale", "Label", "MsgId", "AgentID"],
            "link": ["ToUserName", "FromUserName", "CreateTime", "MsgType", "Title", "Description", "PicUrl", "MsgId", "AgentID"]
        }
        xml_tree = ET.fromstring(xml_content)
        type_name = xml_tree.find("MsgType").text
        msg = {}
        for nodename in type_fields[type_name]:
            msg[nodename] = xml_tree.find(nodename).text

        # 示例，原文返回
        print(msg)
        message = msg

        replystr = '收到:\n' + message['Content']
        resp_dict = {
            'to_user': message['FromUserName'],
            'from_user': message['ToUserName'],
            'type': 'text',
            'content': replystr,
        }
        xml_message = ResponseMessage(resp_dict).xml
        nonce = generateNonce()
        ret, returnMsg = wxcpt.EncryptMsg(xml_message, nonce)
        if ret != 0:
            print("ERR: VerifyURL ret: " + str(ret))
            return "ERR: VerifyURL ret: " + str(ret)
        return returnMsg
    return 'NULL'


class ResponseMessage():
    # python dict 转换成特定格式的xml,下面是一些模板
    """
        text_response = {
            'to_user':'',
            'from_user':'',
            'timestamp':'',
            'type':'text',
            'content':'',
        }
        voice_response= {
            'to_user':'',
            'from_user':'',
            'timestamp':'',
            'type':'voice',
            'media_id':''
        }
        image_response= {
            'to_user':'',
            'from_user':'',
            'timestamp':'',
            'type':'image',
            'data':[
                {'media_id':''}
            ]
        }
        video_response= {
            'to_user':'',
            'from_user':'',
            'timestamp':'',
            'type':'video',
            'media_id':'',
            'title':'',
            'description':'',
        }
        article_response= {
            'to_user':'',
            'from_user':'',
            'timestamp':'',
            'type':'news',
            'data':[
                {'title':'',
                 'description':'',
                 'pic_url':'',
                 'url':'',
                }
            ]
        }

    """
    BASIC_RESPONSE_FIELDS = '<ToUserName><![CDATA[%(to_user)s]]></ToUserName>' + \
                            '<FromUserName><![CDATA[%(from_user)s]]></FromUserName>' + \
                            '<CreateTime>%(timestamp)s</CreateTime>' + \
                            '<MsgType><![CDATA[%(type)s]]></MsgType>'

    TEXT_RESPONSE_FIELD = "<Content><![CDATA[%(content)s]]></Content>"
    VOICE_RESPONSE_FIELD = "<Voice><![CDATA[%(media_id)s]]></Voice>"
    IMAGE_RESPONSE_FIELD = "<MediaId><![CDATA[%(media_id)s]]></MediaId>"
    VIDEO_RESPONSE_FIELD = '<Video>' + \
                           '<MediaId><![CDATA[%(media_id)s]]></MediaId>' + \
                           '<Title><![CDATA[%(title)s]]></Title>' + \
                           '<Description><![CDATA[%(description)s]]></Description>' + \
                           '</Video>'
    ARTICLE_RESPONSE_FIELD = '<items>' + \
                             '<Title><![CDATA[%(title)s]]></Title>' + \
                             '<Description><![CDATA[%(description)s]]></Description>' + \
                             '<PicUrl><![CDATA[%(pic_url)s]]></PicUrl>' + \
                             '<Url><![CDATA[%(url)s]]></Url>' + \
                             '</items>'

    def __init__(self, data_dict):

        if 'timestamp' not in data_dict:
            data_dict['timestamp'] = str(int(time.time()))
        self.data = data_dict

    @property
    def xml(self):
        basic = self.BASIC_RESPONSE_FIELDS % self.data
        # text message
        if self.data['type'] == 'text':
            return '<xml>' + basic + self.TEXT_RESPONSE_FIELD % self.data + '</xml>'
        # image message
        elif self.data['type'] == 'image':
            tmp = ''
            for d in self.data['data']:
                tmp = tmp + self.IMAGE_RESPONSE_FIELD % d
            return '<xml>' + basic + '<Image>' + tmp + '</Image></xml>'
        # voice message
        elif self.data['type'] == 'voice':
            return '<xml>' + basic + self.VOICE_RESPONSE_FIELD % self.data + '</xml>'
        # video message
        elif self.data['type'] == 'video':
            return '<xml>' + basic + self.VIDEO_RESPONSE_FIELD % self.data + '</xml>'
        # news message
        elif self.data['type'] == 'news':
            tmp = ''
            for d in self.data['data']:
                tmp = tmp + self.ARTICLE_RESPONSE_FIELD % d
            count = "<ArticleCount>" + str(len(self.data['data'])) + "</ArticleCount>"
            return '<xml>' + basic + count + '<Articles>' + tmp + '</Articles></xml>'
        else:
            return None


if __name__ == '__main__':
    app.run(debug=True)
    # main()
