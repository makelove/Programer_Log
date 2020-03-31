# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 10:53
# @File    : broadlink1.py


"""
broadlink1.py:
https://www.domoticz.cn/forum/viewtopic.php?f=33&t=22&sid=3cc9783df8f361e02b039be216c0d6ba

在无线路由器中找到
BroadLink_OEM-T1-1e-0d-8e
IP：192.168.0.107 | MAC：78-0f-77-1e-0d-8e | 2.4G无线连接

"""


def main2():
    import broadlink
    import sys

    device_ip = '192.168.0.107'  # "博联设备IP"
    device_port = 80

    device_mac = '780f771e0d8e'  # "博联设备mac地址"
    # mac地址例子："B443xxxxD329"，

    # device_type = "broadlink.mp1"
    device_type = 0x4EF7  # Honyar oem mp1
    # 在 broadlink.__init__.py gendevice() 函数中找到

    socket = str(sys.argv[1])
    # socket = 's1'
    action = str(sys.argv[2])
    # action = 'on'

    device = broadlink.mp1(host=(device_ip, device_port), mac=bytearray.fromhex(device_mac), devtype=device_type)

    device.auth()
    # device.host

    if action == "on":
        if socket == "s1":
            device.set_power(1, True)
        elif socket == "s2":
            device.set_power(2, True)
        elif socket == "s3":
            device.set_power(3, True)
        elif socket == "s4":
            device.set_power(4, True)
    elif action == "off":
        if socket == "s1":
            device.set_power(1, False)
        elif socket == "s2":
            device.set_power(2, False)
        elif socket == "s3":
            device.set_power(3, False)
        elif socket == "s4":
            device.set_power(4, False)
        elif action == "status":
            print("on" if device.check_power()[socket] else "off")
    pass


def main():
    import broadlink
    myssid = 'myssid'
    mynetworkpass = 'mynetworkpass'
    broadlink.setup(myssid, mynetworkpass, 3)  # 没用
    pass


if __name__ == '__main__':
    main2()
