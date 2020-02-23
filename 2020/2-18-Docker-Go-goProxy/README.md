- 视频 https://www.bilibili.com/video/av89812800/

- 本地开发环境损坏
- 使用Docker作为Go工程的打包编译环境

打开vscode

- 启动Docker
    - docker run -it --rm -p 8080:8080  -v  /Users/play/CODE/docker_go:/code  golang

- 检测
```
go version
go version go1.13.4 linux/amd64

go build server.go
go get github.com/emicklei/go-restful
```

- build报错
```
root@b6c01e230bce:/code/spider# go build proxy_auto_drop.go
/go/src/github.com/andybalholm/cascadia/selector.go:9:2: cannot find package "golang.org/x/net/html" in any of:
    /usr/local/go/src/golang.org/x/net/html (from $GOROOT)
    /go/src/golang.org/x/net/html (from $GOPATH)
/go/src/github.com/antchfx/htmlquery/query.go:16:2: cannot find package "golang.org/x/net/html/charset" in any of:
    /usr/local/go/src/golang.org/x/net/html/charset (from $GOROOT)
    /go/src/golang.org/x/net/html/charset (from $GOPATH)
/go/src/github.com/gocolly/colly/colly.go:48:2: cannot find package "google.golang.org/appengine/urlfetch" in any of:
    /usr/local/go/src/google.golang.org/appengine/urlfetch (from $GOROOT)
    /go/src/google.golang.org/appengine/urlfetch (from $GOPATH)
```

- 不能下载 golang.org 的代码，因为被墙
```
root@b6c01e230bce:/code/spider# go get -v github.com/gocolly/colly
github.com/gocolly/colly (download)
github.com/PuerkitoBio/goquery (download)
github.com/andybalholm/cascadia (download)
package golang.org/x/net/html: unrecognized import path "golang.org/x/net/html" (https fetch: Get https://golang.org/x/net/html?go-get=1: dial tcp 216.239.37.1:443: i/o timeout)
github.com/antchfx/htmlquery (download)
github.com/antchfx/xpath (download)
github.com/golang/groupcache (download)

package golang.org/x/net/html/charset: unrecognized import path "golang.org/x/net/html/charset" (https fetch: Get https://golang.org/x/net/html/charset?go-get=1: dial tcp 216.239.37.1:443: i/o timeout)
github.com/antchfx/xmlquery (download)
github.com/gobwas/glob (download)
github.com/kennygrant/sanitize (download)
github.com/saintfish/chardet (download)
github.com/temoto/robotstxt (download)
package google.golang.org/appengine/urlfetch: unrecognized import path "google.golang.org/appengine/urlfetch" (https fetch: Get https://google.golang.org/appengine/urlfetch?go-get=1: dial tcp 216.239.37.1:443: i/o timeout)
```

- 文档说明不清楚 https://github.com/goproxy/goproxy.cn/blob/master/README.zh-CN.md
    - 参考我的帖子 https://github.com/goproxy/goproxy.cn/issues/59

- 解决
```
export GO111MODULE=on
export GOPROXY=https://goproxy.cn
```

