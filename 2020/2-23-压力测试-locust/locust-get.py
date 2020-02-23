# -*- encoding: utf-8 -*-
'''
@File    :   locust-get.py
@Time    :   2020/02/23 12:11:51
@Author  :   play4fun
@Desc    :   
'''



from locust import HttpLocust, TaskSet, task, Locust



def get(l):
    uri = '/'
    rs = l.client.get(uri)  

class UserTasks(TaskSet):
    # 列出需要测试的任务形式一
    tasks = [get]

    # 列出需要测试的任务形式二
    # @task
    # def page404(self):
    #     self.client.get("/does_not_exist")


class WebsiteUser(HttpLocust):
    host = "http://127.0.0.1:8080/"
    min_wait = 2000
    max_wait = 5000
    task_set = UserTasks