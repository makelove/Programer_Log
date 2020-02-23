/*
@File    :   js_server.go
@Time    :   2020/02/22 11:32:32
@Author  :   play4fun
@Desc    :   d
*/

package main

import (
	"fmt"
	"html/template"
	"net/http"
)

func main() {
	fmt.Println("Open http://127.0.0.1:8888/")
	tmpl := template.Must(template.ParseFiles("index.html"))

	data := struct {
		Title string
		// Items []string
	}{
		Title: "Js动态页面演示",
		// Items: []string{
		// 	"My pictures",
		// 	"My dialog",
		// },
	}

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		tmpl.Execute(w, data)
	})

	http.ListenAndServe("0.0.0.0:8888", nil)
}
