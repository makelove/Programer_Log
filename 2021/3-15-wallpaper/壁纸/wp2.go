// 数种动漫和风景壁纸随机API，你值得拥有！
// https://cloud.tencent.com/developer/article/1617028

package main

import (
	"fmt"
	"log"

	"github.com/levigross/grequests"
	"github.com/reujab/wallpaper"
)

func getWp() string { //获取壁纸图片地址
	ro := &grequests.RequestOptions{
		// Params: map[string]string{"Hello": "Goodbye"},
		RedirectLimit:      -1,
		InsecureSkipVerify: true,
	}
	resp, err := grequests.Get("https://api.ixiaowai.cn/gqapi/gqapi.php", ro)
	if err != nil {
		log.Fatalln("Unable to make request: ", err)
	}
	url := resp.Header["Location"][0]
	return url
}

func main() {

	background, err := wallpaper.Get()

	if err != nil {
		panic(err)
	}

	fmt.Println("当前Current wallpaper:", background)
	url := getWp()
	fmt.Println("墙纸:", url)
	wallpaper.SetFromURL(url) //OK
	fmt.Println("设置完毕")
}
