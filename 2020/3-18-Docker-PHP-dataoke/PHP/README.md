- 本地测试 

## 修改hosts 
vi /etc/hosts
127.0.0.1 youhui.dark.net.cn

搞错了 fmp
https://www.runoob.com/docker/docker-install-php.html

## Docker
https://hub.docker.com/_/php?tab=description
下载
docker pull php:5.6-fpm

## 大淘客cms
https://www.dataoke.com/pmc/basic.html
下载index.php文件并上传到您自己的服务器
CMS：高效转链PID
用户在cms购买时使用该PID为您转链
更新授权

docker run -it --rm  -v "$PWD":/usr/src/myapp -w /usr/src/myapp php php phpinfo.php

需要Nginx来配合

## 启动PHP
OK
docker run  --name  myphp-fpm -v "$PWD"/nginx/www:/www   php:5.6-fpm

## 启动nginx
docker run  -p 80:80 -it --rm \
    -v "$PWD"/nginx/www:/usr/share/nginx/html:ro \
    -v "$PWD"/nginx/conf/conf.d:/etc/nginx/conf.d:ro \
    --link myphp-fpm:php \
    nginx

## 浏览器打开
- http://youhui.dark.net.cn/

- demo网站 http://www.yangchun.so/
