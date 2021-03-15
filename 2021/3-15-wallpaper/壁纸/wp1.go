//简单测试
package main

import (
	"fmt"

	"github.com/reujab/wallpaper"
)

func main() {
	background, err := wallpaper.Get()

	if err != nil {
		panic(err)
	}

	fmt.Println("当前Current wallpaper:", background)
//     wallpaper.SetFromFile("/Users/play/Downloads/桂林旅游GuiLin819/IMG_20200819_130920.jpg")//本地图片

	//wallpaper.SetFromURL("https://cn.bing.com/th?id=OHR.Comma_ZH-CN3584865247_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp")//网络图片 OK
	wallpaper.SetFromURL("https://api.ixiaowai.cn/gqapi/gqapi.php")//OK
	fmt.Println("设置完毕")
}