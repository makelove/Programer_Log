# -*- encoding: utf-8 -*-
'''
@File    :   groupby.py
@Time    :   2021/06/19 09:38:40
@Author  :   GH
@Desc    :   https://blog.csdn.net/xiaoc100200/article/details/111402566
python 列表 排序+分组
需求： 按字段排序，然后分组
'''

from itertools import groupby
# from collections import Counter# 统计

user_list = [
    {"uid": 1, "sex": "男", "age": 10},
    {"uid": 3, "sex": "男", "age": 20},
    {"uid": 4, "sex": "女", "age": 20},
    {"uid": 4, "sex": "女", "age": 31},
    {"uid": 2, "sex": "男", "age": 10}
]
user_sort = sorted(user_list, key=lambda x: (x["sex"], x["age"]))  # 必须排序
[{'uid': 4, 'sex': '女', 'age': 20},
 {'uid': 4, 'sex': '女', 'age': 31},
 {'uid': 1, 'sex': '男', 'age': 10},
 {'uid': 2, 'sex': '男', 'age': 10},
 {'uid': 3, 'sex': '男', 'age': 20}]

# 手写代码
outD = {}
for d in user_list:
    tl = outD.get(d['sex'], [])
    tl.append(d)
    outD[d['sex']] = tl
# print(outD)
for k, v in outD.items():
    print(k, ':', v)

# 使用系统库
# 一行代码
user_group = groupby(user_sort, key=lambda x: (x["sex"], x["age"]))
for key, group in user_group:
    print(key, list(group))

# ('女', 20) [{'uid': 4, 'sex': '女', 'age': 20}]
# ('女', 31) [{'uid': 4, 'sex': '女', 'age': 31}]
# ('男', 10) [{'uid': 1, 'sex': '男', 'age': 10}, {'uid': 2, 'sex': '男', 'age': 10}]
# ('男', 20) [{'uid': 3, 'sex': '男', 'age': 20}]

print('-'*30)


def g(x):  # 自定义分组key
    if (x['age'] > 0) and (x['age'] <= 10):
        return 'small'  # 儿童
    elif (x['age'] > 10) and (x['age'] <= 20):
        return 'mid'  # 少年
    else:
        return 'max'  # 大人


user_group = groupby(user_sort, key=g)
for key, group in user_group:
    print(key, list(group))

# mid[{'uid': 4, 'sex': '女', 'age': 20}]
# max[{'uid': 4, 'sex': '女', 'age': 31}]
# small[{'uid': 1, 'sex': '男', 'age': 10}, {'uid': 2, 'sex': '男', 'age': 10}]
# mid[{'uid': 3, 'sex': '男', 'age': 20}]
