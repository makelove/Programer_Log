## Docker黑客工具

- https://hub.docker.com/r/veerendrav2/hacker-tools
- 下载
	- docker pull veerendrav2/hacker-tools
- 启动
	- 	docker run -it --rm --net=host --privileged  veerendrav2/hacker-tools

	-  启动squid代理
	-  	docker run  -it --rm -p 3128:3128  datadog/squid
	-  docker exec -it 1bff576f3afc /bin/bash
- 测试
 	-   traceroute baidu.com
	-   ping 172.17.0.2
	-   nmap 172.17.0.2