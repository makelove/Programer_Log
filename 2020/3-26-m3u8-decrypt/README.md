

# 解密 m3u8

- 视频 ？
    - 上次视频 [怎样用Python下载m3u8视频](https://www.bilibili.com/video/BV1ft41137Ad/)
        - python [怎样下载m3u8视频](https://github.com/makelove/Python_Master_Courses/blob/master/%E5%9B%BE%E5%83%8F%E8%A7%86%E9%A2%91%E5%A4%84%E7%90%86/%E6%80%8E%E6%A0%B7%E4%B8%8B%E8%BD%BDm3u8%E8%A7%86%E9%A2%91/download_m3u8.py) 

- Library https://github.com/globocom/m3u8

- 为了保护自己的视频文件，视频网站会对m3u8和ts文件进行加密
    - 使得下载后的ts文件在合并后，无法打开


- 参考
    - [FFmpeg解码M3U8合并解密TS到MP4](https://luluit.top/archives/2070.html)
    - [加密的m3u8、ts文件合并](https://blog.csdn.net/guanxiao1989/article/details/90529865)
    - [How to decrypt .ts file (AES-128)?](https://www.reddit.com/r/ffmpeg/comments/c3e6jw/how_to_decrypt_ts_file_aes128/)
        - 解决 ffmpeg -allowed_extensions ALL -i "C:\input\9215d654965805dada3ac5327130c1ef_1.m3u8" -c copy output.mp4
    - [Decrypting And Combining .ts Audio Files with .m3u8](https://stackoverflow.com/questions/34235397/decrypting-and-combining-ts-audio-files-with-m3u8)
