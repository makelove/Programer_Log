/*
@File    :   t1.go
@Time    :   2020/02/18 17:36:24
@Author  :   play4fun
@Desc    :   d
*/

package main

import "fmt"

func main() {
	numbers := [6]int{1, 2, 3, 5}
	for i, x := range numbers {
		fmt.Printf("第 %d 位 x 的值 = %d\n", i, x)
	}
}
