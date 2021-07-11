# -*- encoding: utf-8 -*-
'''
@File    :   flask_pydantic1.py
@Time    :   2021/07/11 10:53:01
@Author  :   GH
@Desc    :   

命令行
curl -v -H "Content-Type: application/json" -XPOST http://localhost:5000/insert -d '{
"name" : "werl",
"age" : 5
}'
# 把age改为字符串 报错
curl -v -H "Content-Type: application/json" -XPOST http://localhost:5000/insert -d '{
"name" : "werl",
"age" : "5"
}'

# 使用pydantic
curl -v -H "Content-Type: application/json" -XPOST "http://localhost:5000/insert?name=fjks&age=35" -d '{
"name" : "werl",
"age" : "5"
}'

'''

from flask import Flask, request
from pydantic import BaseModel
from flask_pydantic import validate

app = Flask("__main__")


class QueryModel(BaseModel):
    name: str
    age: int


class People(BaseModel):
    name: str
    age: int
    # address: str
    # salary: float


@app.route('/insert', methods=['POST'])
@validate(body=People)
def insert(body: People, query: QueryModel):
    print('body:', body)  # body: name='werl' age=5
    print('query:',  query)  # query: name='fjks' age=35
    age_after_10_years = body.age + 10
    msg = f'此人名叫：{body.name}，10年后，此人年龄：{age_after_10_years}'
    return {'success': True, 'msg': msg}


@app.route('/insert0', methods=['POST'])
def insert0():
    info = request.json
    name = info['name']
    age = info['age']
    age_after_10_years = age + 10
    msg = f'此人名叫：{name}，10年后，此人年龄：{age_after_10_years}'
    return {'success': True, 'msg': msg}


@app.route('/insert2', methods=['POST'])
def insert2():
    info = request.json
    name = info.get('name', '')
    if not name:
        return {'success': False, 'msg': 'name 参数不可省略，不可为空！'}
    age = info.get('age', 0)
    if not isinstance(age, int):
        return {'success': False, 'msg': 'age参数不是数字！'}
    age_after_10_years = age + 10
    msg = f'此人名叫：{name}，10年后，此人年龄：{age_after_10_years}'
    return {'success': True, 'msg': msg}


def main():
    pass


if __name__ == "__main__":
    app.run(debug=True)
