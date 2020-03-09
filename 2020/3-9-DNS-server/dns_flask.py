# -*- encoding: utf-8 -*-
'''
@File    :   dns_flask.py
@Time    :   2020/03/09 16:36:03
@Author  :   play4fun
@Desc    :   

'''

from flask import Flask, request, jsonify
import socket
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    d = {
        'msg': '/dns?domain=xxx.xx'
    }
    return jsonify(d)
    pass


@app.route('/dns', methods=['GET'])
def dns():
    domain = request.args.get('domain', "")
    rt = {}
    rt['domain'] = domain
    ip = ''
    if domain:
        try:
            ip = socket.gethostbyname(domain)            
        except Exception as e:
            print(e)
            rt['error'] = str(e)
            pass
    rt['ip'] = ip
    return jsonify(rt)
    pass


if __name__ == '__main__':
    app.run(debug=True)
