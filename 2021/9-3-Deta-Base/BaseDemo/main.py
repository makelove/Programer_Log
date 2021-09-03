# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2021/08/01 16:26:39
@Author  :   GH
@Desc    :   

执行 
uvicorn main:app

'''
from typing import Optional
from fastapi.params import Body
from pydantic import BaseModel
from fastapi import FastAPI
from deta import Deta
from config import project_key

deta = Deta(project_key)
db = deta.Base("baseItem")

app = FastAPI()


class Item(BaseModel):
    key: Optional[str] = None
    name: Optional[str] = None
    age: Optional[int] = None


@app.get("/")
def read_root():
    return {"Hello": "World, great day! 数据库NoSQL"}


@app.put("/items/")
def put_item(item: Item):
    print("item_id:", item)
    # TODO 存入数据库
    del item.key
    rs = db.put(item.dict())
    return {"item": item, 'put': rs}


@app.get("/items/{key}")
def read_item(key: str):  # 1orwum5g2grm
    print("item_id:", key)
    rs = db.get(key)
    return {"item": rs}


@app.put("/items/update")
def update_item(item: Item):

    # rs = db.update({'age': item.age, 'name': item.name}, key=item.key)
    rs = db.put(item.dict())  # 直接更新

    return {"update": rs}


@app.delete("/items/{key}")
def delete_item(key: str):
    rs = db.delete(key)
    return {"delete": rs}
