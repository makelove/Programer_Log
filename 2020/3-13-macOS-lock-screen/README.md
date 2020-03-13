# macOS 倒计时 自动锁屏

- lockscreen.py 比较迅速，马上就锁屏
- suspend.py 会准备系统，退出当前账号


- 添加到.bash_profile ，在命令行可以使用lock 短命令 执行，不需要输入很长的py路径
```
#锁屏
alias lock='python3 /Users/play/CODE/Python_Test/macOS/lockscreen.py  '
alias suspend='python3 /Users/play/CODE/Python_Test/macOS/suspend.py  '
```

- 添加到crontab定时任务,晚上23:31定时锁屏
    - [在MAC OS X上如何启用crontab？](https://www.cnblogs.com/pcy0/p/how-to-enable-crontab-on-osx.html)
```
crontab -e
31 23 * * * /Users/play/.py3/bin/python3  /Users/play/CODE/Python_Test/macOS/lockscreen.py 0
```
- 检查
```
sudo launchctl list | grep cron
15518	0	com.vix.cron

cat /System/Library/LaunchDaemons/com.vix.cron.plist

sudo touch /etc/crontab
```

