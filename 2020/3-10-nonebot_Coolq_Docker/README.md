# nonebot+酷Q+Docker

- 视频

- 安装
    - pip install nonebot


- Docker
```
docker pull richardchien/cqhttp:latest
mkdir coolq  # 用于存储 酷Q 的程序文件
docker run -ti  --name cqhttp-test \
             -v $(pwd)/coolq:/home/user/coolq \
             -p 9000:9000 \
             -p 5700:5700 \
             -e COOLQ_ACCOUNT=2262965903 \
             -e CQHTTP_POST_URL=http://127.0.0.1:8080 \
             -e CQHTTP_SERVE_DATA_FILES=yes \
             richardchien/cqhttp:latest
             
#之后
docker start cqhttp-test
docker logs -f cqhttp-test
docker stop cqhttp-test

```
然后访问 http://<你的IP>:9000/ 
进入 noVNC（默认密码 MAX8char ），登录 酷Q，即可开始使用
（插件已自动启用，配置文件也根据启动命令的环境变量自动生成了）。
一般情况下，你不太需要关注插件是如何存在于容器中的。

配置文件位置
- /Users/play/CODE/QQ/kuQ/coolq/app/io.github.richardchien.coolqhttpapi/config/2262965903.ini
```
[2262965903]
ws_reverse_api_url=ws://192.168.0.222:8080/ws/api/
ws_reverse_event_url=ws://192.168.0.222:8080/ws/event/
use_ws_reverse=yes
```
