# -*- coding: utf-8 -*-
# @Time    : 2020/12/19 13:29
# @File    : password.py


"""
password.py:
password-generator
快捷方式
alias pw='python3 /Users/play/CODE/Python_Test/密码生成器/password.py'
"""

import sys
import random, string


def 不重复(size=6, chars=string.ascii_letters + string.digits):
    pw = ''
    for _ in range(size):
        x = random.choice(chars)
        pw += x
        chars = chars.replace(x, '')
        pass
    return pw


def random_string_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def main(size):
    # return random_string_generator(size)
    return 不重复(size)
    pass


if __name__ == '__main__':
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = 8

    if num > 62:
        print('长度太大')
    else:
        rs = main(num)
        print(rs)
