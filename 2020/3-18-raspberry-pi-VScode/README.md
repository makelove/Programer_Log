# 在 树莓派 上安装VScode，穷人也能学编程

- 视频 [在【树莓派】上安装VScode，穷人也能学编程。穷孩子再也不用担心上不了网课，跟不上富孩子的脚步了](https://www.bilibili.com/video/av97641262/)

- 树莓派 价格 
    - 树莓派 zero w  ￥83
    - 树莓派 3b 支撑不了VScode，只有1G内存
    - 树莓派 4b [淘宝购买](https://s.click.taobao.com/t?e=m%3D2%26s%3D%2Be3HE%2F78gn4cQipKwQzePOeEDrYVVa64LKpWJ%2Bin0XLjf2vlNIV67vq%2F9RLX5VH%2Fu6Vvho8Zh8ClldgrEKAMDfvtTsPa%2Bvw8FDXjhIkoffd7RTQd3LKg2nJi6DFpZGNc%2Bht3wBcxEogvC12RxpmE%2F%2F781y6HNSb4geD520RSZ%2BJDRCgKBRXl5cYMXU3NNCg%2F&scm=null&pvid=null&app_pvid=59590_11.9.33.73_509_1584615707568&ptl=floorId%3A17741&originalFloorId%3A17741&app_pvid%3A59590_11.9.33.73_509_1584615707568&union_lens=lensId%3APUB%401584615694%400b1a25cd_3238_170f274a034_9239%4002704xYRf7AxsgwNklmc9WZS)
        - 2G版￥277
        - 4G版￥405

- 启动 树莓派
    - [解决VNC连接安了Ubuntu MATE系统的树莓派3b时出现灰屏的问题](https://blog.csdn.net/qq_32384313/article/details/77533012)

    - 安装 VNC
        - 使用vncpasswd修改密码 123456
        - 启动 vncserver  :1
        - 杀死 vncserver -kill :1
    - 连接 VNC
        - 安装 vnc viewer https://www.realvnc.com/en/connect/download/viewer/windows/
        
- 一行命令安装VScode
    - [如何在几分钟内在Raspberry Pi 4上安装Visual Studio Code](https://www.hanselman.com/blog/HowToInstallVisualStudioCodeOnARaspberryPi4InMinutes.aspx)
    - 官网 http://code.headmelted.com/
    - https://pimylifeup.com/raspberry-pi-visual-studio-code/
    - 命令
        - sudo -s
        - . <( wget -O - https://code.headmelted.com/installers/apt.sh )