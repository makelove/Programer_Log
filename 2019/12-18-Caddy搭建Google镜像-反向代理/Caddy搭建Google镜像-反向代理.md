- 官网
    - https://github.com/caddyserver/caddy
    - 下载 https://caddyserver.com/v1/download

- 参考
    - [caddy 搭建google 镜像,很容易](https://www.banwagongzw.com/33.html)
    - 安装脚本
        - https://github.com/ToyoDAdoubi/doubi/blob/master/caddy_install.sh

- 视频
    - [Caddy搭建Google镜像-反向代理](https://www.bilibili.com/video/av79726017/)

- 配置
    - 最后在Chrome浏览器安装扩展【删除谷歌重定向】
```shell script
(.py3) localhost:caddy_v1.0.4_linux_amd64 play$ cat Caddyfile
:80 {
 gzip
 proxy / https://www.baidu.com
}
```    

## 还需要买一个服务器   
- 国外
    - [vultr](https://www.vultr.com/?ref=8349543) 