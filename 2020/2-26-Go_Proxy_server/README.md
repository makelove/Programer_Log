## 2-26-最简单的翻墙代理

- 视频  
    - 失效了。 [越狱？最简单的代理服务器Go，翻过防火墙](https://www.bilibili.com/video/av91817713/)
    - 百度网盘
        - 链接:https://pan.baidu.com/s/15qUFJKDMBDUl6ldlXh-zzQ  密码:jnxi
    - 今日头条
        - https://www.ixigua.com/home/1789618645372350/video/

- 参考
    - [chrome 67版本后无法拖拽离线安装CRX格式插件的解决方法](https://chromecj.com/utilities/2018-09/1525.html)
    - [解决Chrome插件安装时程序包无效:"CRX_HEADER_INVALID"](https://blog.csdn.net/wst0717/article/details/88867047)

- 单步调试
    - curl -x 127.0.0.1:8081  http://httpbin.org/ip

- 交叉编译 Linux
    - CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build .

- 部署到服务器
    - 端口
    - 测试 curl -x 42.56.89.102:8081  https://httpbin.org/ip

- host屏蔽域名 www.baidu.com
    - 切换代理

- 浏览器插件 https://proxy-switchyomega.com/
    - 配置

- 因为没有国外服务器，所以用【百度】来演示了。

- 对代理进行【压力测试】？