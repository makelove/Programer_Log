# -*- coding: utf-8 -*-


"""
sound_proxy.py:

执行
mitmweb -s sound_proxy.py
"""

from mitmproxy import ctx
from mitmproxy.http import HTTPFlow
from mitmproxy import http
import  json

headers={
    'Content-Type':'audio/mpeg'
}

class sound:
    def request(self, flow: HTTPFlow):
        print(flow.request.host,'\t',flow.request.path)
        # return
        # 判断网址
        if 'download.ams.birds.cornell.edu' in flow.request.host and 'audio' in flow.request.path:#过滤网址
            #返回mp3 response
            fp=f'sounds/{flow.request.host}/{flow.request.path[1:]}'
            print('返回mp3 response',fp)
            with open(fp,'rb') as f:
                sd=f.read()
            #response
            flow.response = http.HTTPResponse.make(      status_code=  200,headers=headers, content=sd,        )
            print('mp3文件大小',len(sd))
            pass


addons = [
    sound()
]