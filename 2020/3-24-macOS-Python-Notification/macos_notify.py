# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 15:45
# @File    : macos_notify.py


"""
macos_notify.py:
参考
https://stackoverflow.com/questions/17651017/python-post-osx-notification
"""

import os
from datetime import datetime
from bili_status_number import bili_stat


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


def main():
    # notify("Title", "Heres an alert")

    follower,viewer,likes=bili_stat()
    title = 'B站 统计'
    text = f'粉丝:{follower}, 点赞:{likes},播放:{viewer}万'
    notify(title, text)
    pass


if __name__ == '__main__':
    main()
