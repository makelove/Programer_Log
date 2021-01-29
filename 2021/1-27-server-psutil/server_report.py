# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 10:33
# @File    : t1.py


"""
t1.py:
"""
import psutil


def cpu_percent():
    rt = ''

    # psutil.net_if_addrs()
    d = psutil.net_if_addrs()
    ip = ''
    for itf, l in d.items():
        # print(itf)
        for x in l:
            print(x,x.netmask)
            # print(x.netmask)
            # if x.netmask=='255.255.255.0':#网段掩码
            #     print('\t',x.address)
            if x.address.startswith('192.'):  # TODO 修改ip
                print('\tIP:', x.address)
                ip = x.address
                break
            # if isinstance():
            #

    mem = psutil.virtual_memory()
    if mem.percent >= 70:
        rt += f'内存-百分比：{mem.percent}\n'
        # psutil.net_if_stats()

    disk = psutil.disk_usage('/')
    if disk.percent >= 70:
        rt += f'硬盘-百分比：{disk.percent}\n'

    # cpu_count=psutil.cpu_count()
    # for i in range(cpc):
    #     print(f'CPU {i} : {psutil.cpu_percent(i)}')

    # s1 = f'CPU 10秒统计: {psutil.cpu_percent(interval=10)}'
    # print(s1)
    # s2 = f'{cpu_count}个CPU 10秒统计 : {psutil.cpu_percent(interval=10, percpu=True)}'
    # print(s2)

    cpup = psutil.cpu_percent(interval=10)
    if cpup >= 10:
        rt += f'CPU 10秒统计：{cpup}\n'

    # rt = f'''服务器 {ip}
    # 硬盘-百分比：{disk}
    # 内存-百分比：{mem.percent}
    # {s1}
    # {s2}
    #
    # '''
    if rt != '':
        rt = f'统计：\n服务器 {ip}\n' + rt
    return rt
    pass


def main():
    from dingtalkchatbot.chatbot import DingtalkChatbot

    # WebHook地址
    webhook ='https://oapi.dingtalk.com/robot/send?access_token=xx'
    secret ='xx'

    # 初始化机器人小丁
    xiaoding = DingtalkChatbot(webhook, secret=secret)  # 方式二：勾选“加签”选项时使用（v1.5以上新功能）

    # Text消息@所有人
    msg = cpu_percent()
    if msg == '':
        print('服务器正常，不发消息')
        return

    # msg = '统计：\n' + cpu
    print(msg)
    rs = xiaoding.send_text(msg=msg, is_at_all=False, at_dingtalk_ids=['xx'])  # TODO @某人
    print('发送完毕', rs)
    pass


if __name__ == '__main__':
    main()
    # cpu_percent()
