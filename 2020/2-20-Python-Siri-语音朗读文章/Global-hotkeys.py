# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 17:50
# @File    : Global-hotkeys.py


"""
Global-hotkeys.py: 全局热键

只支持一对热键
"""

from pynput import keyboard


def on_activate():
    print('Global hotkey activated!')


def for_canonical(f):
    return lambda k: f(listener.canonical(k))


hotkey = keyboard.HotKey(
    # keyboard.HotKey.parse('<ctrl>+<alt>+1'),
    keyboard.HotKey.parse('<ctrl>+1'),
    on_activate)

with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as listener:
    listener.join()


def main():
    listener.start()
    pass


if __name__ == '__main__':
    main()
