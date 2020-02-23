# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 18:03
# @File    : main.py


"""
main.py: 在pycharm或vscode里单步调试
"""

from scrapy import cmdline
from datetime import datetime

# now = datetime.now().strftime('%Y-%m-%d_%H-%M')

cmdline.execute("scrapy crawl example  -s CLOSESPIDER_ITEMCOUNT=1000".split())
