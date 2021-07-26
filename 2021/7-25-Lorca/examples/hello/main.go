/**
* @File    :   main.go
* @Time    :   2021/07/22 14:20:03
* @Author  :   GH
* @Desc    :  

编译windows
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build -v -o hello_win10 main.go 

*/


package main

import (
	"log"
	"net/url"

	"github.com/zserge/lorca"
)

func main() {
	// Create UI with basic HTML passed via data URI
	ui, err := lorca.New("data:text/html,"+url.PathEscape(`
	<html>
		<head><title>Hello</title></head>
		<body><h1>Hello, world!</h1></body>
	</html>
	`), "", 480, 320)
	if err != nil {
		log.Fatal(err)
	}
	defer ui.Close()

	ui.Bind("addUp", func(a, b int) int { return a + b })
	// let x=await addUp(34534342,23748374823)

	// Wait until UI window is closed
	<-ui.Done()
}
