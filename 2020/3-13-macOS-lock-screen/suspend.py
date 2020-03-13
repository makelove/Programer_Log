# -*- encoding: utf-8 -*-
'''
@File    :   suspend.py
@Time    :   2020/03/13 09:36:08
@Author  :   play4fun
@Desc    :   https://www.reddit.com/r/Python/comments/2rrb29/need_a_way_to_lock_and_unlock_macbook_screen_with/

登录窗口
退出当前账号
可以休眠

192.30.253.118 gist.github.com
'''

from time import sleep
import os,sys

def lock():
    cmd='/System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession -suspend'
    print(cmd)
    os.system(cmd)
    pass

if __name__ == "__main__":
    if len(sys.argv)==2:
        minute=int(sys.argv[1])        
    else:
        print('suspend.py 分钟数')
        minute=45
    
    print(f"{minute}分钟后退出会话")
    sleep(minute*60)
    lock()
