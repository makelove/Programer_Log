# -*- encoding: utf-8 -*-
'''
@File    :   js_server.py
@Time    :   2020/02/23 09:53:30
@Author  :   play4fun
@Desc    :   https://www.w3cschool.cn/flask/flask_templates.html
'''

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    Title = "Js动态页面演示"
    return render_template('index.html', Title=Title)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
