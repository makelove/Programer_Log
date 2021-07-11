
## Flask-Pydantic Flask使用Pydantic

- 视频 [【编程】Flask使用Pydantic进行数据校验，Python fastapi](https://www.bilibili.com/video/bv16f4y1L7Rm)

- 安装
    - https://pypi.org/project/Flask-Pydantic/
    - pip install Flask-Pydantic
    - 源代码 https://github.com/bauerji/flask_pydantic

- 参考
    - [如何评价最近爆红的FastAPI？](https://www.zhihu.com/question/424133076)
    - [请不要把 Flask 和 FastAPI 放到一起比较](https://zhuanlan.zhihu.com/p/369591096)
        - [用它5分钟以后，我放弃用了四年的 Flask](https://juejin.cn/post/6844904051327369224)

- 注意
    - @validate() 接口参数字段，必须是body，或 query
    - 否则报错