

## 使用【GitHub Page】制作【短链接平台】

- 视频 
    - [【编程】使用【GitHub Page】制作 【短链接服务】，免费！Python](https://www.bilibili.com/video/BV1Tf4y147HD/)
    - [【编程】GitHub Pages免费图床，淘宝客，淘口令二维码，Python](https://www.bilibili.com/video/BV1iV411v7oL/)

- 免费
- 我的网站链接
    - 重定向
        - https://dark.net.cn/sl/t1.htm
    - 二维码
        - https://dark.net.cn/qr/tk3.png

- 参考
    - [Create a new file in the repository](https://pygithub.readthedocs.io/en/latest/examples/Repository.html#create-a-new-file-in-the-repository)
    - [HTML页面跳转（重定向）的五种方法](https://blog.csdn.net/guoshenglong11/article/details/22306721)
    - [HTML 5 meta 标签](https://www.w3school.com.cn/html5/html5_meta.asp)
    - 运行代码 https://www.w3school.com.cn/tiy/t.asp?f=html_redirect

- 现有的平台
    - 都不能用了
    - 2019年的文章 [有哪些靠谱的短链接服务？主流大平台短链接优劣对比分析](https://blog.csdn.net/daiwoyigebing/article/details/103280941)
    - 唯一好用的是微博短链接t.cn
        - 之前的api都关闭了，不能使用。
        - 有人破解了，可以购买
        - 登录微博，发条微博，找出里面的短链接
            - 模拟浏览器操作
- 怎样赚钱？
    - 在跳转之前，显示淘宝广告，自己的转链
        - https://dark.net.cn/sl/redirect.htm
        
- 免费图床
    - 读入文件，然后使用repo.create_file上传
    - 淘宝客，淘口令二维码
        - 使用 [qrcode](https://github.com/lincolnloop/python-qrcode),再传到byteIO
    
```python
    with open(entry, 'rb') as input_file:
        data = input_file.read()
    if entry.endswith('.png'):
        data = base64.b64encode(data)
```