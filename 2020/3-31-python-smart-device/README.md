
# python编程 控制智能硬件
- 视频 ？

- 智能硬件
    - [鸿雁（HONYAR）智能wifi插座 每位独立定时开关 远程手机遥控 插排/插线板/拖线板 计量型](https://union-click.jd.com/jdc?e=&p=AyIGZRprFwcQAlYTXCVGTV8LRGtMR1dGFxBFC1pXUwkEBwpZRxgHRQcLREJEAQUcTVZUGAVJHk1cTQkTSxhBekcLVx5ZEAEaAGUcGVJrFk4jQjlMfHFsIFAPcABwHQV7VxkyEzdVGloUBhsEURJZJTISBGVNNRUDEwZWGFkTBRY3VRhSEwYXBF0YWCUCFg5RHFkUAxQBURpdJQUSDmVLB0VJSlgDGFoQCiI3Vx5ZEAEaAGUYayUyEjdWKxl7VRNUVk9SEAoSVQdMXkUAE1QASwwXBBtXBxgIHQZGUAYrWRQDFg4%3D)
        - ￥119 
        - 手机App 控制，定时。统计电量
        - 型号 IHC8342B 

- 之前尝试通过WireShark【抓包】来获取 控制接口，但是没有找到
- 突然发现 有 Python api
    - https://github.com/mjg59/python-broadlink
        - 杭州博联智能科技股份有限公司 http://www.broadlink.com.cn
    - 安装
        - git clone https://github.com/mjg59/python-broadlink.git
        - cd python-broadlink
        - virtualenv -p /usr/local/bin/python3 ~/.smart
        - source ~/.smart/bin/activate
        - pip install -r requirements.txt
        - python3 setup.py install
- 参考代码
    - [博联MP系列智能插排设备连接及控制方法，如MP1、MP2等](https://www.domoticz.cn/forum/viewtopic.php?f=33&t=22&sid=3cc9783df8f361e02b039be216c0d6ba)
        - 代码 有 bug
        - 修改后 [broadlink1.py](broadlink1.py)

- 增加 使用场景 
    - 回家
        - 加湿器
        - 热水器，洗澡
        - 电灯
    - 起床
        - 拉开窗帘
    - 睡觉
        - 定时关闭 电灯
        - 关上窗帘