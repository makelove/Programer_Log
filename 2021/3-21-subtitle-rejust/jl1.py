# -*- coding: utf-8 -*-
# @Time    : 2021/3/21 13:01
# @File    : jl1.py


"""
jl1.py:
正义联盟
"""

import srt
from datetime import timedelta

# fp='/Users/play/Downloads/简体.srt'
fp = '/Users/play/Downloads/cn2.srt'  # 转换格式 UTF-8编码
fp3 = '/Users/play/Downloads/调整后.srt'
with open(fp) as f:
    txt = f.read()
# with open(fp,'rb') as f:#注意文件格式，Little-endian UTF-16 Unicode text, with CRLF line terminators
#     txt=f.read()

subtitle_generator = srt.parse(txt)
subtitles = list(subtitle_generator)
print(subtitles[10])

subs = []
for sub in subtitles:  # 延时30秒
    sub.start = sub.start + timedelta(seconds=32)
    sub.end = sub.end + timedelta(seconds=32)
    subs.append(sub)

ft = srt.compose(subs, reindex=False)  # 问题 https://github.com/cdown/srt/issues/62
print(ft[:20])
with open(fp3, 'wb') as f:
    f.write(ft.encode())
    # f.write(srt.compose(subs).encode())
    print(fp3)


def main():
    pass


if __name__ == '__main__':
    main()
