# -*- encoding: utf-8 -*-
'''
@File    :   ffmpeg1.py
@Time    :   2021/03/06 23:52:55
@Author  :   play4fun
@Desc    :   使用m3u8-downloader下载ts片段后，使用FFmpeg合并视频
'''

import os
def main():
    fl=sorted(os.listdir('.'))
    txt=''
    for f in fl:    
        print(f"file '{f}'")
        if f.endswith('mp4'):
            txt+=f"file '{f}'\n"
    with open('filelist.txt','w') as f:
        f.write(txt)

    cmd='ffmpeg -f concat -safe 0 -i filelist.txt -c copy output.mp4'
    print(cmd)
    os.system(cmd)
    pass

if __name__ == "__main__":
    main()
