# -*- encoding: utf-8 -*-
'''
@File    :   fastapi_pydantic1.py
@Time    :   2021/07/11 11:02:05
@Author  :   GH
@Desc    :   
参考
https://juejin.cn/post/6844904051327369224

运行
uvicorn fastapi_pydantic1:app  --port 5000
'''

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class People(BaseModel):
    name: str
    age: int
    # address: str
    # salary: float


@app.post('/insert')
def insert(people: People):
    age_after_10_years = people.age + 10
    msg = f'此人名字叫做：{people.name}，十年后此人年龄：{age_after_10_years}'
    return {'success': True, 'msg': msg}
