
# macOS 桌面通知
- 需求
    - 有时候需要发送消息通知自己
    - 手机-微信-查看消息不方便，影响工作
    - 在电脑上工作，可以使用【桌面通知】，Windows也有

- 视频 [macOS桌面通知，Python编程，统计B站粉丝播放量](https://www.bilibili.com/video/BV1b741127CJ/)

- 参考
    - https://stackoverflow.com/questions/17651017/python-post-osx-notification
    
- 命令行
    - osascript -e 'display notification "通知内容" with title "标题" subtitle "子标题"'
    
   
- python编程
```python
import os

def notify(title, text):
    os.system("""
    osascript -e 'display notification "{}" with title "{}"'
    """.format(text, title))

notify("Title", "Heres an alert")
```

- 用途
    - B站 数据统计
    - 股票 涨跌 警告
    - 突发事件 地震