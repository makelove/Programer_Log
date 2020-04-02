
# 抖音 抓包 并存到 数据库
- 视频 [mitmproxy-抖音抓包，并把短视频链接存到MongoDB数据库](https://www.bilibili.com/video/BV1ae411x78w)

- 搜索接口
    - https://search-lf.amemv.com/aweme/v1/general/search/single/?version_code=10.4.0&js_sdk_version=1.55.0.3&app_name=aweme&vid=70A898D5-73F9-429E-857C-41789EF2CD25&app_version=10.4.0&device_id=69337363324&channel=App%20Store&mcc_mnc=&aid=1128&screen_width=640&openudid=708a9ae21c955c1e94c739033b9a2002e4aa9153&cdid=7A55D456-9D79-46A5-B641-ACA8506D7780&os_api=18&ac=WIFI&os_version=13.4&device_platform=iphone&build_number=104012&iid=109605200207&device_type=iPod9,1&is_vcd=1&idfa=7327A25C-725B-48D7-9132-153B648500E3&client_width=320&keyword=%E5%AE%9D%E9%AA%8F730&disable_synthesis=0&sort_type=0&is_filter_search=0&count=12&mac_address=02%3A00%3A00%3A00%3A00%3A00&single_filter_aladdin=0&is_pull_refresh=0&epidemic_card_type=2&multi_mod=0&query_correct_type=1&search_id=202004011125360100080681420D933E6C&offset=92&search_source=search_sug&dynamic_type=1&publish_time=0&hot_search=0
    - 关键词很重要

- mitmproxy 编写插件
    - 启动 mitmweb -s addon1.py
    - 过滤 ~u aweme\/v1\/general\/search\/single
    - [使用 mitmproxy + python 做拦截代理](https://www.cnblogs.com/grandlulu/p/9525417.html)
    - 代码例子 https://github.com/mitmproxy/mitmproxy/tree/master/mitmproxy/addons
    - https://docs.mitmproxy.org/stable/addons-overview/


- 破解 抖音 协议 接口
    - GitHub
    - 以后再研究
    - 不知道行不行 [抖音协议中的加解密算法实现](https://github.com/usualwyy/aweme-algorithm)

- 参考
    - [Android逆向之旅—Android中分析某音短视频的数据请求加密协议(IDA动态调试SO)第一篇](http://www.520monkey.com/archives/1066)
    


- 问题
    - 难度大，
    - 经常改变，不稳定
    - 使用别人破解的接口，要收费   
    - 现在抖音升级特别频繁，老版本的限制越来越多，以前的签名算法，要么已经过期，要么就不返回数据，要么就是经常封 IP，造成接口和代码要经常改动，维护代理 IP 的成本也高 
    - 视频要马上下载，不然过期失效

- 替代方案
    - 笨方法 auto.js 自动点击，输入关键词，搜索
        - 关键词很重要
        - 旅游，景点 热门
        - 网红



