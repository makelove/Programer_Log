# Ubuntu安装Wine-执行Windows程序

- 参考
    - https://www.winehq.org/
    - 安装指南Ubuntu https://wiki.winehq.org/Ubuntu_zhcn
    - http://ubuntuhandbook.org/index.php/2019/12/install-wine-4-21-ubuntu-19-10/

- 视频 ？

- 步骤
```
sudo dpkg --add-architecture i386
wget -nc https://dl.winehq.org/wine-builds/winehq.key
sudo apt-key add winehq.key
sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main'
sudo add-apt-repository ppa:cybermax-dexter/sdl2-backport
不要安装开发版
sudo apt install --install-recommends winehq-devel
安装稳定版
sudo apt install --install-recommends winehq-stable


wine --version
wine-5.3
```

- wine 第一次运行
    - /home/play/.wine

    - 安装.net Wine Mono安装器
    -  Gecko安装器 HTML
    

- 安装微信 https://pc.weixin.qq.com/