- 然后
```
root@b6c01e230bce:/code/spider# go get -v github.com/gocolly/colly
go: finding github.com/gocolly/colly v1.2.0
go: downloading github.com/gocolly/colly v1.2.0
go: extracting github.com/gocolly/colly v1.2.0
go: finding google.golang.org/appengine v1.6.5
go: downloading google.golang.org/appengine v1.6.5
go: finding github.com/gobwas/glob v0.2.3
go: finding github.com/kennygrant/sanitize v1.2.4
go: finding github.com/saintfish/chardet latest
go: finding github.com/PuerkitoBio/goquery v1.5.1
go: downloading github.com/kennygrant/sanitize v1.2.4
go: finding golang.org/x/net latest
go: finding github.com/antchfx/xmlquery v1.2.3
go: finding github.com/temoto/robotstxt v1.1.1
go: finding github.com/antchfx/htmlquery v1.2.2
go: downloading github.com/antchfx/xmlquery v1.2.3
go: downloading github.com/temoto/robotstxt v1.1.1
go: downloading github.com/gobwas/glob v0.2.3
go: downloading golang.org/x/net v0.0.0-20200202094626-16171245cfb2
go: downloading github.com/antchfx/htmlquery v1.2.2
go: downloading github.com/PuerkitoBio/goquery v1.5.1
go: downloading github.com/saintfish/chardet v0.0.0-20120816061221-3af4cd4741ca
go: extracting github.com/kennygrant/sanitize v1.2.4
go: extracting google.golang.org/appengine v1.6.5
go: extracting github.com/antchfx/xmlquery v1.2.3
go: extracting github.com/antchfx/htmlquery v1.2.2
go: extracting github.com/temoto/robotstxt v1.1.1
go: extracting github.com/gobwas/glob v0.2.3
go: extracting golang.org/x/net v0.0.0-20200202094626-16171245cfb2
go: extracting github.com/saintfish/chardet v0.0.0-20120816061221-3af4cd4741ca
go: extracting github.com/PuerkitoBio/goquery v1.5.1
go: downloading github.com/andybalholm/cascadia v1.1.0
go: downloading golang.org/x/text v0.3.2
go: downloading github.com/golang/protobuf v1.3.1
go: extracting github.com/andybalholm/cascadia v1.1.0
go: finding github.com/antchfx/xpath v1.1.4
go: extracting github.com/golang/protobuf v1.3.1
go: finding github.com/golang/groupcache latest
go: downloading github.com/antchfx/xpath v1.1.4
go: downloading github.com/golang/groupcache v0.0.0-20200121045136-8c9f03a8e57e
go: extracting github.com/golang/groupcache v0.0.0-20200121045136-8c9f03a8e57e
go: extracting github.com/antchfx/xpath v1.1.4
go: extracting golang.org/x/text v0.3.2
go: finding github.com/andybalholm/cascadia v1.1.0
go: finding golang.org/x/text v0.3.2
go: finding github.com/golang/protobuf v1.3.1
golang.org/x/net/html/atom
golang.org/x/net/html
github.com/antchfx/xpath
github.com/golang/groupcache/lru
github.com/andybalholm/cascadia
golang.org/x/text/encoding/internal/identifier
golang.org/x/text/transform
golang.org/x/text/encoding
golang.org/x/text/encoding/internal
github.com/PuerkitoBio/goquery
golang.org/x/text/encoding/charmap
golang.org/x/text/encoding/japanese
golang.org/x/text/encoding/korean
golang.org/x/text/encoding/simplifiedchinese
golang.org/x/text/encoding/traditionalchinese
golang.org/x/text/internal/utf8internal
golang.org/x/text/runes
golang.org/x/text/internal/tag
golang.org/x/text/internal/language
golang.org/x/text/encoding/unicode
github.com/gobwas/glob/util/runes
github.com/gobwas/glob/util/strings
github.com/gobwas/glob/match
golang.org/x/text/internal/language/compact
github.com/gobwas/glob/syntax/lexer
golang.org/x/text/language
github.com/gobwas/glob/syntax/ast
github.com/gobwas/glob/compiler
github.com/gobwas/glob/syntax
github.com/gobwas/glob
github.com/gocolly/colly/debug
golang.org/x/text/encoding/htmlindex
github.com/gocolly/colly/storage
golang.org/x/net/html/charset
github.com/kennygrant/sanitize
github.com/antchfx/htmlquery
github.com/antchfx/xmlquery
github.com/saintfish/chardet
github.com/temoto/robotstxt
github.com/golang/protobuf/proto
golang.org/x/net/context
google.golang.org/appengine/internal/datastore
google.golang.org/appengine/internal/base
google.golang.org/appengine/internal/log
google.golang.org/appengine/internal/remote_api
google.golang.org/appengine/internal/urlfetch
google.golang.org/appengine/internal
google.golang.org/appengine/urlfetch
github.com/gocolly/colly


root@b6c01e230bce:/code/spider# go build proxy_auto_drop.go
go: finding golang.org/x/net latest
go: finding github.com/saintfish/chardet latest
go: finding github.com/golang/groupcache latest

root@b6c01e230bce:/code/spider# ls -l
total 14268
-rwxr-xr-x 1 root root 14605898 Feb 18 02:07 proxy_auto_drop
-rw-r--r-- 1 root root      514 Feb 18 02:01 proxy_auto_drop.go

root@b6c01e230bce:/code/spider# ./proxy_auto_drop
2020/02/18 02:07:53 OnResponse
2020/02/18 02:07:53 r.Request.ProxyURL
2020/02/18 02:07:53 OnResponse Visited https://httpbin.org/ip
2020/02/18 02:07:53 {
  "origin": "221.218.140.26"
}

------------

```