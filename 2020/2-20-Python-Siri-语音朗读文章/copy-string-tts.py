# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 18:00
# @File    : copy-string-tts.py


"""
copy-string-tts.py:
"""

from pynput import keyboard
import pyperclip as cp
import os


def get_listener(key, voice):
    def on_activate():
        print('Global hotkey activated!')

        cpstr: str = cp.paste()
        print(cpstr)
        if cpstr.strip():
            cmd = f'say -v {voice} "{cpstr}"'
            print(cmd)
            os.system(cmd)
            pass

    def for_canonical(f):
        return lambda k: f(listener.canonical(k))

    hotkey = keyboard.HotKey(
        # keyboard.HotKey.parse('<ctrl>+<alt>+1'),
        keyboard.HotKey.parse(key),
        on_activate)

    with keyboard.Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release)) as listener:
        listener.join()
    return listener


def main():
    listener1 = get_listener('<ctrl>+1', "Ting-Ting")
    listener1.start()

    # listener2 = get_listener('<ctrl>+2', "Mei-Jia")
    # listener2.start()#不行
    pass


if __name__ == '__main__':
    main()
