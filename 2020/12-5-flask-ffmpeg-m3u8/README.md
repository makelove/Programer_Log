## Python编程，Flask网站播放m3u8流媒体

- 视频 [【Python编程】Flask网站播放m3u8流媒体](https://www.bilibili.com/video/BV15K4y1L7nF/)

- 步骤
    - FFmpeg切割视频，ts
    - m3u8指向ts段文件
    - 在浏览器端使用hls.js播放视频
- 代码
    - https://github.com/newnewcoder/flask-hls-demo
    - https://github.com/aminyazdanpanah/python-ffmpeg-video-streaming
        - 文档 https://video.aminyazdanpanah.com/python/start
    - m3u8文件解析 https://github.com/globocom/m3u8
- 加密m3u8
    - Encryption(DRM)
- 参考
    - [使用FFmpeg作为HLS流服务器（第1部分）– HLS基础](https://www.martin-riedl.de/2018/08/24/using-ffmpeg-as-a-hls-streaming-server-part-1/)
        - 第二部分 https://www.martin-riedl.de/2018/08/24/using-ffmpeg-as-a-hls-streaming-server-part-2/
    - [m3u8下载](https://gist.github.com/primaryobjects/7423d7982656a31e72542f60d30f9d30)
    
- ffmpeg 切割视频，生成m3u8
```shell script
ffmpeg  -i  input.mp4   \
   -c:v libx264 -crf 21 -preset veryfast \
    -c:a aac -b:a 128k -ac 2 \
    -f hls -hls_time 4 -hls_playlist_type event stream.m3u8

ffmpeg -i input.mp4  \
    -c:v libx264 -c:a aac -strict -2 -hls_time 20 -f hls output.m3u8
```  