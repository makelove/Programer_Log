- 视频： 


https://blog.csdn.net/qq_35430000/article/details/79421544

4.3. background
后台（姑且这么翻译吧），是一个常驻的页面，它的生命周期是插件中所有类型页面中最长的，它随着浏览器的打开而打开，随着浏览器的关闭而关闭，所以通常把需要一直运行的、启动就运行的、全局的代码放在background里面。
background的权限非常高，几乎可以调用所有的Chrome扩展API（除了devtools），而且它可以无限制跨域，也就是可以跨域访问任何网站而无需要求对方设置CORS。

然后会生成一个.crx文件，要发布到Google应用商店的话需要先登录你的Google账号，然后花5个$注册为开发者，本人太穷，就懒得亲自验证了，有发布需求的自己去整吧。


插件要实现一些ajax请求，都得通通搬到background里实现。


- 消息传递 参考
    - [Message Passing](https://developer.chrome.com/extensions/messaging)
        - 长连接 Long-lived connections
    - chrome.runtime.sendMessage的回调函数默认是同步的，而且超时后直接执行，返回undefined，如果要异步执行，必须在处理函数中return true
        - https://blog.csdn.net/anjingshen/article/details/75579521