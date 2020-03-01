# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 14:58
# @File    : macOS-siri-百度翻译-TTS.py


"""
macOS-siri-百度翻译-TTS.py:

你好 早上好，你吃饭了吗？

国际和平，让和平白鸽自由飞翔，带去安宁温馨；让美好橄榄枝四处蔓延，编织幸福世界；让和谐旗帜随风飘扬，传递快乐心语。祝愿世界和平，永无战争！
"""
import time
from AppKit import NSSpeechSynthesizer
from baidu_translate_api import translate

nssp = NSSpeechSynthesizer
ve = nssp.alloc().init()

#来源 https://stackoverflow.com/questions/29152617/nsspeechsynthesizer-voice-language-relations
voices = {#注释掉的语言是百度翻译API不支持的
    "en": ("com.apple.speech.synthesis.voice.Alex", '英语'),  # 英语
    "ru": ("com.apple.speech.synthesis.voice.milena", '俄语'),  # 俄语
    "ara": ("com.apple.speech.synthesis.voice.tarik", '阿拉伯'),  # 阿拉伯
    "hu": ("com.apple.speech.synthesis.voice.mariska", '匈牙利'),  # 匈牙利
    "nl": ("com.apple.speech.synthesis.voice.ellen", '荷兰'),  # 荷兰
    "el": ("com.apple.speech.synthesis.voice.melina", '希腊'),  # 希腊
    "dan": ("com.apple.speech.synthesis.voice.sara", '丹麦'),  # 丹麦
    # "he": ("com.apple.speech.synthesis.voice.carmit",'以色列'),#以色列 希伯来语
    # "id": ("com.apple.speech.synthesis.voice.damayanti",'印度尼西亚'),#印度尼西亚
    "spa": ("com.apple.speech.synthesis.voice.Jorge", '西班牙'),  # 西班牙
    "it": ("com.apple.speech.synthesis.voice.alice", '意大利'),  # 意大利
    "kor": ("com.apple.speech.synthesis.voice.yuna", '韩国'),  # 韩国
    "de": ("com.apple.speech.synthesis.voice.anna", '德国'),  # 德国
    # "no": ("com.apple.speech.synthesis.voice.nora",'挪威'),#挪威
    "pl": ("com.apple.speech.synthesis.voice.zosia", '波兰'),  # 波兰
    "pt": ("com.apple.speech.synthesis.voice.joana", '葡萄牙'),  # 葡萄牙
    "rom": ("com.apple.speech.synthesis.voice.ioana", '罗马尼亚'),  # 罗马尼亚
    "slo": ("com.apple.speech.synthesis.voice.laura", '斯洛伐克'),  # 斯洛伐克，借用 斯洛文尼亚
    "th": ("com.apple.speech.synthesis.voice.kanya", '泰国'),  # 泰国
    # "tr": ("com.apple.speech.synthesis.voice.yelda",'土耳其'),#土耳其
    "fin": ("com.apple.speech.synthesis.voice.satu", '芬兰'),  # 芬兰
    "fra": ("com.apple.speech.synthesis.voice.thomas", '法国'),  # 法国
    # "hi": ("com.apple.speech.synthesis.voice.lekha",'印度'),  # 印度-印地语
    "cs": ("com.apple.speech.synthesis.voice.zuzana", '捷克'),  # 捷克
    "swe": ("com.apple.speech.synthesis.voice.alva", '瑞典'),  # 瑞典
    "jp": ("com.apple.speech.synthesis.voice.kyoko", '日语')  # 日语
}


def say(voice, text):
    # print(voice)
    # print(text)
    ve.setVoice_(voice)
    ve.startSpeakingString_(text)

    while not ve.isSpeaking():  # 等待发音
        time.sleep(0.1)

    while ve.isSpeaking():  # 等待结束
        time.sleep(0.1)
    # print('-' * 20)


def main():
    text = input('请输入中文:')
    # text = '早上好，你吃饭了吗'
    print(text)
    # sp = nssp.alloc().initWithVoice_()
    # sp.startSpeakingString_(text)

    # 普通话
    print('普通话')
    say('com.apple.speech.synthesis.voice.ting-ting', text)
    # 台湾
    print('台湾')
    say('com.apple.speech.synthesis.voice.mei-jia', text)
    # 香港
    print('香港')
    say('com.apple.speech.synthesis.voice.sin-ji', text)

    # for
    for lang, (voice, country) in voices.items():
        print(country, '\t', lang, '\t', voice)
        try:
            transtr = translate(text, froml='zh', tol=lang)#翻译api可能限流
        except Exception as e:
            print('Exception',e)
            continue
            pass
        
        print(transtr)
        say(voice, transtr)
        print('-' * 40)
        # time.sleep(0.5)
    pass


if __name__ == '__main__':
    main()
