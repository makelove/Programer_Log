
## 把repo仓库的Markdown转成HTML

- 视频 ?
    - 上个视频 [【编程】Github API 的使用-PyGithub](https://www.bilibili.com/video/BV1fh411Z777/)
    
- markdown
    - 不错 https://www.devdungeon.com/content/convert-markdown-html-python
    - [Python下将Markdown转为HTML](https://www.jianshu.com/p/0eff6cba1b7f)
    - [Python Markdown Extensions](https://www.dj-bauer.de/python-markdown-extensions-en.html)
    
```
import markdown

markdown.markdownFromFile(
    input='input.md',
    output='output.html',
    encoding='utf8',
)
```    