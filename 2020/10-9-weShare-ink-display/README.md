## 微雪-墨水屏-编程


- e-Paper ESP32 Driver Board
    - 微雪 4.2寸墨水屏裸屏 电子纸 显示模块 红黑白三色 兼容树莓派4

- 资料
    - https://www.waveshare.net/wiki/E-Paper_ESP32_Driver_Board
        - 根据这个指南，安装软件和驱动
        - 下载案例 E-Paper_ESP32_Driver_Board_Code
    - 外国参考 https://www.hackster.io/vitorio/e-paper-name-tag-2d22cc
- 步骤
    - Windows 7 安装 Arduino IDE
    - 在GitHub下载 [Arduino-ESP32 支持包](https://codeload.github.com/espressif/arduino-esp32/zip/master) 驱动，放在hardware文件夹，新建子文件夹
    - 使用管理员权限打开cmd

```
cd C:\Program Files (x86)\Arduino\hardware\espressif\esp32\tools
C:\Program Files (x86)\Arduino\hardware\espressif\esp32\tools>get.exe
System: Windows, Info: Windows-7-6.1.7601-SP1
Platform: i686-mingw32
Downloading xtensa-esp32-elf-win32-1.22.0-80-g6c4433a-5.2.0.zip
Done
Extracting xtensa-esp32-elf-win32-1.22.0-80-g6c4433a-5.2.0.zip
Downloading esptool-2.6.1-windows.zip
Done
Extracting esptool-2.6.1-windows.zip
Downloading mkspiffs-0.2.3-arduino-esp32-win32.zip
Done
Extracting mkspiffs-0.2.3-arduino-esp32-win32.zip
Renaming mkspiffs-0.2.3-arduino-esp32-win32/ to mkspiffs
Done
```
## WiFi案例
- 然后打开ArduinoIDE
    - 打开WiFi案例，编译，上传
    - 编译完后，马上长按boot键
    - 等上传完毕，松开
    - 打开串口后台，码率
    - 按下EN键，连接WiFi
    - 串口显示IP
    - 浏览器登录http://192.168.1.104/
    - 上传图片

- 串口输出
```
ets Jun  8 2016 00:22:57

rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
configsip: 0, SPIWP:0xee
clk_drv:0x00,q_drv:0x00,d_drv:0x00,cs0_drv:0x00,hd_drv:0x00,wp_drv:0x00
mode:DIO, clock div:1
load:0x3fff0018,len:4
load:0x3fff001c,len:1216
ho 0 tail 12 room 4
load:0x40078000,len:10864
load:0x40080400,len:6432
entry 0x400806b8


Connecting to Pro
.
WiFi connected
Server started
192.168.1.104

Ok!

```

## 蓝牙案例
- 跟WiFi案例相同，编译上传固件
    - 在案例文件夹里找到app-release.apk，上传到手机安装
    - 手机蓝牙，连接电子纸驱动板
    - 打开App，上传图片

- 微雪客服，技术支持工程师
```
EMAIL：2355742828@qq.com
电话：0755-83040712
QQ： 2355742828
```