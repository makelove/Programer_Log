/*

对比 Python 和 Go 语言的每秒请求数
https://www.oschina.net/translate/python-vs-go-requests-per-second


curl http://127.0.0.1:8080/

压力测试
ab -q -c 50 -n 1000 http://127.0.0.1:8080/
*/

package main

import (
    "encoding/json"
    "fmt"
    "github.com/emicklei/go-restful"
    "io"
    "net/http"
)



func main() {
    ws := new(restful.WebService)
    ws.Route(ws.GET("/").To(hello))
    restful.Add(ws)
    fmt.Print("Server starting on port 8080\n")
     http.ListenAndServe(":8080", nil)
}

func hello(req *restful.Request, resp *restful.Response) {
    
    b, _ := json.Marshal(article)
    io.WriteString(resp, string(b))
}

type Article struct {
    Name string
    Body string
}
var article = Article{"A Royal Baby", "A slow news week"}