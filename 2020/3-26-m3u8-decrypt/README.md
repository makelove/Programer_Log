

# 解密 m3u8

- 视频 [冷门知识！解密m3u8视频，下载ts文件后用FFmpeg合并](https://www.bilibili.com/video/BV17c411h7z7/)
    - 上次视频 [怎样用Python下载m3u8视频](https://www.bilibili.com/video/BV1ft41137Ad/)
        - python代码 [怎样下载m3u8视频](https://github.com/makelove/Python_Master_Courses/blob/master/%E5%9B%BE%E5%83%8F%E8%A7%86%E9%A2%91%E5%A4%84%E7%90%86/%E6%80%8E%E6%A0%B7%E4%B8%8B%E8%BD%BDm3u8%E8%A7%86%E9%A2%91/download_m3u8.py) 

- Library https://github.com/globocom/m3u8

- 为了保护自己的视频文件，视频网站会对m3u8和ts文件进行加密
    - 使得下载后的ts文件在合并后，无法打开

- FFmpeg工具
    - 直接下载，合并  
        - ffmpeg -i HdNz1kaz.m3u8 -c copy new.mp4

- 参考
    - [m3u8 文件格式详解](https://www.jianshu.com/p/e97f6555a070)
        - HLS 是新一代流媒体传输协议，其基本实现原理为将一个大的媒体文件进行分片，将该分片文件资源路径记录于 m3u8 文件（即 playlist）内，其中附带一些额外描述（比如该资源的多带宽信息···）用于提供给客户端。客户端依据该 m3u8 文件即可获取对应的媒体资源，进行播放。

    - [FFmpeg解码M3U8合并解密TS到MP4](https://luluit.top/archives/2070.html)
    - [加密的m3u8、ts文件合并](https://blog.csdn.net/guanxiao1989/article/details/90529865)
        - 方法很多，建议多看一下
    - [How to decrypt .ts file (AES-128)?](https://www.reddit.com/r/ffmpeg/comments/c3e6jw/how_to_decrypt_ts_file_aes128/)
        - 解决 ffmpeg -allowed_extensions ALL -i "C:\input\9215d654965805dada3ac5327130c1ef_1.m3u8" -c copy output.mp4
    - [Decrypting And Combining .ts Audio Files with .m3u8](https://stackoverflow.com/questions/34235397/decrypting-and-combining-ts-audio-files-with-m3u8)

- 解密
    - [打造m3u8视频（流视频）下载解密合并器(kotlin)](https://www.cnblogs.com/stars-one/p/12198572.html) 纯代码编程，不用FFmpeg工具
    - [幕课客户端 AES-128 解密播放流程(二)](https://juejin.im/entry/6844903486027464717)
        - 分析过程很好，值得参考