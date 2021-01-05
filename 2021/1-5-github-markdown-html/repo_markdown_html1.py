# -*- coding: utf-8 -*-
# @Time    : 2021/1/5 00:20
# @File    : repo_markdown_html1.py


"""
repo_markdown_html1.py:
"""
from github import Github
from pprint import pprint
from config import token
import codecs, markdown

g = Github(token)


def main():
    repo = g.get_repo("makelove/Programer_Log")
    for content in repo.get_contents(''):
        print('-' * 4, content.name)
        if content.name.endswith('.md'):
            # break
            html = markdown.markdown(content.decoded_content.decode())
            # 创建文件夹
            fp22 = 'repo_html/' + content.name + '.html'
            with codecs.open(fp22, mode="wb", encoding="utf-8") as output_file:
                output_file.write(html)
                print('markdown html', fp22)
            pass
    pass


if __name__ == '__main__':
    main()
