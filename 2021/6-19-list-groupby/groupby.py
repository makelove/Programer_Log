# -*- encoding: utf-8 -*-
'''
@File    :   groupby.py
@Time    :   2021/06/19 09:38:40
@Author  :   HG
@Desc    :   
'''

from itertools import groupby

user_list = [
    {"uid": 1, "sex": "男", "age": 10},
    {"uid": 3, "sex": "男", "age": 20},
    {"uid": 4, "sex": "女", "age": 20},
    {"uid": 4, "sex": "女", "age": 31},
    {"uid": 2, "sex": "男", "age": 10}
]
user_sort = sorted(user_list, key=lambda x: (x["sex"], x["age"]))
[{'uid': 4, 'sex': '女', 'age': 20},
 {'uid': 4, 'sex': '女', 'age': 31},
 {'uid': 1, 'sex': '男', 'age': 10},
 {'uid': 2, 'sex': '男', 'age': 10},
 {'uid': 3, 'sex': '男', 'age': 20}]

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
        return 'small'
    elif (x['age'] > 10) and (x['age'] <= 20):
        return 'mid'
    else:
        return 'max'


user_group = groupby(user_sort, key=g)
for key, group in user_group:
    print(key, list(group))

# mid[{'uid': 4, 'sex': '女', 'age': 20}]
# max[{'uid': 4, 'sex': '女', 'age': 31}]
# small[{'uid': 1, 'sex': '男', 'age': 10}, {'uid': 2, 'sex': '男', 'age': 10}]
# mid[{'uid': 3, 'sex': '男', 'age': 20}]
