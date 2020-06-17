
# 观鸟App抓包，并下载鸟声音频

- 视频  ??

- 参考
    - iOS App ：鸟类百科
        - 康奈尔大学 鸟类观察 https://www.birds.cornell.edu/home
            - 鸟类资料是存放在大学的服务器上，所以国内下载缓慢 download.ams.birds.cornell.edu
    - 国内网站，没有音频。[鸟类_百问中文](http://www.baiven.com/q/18/218/)

- 步骤
    - 启动 mitmweb
        - 过滤域名 ~d bird.snowyevening.com | ~d download.ams.birds.cornell.edu
    - 手机设置WiFi代理
    - 启动App，抓包
    - 推荐列表
        - POST http://bird.snowyevening.com:8008/api/recommendlist
            - {"applan":"zh-Hans","appvision":"3.2.4","page":0}
    - 热门列表
        - POST http://bird.snowyevening.com:8008/api/hotranklist
    - 详情
        - POST http://bird.snowyevening.com:8008/api/birddetail
            - {    "applan": "zh-Hans",    "appvision": "3.2.4",    "birdId": "27016" }
- 下载热门列表的鸟类，音频
    - download_sound.py
    - TODO 下一步，把全部鸟类的声音都下载下来
- 使用代理插件，更快地听到鸟类声音，不用等很久
    - mitmweb -s sound_proxy.py
