# -*- encoding: utf-8 -*-
'''
@File    :   locust_file.py
@Time    :   2020/02/23 12:06:03
@Author  :   play4fun
@Desc    :   
'''

from locust import HttpLocust, TaskSet, between

def login(l):
    l.client.post("/login", {"username":"ellen_key", "password":"education"})

def logout(l):
    l.client.post("/logout", {"username":"ellen_key", "password":"education"})

def index(l):
    l.client.get("/")

def profile(l):
    l.client.get("/profile")

class UserBehavior(TaskSet):
    tasks = {index: 2, profile: 1}