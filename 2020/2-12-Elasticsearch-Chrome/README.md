Elasticsearch也使用Java开发并使用Lucene作为其核心来实现所有索引和搜索的功能，
但是它的目的是通过简单的RESTful API来隐藏Lucene的复杂性，从而让全文搜索变得简单。
不过，Elasticsearch不仅仅是Lucene和全文搜索，我们还能这样去描述它：

分布式的实时文件存储，每个字段都被索引并可被搜索
分布式的实时分析搜索引擎
可以扩展到上百台服务器，处理PB级结构化或非结构化数据

官网 https://hub.docker.com/_/elasticsearch/?tab=description

下载
docker pull elasticsearch:6.5.0

运行 启动ES
docker run -p 9200:9200 -it --name es_6_5 elasticsearch:6.5.0
或，单节点模式
docker run -d --name es -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.3.2


进入镜像
docker exec -it es_6_5 /bin/bash

安装中文分词插件
[root@a31684a47a92 elasticsearch]# pwd
/usr/share/elasticsearch
[root@a31684a47a92 elasticsearch]# ls
LICENSE.txt  NOTICE.txt  README.textile  bin  config  data  lib  logs  modules  plugins

./bin/elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v6.5.0/elasticsearch-analysis-ik-6.5.0.zip

加入跨域配置
vi ./config/elasticsearch.yml 
```
http.cors.enabled: true
http.cors.allow-origin: "*"
```
这样 elasticsearch-head 插件才可以访问 Elasticsearch

重启
docker restart es_6_5

部署 ElasticSearch-Head
3种方式
https://hub.docker.com/r/mobz/elasticsearch-head
docker pull mobz/elasticsearch-head:5
docker run -d --name es_admin -p 9100:9100 mobz/elasticsearch-head:5
docker restart es_admin 
不好用
使用Chrome插件
https://github.com/mobz/elasticsearch-head

JS查询
CURL 
创建索引
建立索引库company，PUT和POST都可以：
curl -XPUT 'http://localhost:9200/company'
索引库名称必须要全部小写，不能以下划线开头，也不能包含逗号

创建索引，其中employee是type，1是document，-d是指定要传输的数据(遵循JSON格式)：
curl -H "Content-Type: application/json" -XPOST http://localhost:9200/company/employee/2 -d '{
"first_name" : "werl",
"last_name" : "jkd",
"age" : 45,
"about" : "君士坦丁堡亦以其宏伟建筑而闻名。著名的建筑包括圣索菲亚大教堂、君士坦丁堡大皇宫、君士坦丁堡竞技场和黄金城门，大道与广场在其间星罗棋布。在1204年和1453年两次被劫掠之前，君士坦丁堡还保存着为数众多的艺术和文学作品。在被奥斯曼帝国攻克之时，该城已经逐渐破败，但在此后得到了迅速的复兴与发展，并于17世纪中叶再次成为当时世界第一大城市。",
"interests": [ "sports", "tv" ]
}'


python api
