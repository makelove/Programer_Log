TTS 从文本到语音(TextToSpeech) 语音合成

- macos say
使用文档
man say

命令行
say 'TTS是Text To Speech的缩写，即“从文本到语音”，是人机对话的一部分，让机器能够说话。'

保存为文件
say 'TTS是Text To Speech的缩写，即“从文本到语音”，是人机对话的一部分，让机器能够说话。' -o tts.aiff

转成mp3
brew install lame
lame -m m tts.aiff tts.mp3

发音人
【系统偏好设置】>>【辅助功能】>>【语音】


2. 更好的发音系统，更多选择
讯飞语音
https://www.xfyun.cn/services/online_tts
文档
https://www.xfyun.cn/doc/tts/online_tts/API.html

demo代码写得很烂
不方便使用，需要重写


