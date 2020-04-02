
# 今日头条 制作视频 收益
- 看看别人是怎样的收益

- 视频 ？

- 视频是按照播放次数计算收益的。
    - 一般来说，非粉丝观看，一万次播放是3元钱；
    - 如果是粉丝观看产生的播放，一万次是几百元不等。
    - 现在很多原创账号，一万次粉丝的播放在600元左右。

### 鼓励大家走头条号原创视频的制作路线。

```
#复制HTML
html='''html'''
import re
pa='([\d\.]+.?)次观看'
pa='([\d\.]+.?)播放'
rs=re.findall(pa,html)
rs2=[]
for num in rs:
    if num[-1]=='万':
        rs2.append(float(num[:-1])*10000)
    else:
        rs2.append(float(num))

sm=sum(rs2)
sm
sm/10000*3
sm/10000*600*13.5
```