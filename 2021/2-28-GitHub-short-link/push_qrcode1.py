# -*- coding: utf-8 -*-
# @Time    : 2021/3/1 12:17
# @File    : push_qrcode1.py


"""
push_qrcode1.py:
"""

import base64
import qrcode
from github import Github
from config import token

g = Github(token)
# repo = g.get_repo("MartinHeinz/python-project-blueprint")
repo = g.get_repo("makelove/makelove.github.io")


def QRCode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    # data = '8👈￥V0RPcyl5PTI￥ https://m.tb.cn/h.4lGcAwM  兔笼全景外壳gopro max配件gopromax麦克风拓展固定支架冷靴边框'
    # text='￥V0RPcyl5PTI￥兔笼全景外壳gopro max配件gopromax麦克风拓展固定支架冷靴边框'
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    # img.save('tkl-标题.png')
    # data = img.get_image()
    import io
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    data = img_byte_arr.getvalue()
    return data


def main(text, path=None):

    data = QRCode(text)
    # content = base64.b64encode(data)#不需要
    # path = "qr/tk2.png"  # TODO 存储起来，与原始URL映射
    # rs = repo.create_file(path=path, message="tkl", content=data, branch="master")

    if path is None:
        path = "qr/tk3.png"  # TODO 存储起来，与原始URL映射
        rs = repo.create_file(path=path, message="test", content=data, branch="master")
    else:
        contents = repo.get_contents(path)
        rs = repo.update_file(contents.path, message="update_file", content=data, sha=contents.sha, branch="master")

    print('结果：', rs)#{'commit': Commit(sha="6821ebd50c434a2061b34b2904d56135a5809838"), 'content': ContentFile(path="qr/tk2.png")}
    turl = 'https://dark.net.cn/' + path  # https://dark.net.cn/qr/tk2.png
    print('目标URL：', turl)
    pass


if __name__ == '__main__':
    text = '￥V0RPcyl5PTI￥兔笼全景外壳gopro max配件gopromax麦克风拓展固定支架冷靴边框'
    text = '啊GGHCcyrdkcR哈罗德 RODE VideoMic NTG麦克风相机枪式锂电手机录音麦笔记本话筒'
    # main(text)

    # text = '￥uZCLcyr1dhz￥高钙乳酪棒 儿童零食芝士棒健康营养120g'
    text = '9👈，RpUacyrUwru信 正品INTEX探险者二人充气船两人充气艇橡皮划艇2人冲锋独木舟加厚'
    path = "qr/tk3.png"
    main(text,path)
