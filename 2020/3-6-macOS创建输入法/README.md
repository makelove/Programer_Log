# 很简单！macOS创建自己的输入法

- 视频 ？

- 参考
    - [在 Mac 上创建和使用您自己的输入法](https://support.apple.com/zh-cn/guide/mac-help/mchlp2866/mac)
    - [GitHub粤语拼音](https://github.com/ache051/mac_cantonese)

- 步骤
    - 使用macOS的【文本编辑】新建一个【文本文档】
        - 请选取“格式”>“制作纯文本”。
        - 使用 Unicode (UTF-16) 编码存储文件，并使用诸如“.inputplugin”的扩展名。
        - 按照【规范】填写 输入法的键和对应的中文
        - 双击 该文件
        - 打开【系统偏好设置】，键盘，输入法，进行添加
        - 搞定


- 优化
    - 输入法的键和对应的中文，可以通过一些词库进行更新

- 缺点
    - 不能像其他输入法那样，在输入的同时展示候选单词
        - 必须输入按键后，再按下空格键，才能展示候选单词
        - 我还没找到怎样进一步设置的攻略。。。

- 安装文件，系统路径
```
#用户路径
(.py3) localhost:~ play$ ll ~/Library/Input\ Methods/
total 8
drwx------+  4 play  staff   128B  3  6 16:44 ./
drwx------@ 81 play  staff   2.5K  2 15 23:02 ../
-rw-------   1 play  staff     0B  6 12  2019 .localized
-rw-r--r--@  1 play  staff   456B  3  6 16:42 bili_utf16.inputplugin

#系统路径
(.py3) localhost:~ play$ ll /Library/Input\ Methods/
total 0
drwxr-xr-x   3 root  wheel    96B  3  6 16:11 ./
drwxr-xr-x  68 root  wheel   2.1K  3  3 21:15 ../
drwxrwxr-x   3 root  staff    96B 11  6 12:31 SogouInput.app/

#搜狗输入法
(.py3) localhost:~ play$ ll /Library/Input\ Methods/SogouInput.app/Contents/
total 4120
drwxrwxr-x   19 play  staff   608B  3  6 09:50 ./
drwxrwxr-x    3 root  staff    96B 11  6 12:31 ../
drwxrwxr-x    4 play  staff   128B 11  6 12:17 Frameworks/
-rwxrwxr--    1 play  staff   3.6K  3  6  2022 Info.plist*
drwxrwxr-x    3 play  staff    96B 11  6 12:17 MacOS/
-rwxrwxr--    1 play  staff     8B  3  6  2022 PkgInfo*
drwxrwxr-x  173 play  staff   5.4K 11  6 12:17 Resources/
drwxrwxr-x    3 play  staff    96B 11  6 12:17 SGAssistPanel.app/
drwxrwxr-x    3 play  staff    96B 11  6 12:17 SGEmojiPanelTool.app/
drwxrwxr-x    3 play  staff    96B 11  6 12:17 SGInputStatPanel.app/
drwxrwxr-x    3 play  staff    96B 11  6 12:17 SGPicFaceTool.app/
-rwxrwxr--    1 play  staff   137K  3  6  2022 SogouHelper*
drwxrwxr-x    3 play  staff    96B 11  6 12:17 SogouPreference.app/
-rwxrwxr--    1 play  staff   132K  3  6  2022 SogouProcessInfo*
-rwxrwxr--    1 play  staff   1.5M  3  6  2022 SogouServices*
drwxrwxr-x    3 play  staff    96B 11  6 12:17 SogouTaskManager.app/
-rwxrwxr--    1 play  staff   199K  3  6  2022 SogouXdelta*
drwxrwxr-x    3 play  staff    96B 11  6 12:17 _CodeSignature/
-rw-r--r--    1 play  staff   643B  3  6 09:50 updateOrder.plist
```
