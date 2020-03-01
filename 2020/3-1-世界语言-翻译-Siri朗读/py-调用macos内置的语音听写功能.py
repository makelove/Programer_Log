# coding=utf-8
#Python Text to Speech in Macintosh
#https://stackoverflow.com/questions/12758591/python-text-to-speech-in-macintosh
#文本到语音 TTS


from  AppKit import NSSpeechSynthesizer
import time
import sys


if len(sys.argv) < 2:
   text = raw_input('type text to speak> ')
else:
   text = sys.argv[1]

nssp = NSSpeechSynthesizer

ve = nssp.alloc().init()

for voice in nssp.availableVoices():
   ve.setVoice_(voice)
   print voice
   ve.startSpeakingString_(text)

   while not ve.isSpeaking():#等待发音
      time.sleep(0.1)

   while ve.isSpeaking():#等待结束
      time.sleep(0.1)


#来源 https://stackoverflow.com/questions/29152617/nsspeechsynthesizer-voice-language-relations
 voices = {
  "en": "com.apple.speech.synthesis.voice.Alex",#英语
  "ru": "com.apple.speech.synthesis.voice.milena",#俄语
  "ara": "com.apple.speech.synthesis.voice.tarik",#阿拉伯
  "hu": "com.apple.speech.synthesis.voice.mariska",#匈牙利
  "nl": "com.apple.speech.synthesis.voice.ellen",#荷兰
  "el": "com.apple.speech.synthesis.voice.melina",#希腊
  "dan": "com.apple.speech.synthesis.voice.sara",#丹麦
  # "he": "com.apple.speech.synthesis.voice.carmit",#以色列 希伯来语
  # "id": "com.apple.speech.synthesis.voice.damayanti",#印度尼西亚
  "spa": "com.apple.speech.synthesis.voice.Jorge",#西班牙
  "it": "com.apple.speech.synthesis.voice.alice",#意大利
  # "zh": "com.apple.speech.synthesis.voice.ting-ting",#中国
  "kor": "com.apple.speech.synthesis.voice.yuna",#韩国
  "de": "com.apple.speech.synthesis.voice.anna",#德国
  # "no": "com.apple.speech.synthesis.voice.nora",#挪威
  "pl": "com.apple.speech.synthesis.voice.zosia",#波兰
  "pt": "com.apple.speech.synthesis.voice.joana",#葡萄牙
  "rom": "com.apple.speech.synthesis.voice.ioana",#罗马尼亚
  "slo": "com.apple.speech.synthesis.voice.laura",#斯洛伐克，借用 斯洛文尼亚
  "th": "com.apple.speech.synthesis.voice.kanya",#泰国
  # "tr": "com.apple.speech.synthesis.voice.yelda",#土耳其
  "fin": "com.apple.speech.synthesis.voice.satu",#芬兰
  "fra": "com.apple.speech.synthesis.voice.thomas",#法国
  "hi": "com.apple.speech.synthesis.voice.lekha",#印度-印地语
  "cs": "com.apple.speech.synthesis.voice.zuzana",#捷克
  "swe": "com.apple.speech.synthesis.voice.alva",#瑞典
"jp": "com.apple.speech.synthesis.voice.kyoko"#日语
}