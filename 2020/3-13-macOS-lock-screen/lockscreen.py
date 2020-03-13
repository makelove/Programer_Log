# -*- encoding: utf-8 -*-
'''
@File    :   lockscreen.py
@Time    :   2020/03/13 10:15:23
@Author  :   play4fun
@Desc    :   https://gist.github.com/pudquick/350ba6411df3be77d32a
很快就锁屏了
只是锁屏
'''
from time import sleep
import os,sys
from ctypes import CDLL

def lock():
    loginPF = CDLL('/System/Library/PrivateFrameworks/login.framework/Versions/Current/login')
    result = loginPF.SACLockScreenImmediate()
    print('锁屏:',result)#0
    pass

if __name__ == "__main__":
    if len(sys.argv)==2:
        minute=int(sys.argv[1])        
    else:
        print('lockscreen.py 分钟数')
        minute=35
    
    print(f"{minute}分钟后锁屏")
    sleep(minute*60)
    lock()