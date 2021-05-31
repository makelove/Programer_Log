
# 在命令行使用REPL执行puppeteer爬虫和抓包

- 视频 B站 [【编程】在命令行使用REPL执行Puppeteer爬虫和抓包，调试代码](https://www.bilibili.com/video/BV1Nq4y1j71W/)
## 什么是REPL ?
- Python
    - [为什么解释器的交互模式又叫 REPL](https://zhuanlan.zhihu.com/p/107266796)
    - Read Eval Print Loop
        - Read，读取用户输入
        - Eval， 执行输入内容
        - Print，打印输出结果
        - Loop， 不断循环以上步骤

- Node.js

## puppeteer 和 REPL
- 参考
    - [puppeteer 调试工具——puppeteer-debug](https://zhuanlan.zhihu.com/p/34970878)
        - 不好用，没有更新？
        - 最近研究了下用 puppeteer 写爬虫，很好很强大。唯一不太满意的地方就是调试起来有点麻（dan）烦（teng），每调试一步都要重启
    - [puppeteer-extra-plugin-repl](https://www.npmjs.com/package/puppeteer-extra-plugin-repl?activeTab=readme)
        - 好用
        - npm i -g puppeteer-extra-plugin-repl
    - [Feature request: REPL in puppeteer](https://github.com/puppeteer/puppeteer/issues/3391)
        - 最好用
        - 请看 DEMO.JS