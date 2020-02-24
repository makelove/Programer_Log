package dir1

import (
	"a/dir2"
	"fmt"
)

//T1 备注，函数名第一个字母
func T1() {
	fmt.Println("b2.go使用b.go:", int_fjdk)
	fmt.Println("dir2/d2.go ddd2:", dir2.Ddd2)
}
