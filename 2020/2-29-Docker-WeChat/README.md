

## 在Docker 运行 微信Windows版

- 视频  [微信营销？在Docker运行微信Windows版，机器人自动回复淘口令](https://www.bilibili.com/video/av92594352)

- 参考
    - [DoChat-Dockerized WeChat (盒装微信) ](https://github.com/huan/docker-wechat)
        - https://hub.docker.com/r/zixia/wechat
        - docker pull zixia/wechat
    - https://github.com/bestwu/docker-wechat
        - 2019年10月17日[Linux 下 完美运行 wechat](https://www.kpromise.top/run-wechat-in-linux/)
        - 本镜像基于深度操作系统 https://hub.docker.com/r/bestwu/wechat
        - docker pull bestwu/wechat

- 要求
    - Ubuntu19.10，我使用VMware虚拟机
    - 安装Docker
        - sudo apt update && apt install docker.io
    - 微信测试账号
    - 新建DoChat和WeChatFiles文件夹
    - 检查输出
        -  sudo docker logs -f --tail 30 wechat

```
sudo docker run -d --name wechat --device /dev/snd \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v $HOME/WeChatFiles:/WeChatFiles \
    -e DISPLAY=unix$DISPLAY \
    -e XMODIFIERS=@im=fcitx \
    -e QT_IM_MODULE=fcitx \
    -e GTK_IM_MODULE=fcitx \
    -e AUDIO_GID=`getent group audio | cut -d: -f3` \
    -e GID=`id -g` \
    -e UID=`id -u` \
    bestwu/wechat
```
