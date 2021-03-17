

## 怎样制作自己的虚拟偶像

- 视频 [【轻松搞定】怎样制作自己的虚拟偶像？VMagicMirror，开源免费！](https://www.bilibili.com/video/BV1BZ4y1w7iw/)

- 修改/etc/hosts
```
185.199.111.153 malaybaku.github.io
104.18.31.199 accounts.pixiv.net
104.18.31.199 oauth.secure.pixiv.net
```

- 参考
    - 官网 https://malaybaku.github.io/VMagicMirror/en/index
        - GitHub源代码 https://github.com/malaybaku/VMagicMirror
    - 下载 https://malaybaku.github.io/VMagicMirror/en/download
        - BOOTH 网站需要注册
        - 解压到硬盘，点击VMagicMirror.exe运行
            - 2个窗口，不要关闭
- 使用 https://malaybaku.github.io/VMagicMirror/en/get_started
    - 设置语言为英文
    - 在VRoid Hub中使用模型，需要验证签约
        - 拿到一个授权代码，输入
        - 在模型窗口选择模型，下载
    - 嘴唇与麦克风同步 LipSync口型同步
        - 一开始正常，后来就不同步了，奇怪！
    - 摄像头，头部跟踪
    - 手部追踪 ？？要买Leap Motion
    - 言语到运动 Word To Motion 控制面部表情的功能
        - 使用键盘的数字键，切换不同表情动作
    - PPT幻灯片演示 
        - 选中Presentation-like hand移动VRM的右手，就好像他/她正在演示中一样。
    - 窗口透明
        - 默认是绿幕
    - 外部跟踪器 Ex.Tracker 
        - 文档 https://malaybaku.github.io/VMagicMirror/en/docs/external_tracker
        - 支持Face ID的iPhone App ： iFacialMocap
    - 直播 https://malaybaku.github.io/VMagicMirror/en/tips/virtual_camera
        - 安装OBS Studio
            - 创建一个新来源，选择Game Capture游戏捕获
            - 选择Mode到Capture Specific Window。
            - 单击右侧的Window，然后选择[VMagicMirror.exe]: VMagicMirror。
            - 检查Allow Transparancy。
            - 调整位置，缩放