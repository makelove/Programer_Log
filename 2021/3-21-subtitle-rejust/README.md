

## srt字幕调整，延时32秒


- 参考
	- https://github.com/cdown/srt
	    - 好用
		- 文档 http://srt.readthedocs.org/en/latest/api.html
		
- 步骤
    - 下载电影《扎克·施奈德版正义联盟(Zack Snyder's Justice League) (2021)》 https://github.com/makelove/Programer_Log/issues/5
    - 从字幕网站下载字幕，发现字幕版本不对应。字幕提前了32秒
    - 电影自带英文字幕，使用FFmpeg把字幕剥离 sub1.srt
        - ffmpeg.exe -i 'Zack.Snyders.Justice.League.2021.REPACK.720p.HDRip.1200MB.x264-GalaxyRG.mkv' -map 0:s:0 sub1.srt
    - 对比中文字幕和英文字幕，同一句话的时间，确定相差了多长时间
    - 编写python代码，jl1.py