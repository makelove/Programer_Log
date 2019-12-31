
# 12-31-Ubuntu-docker-puppeteer-刷B站视频播放量

- 首先在Ubuntu服务器上安装docker.io
	- 参考 https://docs.docker.com/install/linux/docker-ce/ubuntu/
	- 先更新apt缓存
		- sudo apt-get update
	
	- 添加key
	- 添加repo
	- 更新apt缓存
		- sudo apt-get update
	- 安装
		- sudo apt-get install docker-ce docker-ce-cli containerd.io
	- 测试
		- sudo docker run hello-world

- 拉取镜像
	- sudo docker pull alekzonder/puppeteer
- 上传js脚本
	- docker-h5.js
- 运行测试
	- sudo docker run --shm-size 1G --name bili -v /home/play/WORK/puppeteer/docker-h5.js:/app/index.js  alekzonder/puppeteer:latest

- 服务器定时运行
	- sudo crontab -e
		- 3 */2 * * * docker start bili
		- 每隔2小时执行
