# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 18:14
# @File    : copy-string-tts2.py


"""
copy-string-tts2.py:
支持多对热键

运行后
先选中文本
按 ctrl+c 复制
然后按照对应的热键
"""

from pynput import keyboard
import pyperclip as cp
import os

def say(voice):
    cpstr: str = cp.paste()
    print(cpstr)
    print('-'*20)
    if cpstr.strip():
        cmd = f'say -v {voice} "{cpstr}"'
        print(cmd)
        os.system(cmd)
        print('-'*40)
        pass

def on_activate_1():
    print('<ctrl>+1 pressed')
    say("Ting-Ting")


def on_activate_2():
    print('<ctrl>+2 pressed')
    say("Mei-Jia")
def on_activate_3():
    print('<ctrl>+3 pressed')
    say("Sin-ji")

def on_activate_4():
    print('<ctrl>+4 pressed')
    say("Allison")




def main():
    try:
        with keyboard.GlobalHotKeys({
                '<ctrl>+1': on_activate_1,
                '<ctrl>+2': on_activate_2,
                '<ctrl>+3': on_activate_3,
                '<ctrl>+4': on_activate_4,
            }) as h:
                h.join()
        h.start()
    except KeyboardInterrupt as e:
        print('KeyboardInterrupt',e)
        return
    except Exception as e:
        print('Exception',e)
        raise

    
    
    # listener.start()
    pass


if __name__ == '__main__':
    main()
