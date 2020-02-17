## Python的秘密

- 视频 [Python的秘密，你知道吗？Python之禅](https://www.bilibili.com/video/av89586065/)

- Python之禅 
    - import this
    - 英文
    - 中文翻译
```
Beautiful is better than ugly.
# 优美胜于丑陋（Python以编写优美的代码为目标）
Explicit is better than implicit.
# 明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似） 
Simple is better than complex.
# 简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现） 
Complex is better than complicated.
# 复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）
Flat is better than nested.
# 扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套） 
Sparse is better than dense.
# 间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题） 
Readability counts.
# 可读性很重要（优美的代码是可读的） 
Special cases aren't special enough to break the rules.
Although practicality beats purity.
# 即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上） 
Errors should never pass silently.
Unless explicitly silenced.
# 不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写except:pass风格的代码） 
In the face of ambiguity, refuse the temptation to guess.
# 当存在多种可能，不要尝试去猜测 
There should be one-- and preferably only one --obvious way to do it.
# 而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法） 
Although that way may not be obvious at first unless you're Dutch.
# 虽然这并不容易，因为你不是 Python 之父（这里的Dutch是指Guido）
Now is better than never.
Although never is often better than *right* now.
# 做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
# 如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准） 
Namespaces are one honking great idea -- let's do more of those!
# 命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）
```


- Python的好处
     - 天下武功，唯快不破
     - 代码量少
     - 生态系统完善
     - 工具库齐全


- 怎样生成随机加密串

```
import string
import random

def random_string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
```

```
from uuid import uuid4
str(uuid4())
```

- 使用secrets模块生成secure token
```
import secrets

#生成适合于重置密码和难以想象的URL的安全令牌
secrets.token_bytes()
secrets.token_hex()

#返回随机字节为nbytes的URL安全文本字符串。 文本以Base64编码，每个字节平均约为1.3个字符。 如果nbytes为None或未给出，则使用有效的默认值。
secrets.token_urlsafe()

#减少攻击风险
secrets.compare_digest("e","E")
False

tokens使用多少字节

为了抵御蛮力攻击和时序攻击，tokens需要具有足够的随机性。根据专家的说法，32字节(256位)的随机性足以抵御蛮力攻击。您应该根据您的要求选择字节大小。

使用secrets.compare_digest(a,b)减少时序攻击

为了降低时序攻击的风险，secrets模块具有compare_digest(a,b)功能。如果字符串a和b相等，则此函数返回True，否则返回False以降低计时攻击的风险。

```

- 参考
    - [Python 的加密库入门](https://zhuanlan.zhihu.com/p/65168597)
    - [HTTP对外接口API sign签名](https://www.cnblogs.com/yoyoketang/p/11742187.html)
    - [Whats the simplest and safest method to generate a API KEY and SECRET in Python](https://stackoverflow.com/questions/34897740/whats-the-simplest-and-safest-method-to-generate-a-api-key-and-secret-in-python/48426397#48426397)