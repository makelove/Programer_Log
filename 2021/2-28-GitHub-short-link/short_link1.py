# -*- coding: utf-8 -*-
# @Time    : 2021/2/28 16:29
# @File    : short_link1.py


"""
short_link1.py:

效果
https://dark.net.cn/sl/redirect.htm
https://dark.net.cn/sl/t1.htm
"""
import sys
import base64
from github import Github
from config import token

g = Github(token)
# repo = g.get_repo("MartinHeinz/python-project-blueprint")
repo = g.get_repo("makelove/makelove.github.io")


def main(url, path=None):
    # git

#     content = f'''<head>
# <meta http-equiv="refresh" content="0;url={url}">
# </head>'''

    #添加广告
    content = f'''<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="refresh" content="0;url={url}"> 
</head>'''

    if path is None:
        path = "sl/t1.htm"  # TODO 存储起来，与原始URL映射
        rs = repo.create_file(path=path, message="test", content=content, branch="master")
    else:
        contents = repo.get_contents(path)
        rs = repo.update_file(contents.path, message="update_file", content=content, sha=contents.sha, branch="master")
    print('结果：', rs)
    turl = 'https://dark.net.cn/' + path
    print('目标URL：', turl)

    # rs['commit'].sha
    # cmt=repo.get_commit(rs['commit'].sha)

    # sha = data["pull_request"]["head"]["sha"]
    # repo.get_commit(sha=sha).create_status(
    #     state="pending",
    #     target_url="https://FooCI.com",
    #     description="FooCI is building",
    #     context="ci/FooCI"
    # )
    pass


if __name__ == '__main__':
    # url=sys.argv[1]
    url = 'https://m.tb.cn/h.4lGcAwM'  # 60天
    # 长连接
    # main(url)


    #
    url = 'https://m.tb.cn/h.4P4mv6C?sm=2cc4c6'
    path = "sl/t1.htm"  # TODO 存储起来，与原始URL映射
    main(url, path)
