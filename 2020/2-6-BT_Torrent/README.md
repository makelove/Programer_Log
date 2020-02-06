# BT下载Torrent 
- 3种编程方式
    - Python
    - Node.js
    - Go

- 平时我们都是使用迅雷-BitTorrent下载Torrent
    - 程序员是怎样下载Torrent的？
        - 可以搭建Aria2 离线下载服务


## Python
- https://github.com/makelove/True_Artificial_Intelligence/tree/master/Python/BT_libtorrent

## Node.js
- WebTorrent (torrents on the web) 在浏览器里BT下载
    - 官网 https://webtorrent.io/
    - 在线文件传输和BT下载 https://instant.io/
    - GitHub代码 https://github.com/webtorrent/webtorrent

## Go
- https://github.com/anacrolix/torrent
    - 完整功能的BitTorrent客户端
    - 文档 https://godoc.org/github.com/anacrolix/torrent
    - 案例
        - 看cmd文件夹
    - 操作
        - 把BT种子转成磁链接
        - 通过磁链接下载文件