/*
@File    :   a.go
@Time    :   2020/02/24 11:42:20
@Author  :   play4fun
@Desc    :   d
*/

package main

import (
	"a/dir1"
	"a/dir1/dir11"
	"fmt"
)

func main() {
	//使用a2.go的变量，直接调用
	fmt.Println("a2.go abc2:", abc2)
	// 使用dir1/b.go的变量
	// - import "a/dir1"
	fmt.Println("dir1/b.go bbb1:", dir1.Bbb1)
	fmt.Println("a/dir1/dir11/b11.go B11:", dir11.B11)
	// 使用dir1/b2.go的函数
	dir1.T1()
}
