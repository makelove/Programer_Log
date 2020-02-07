/*
@Time    : 2020/2/6 15:17
@File    : go_spider.go

*/

package main
import (
	"github.com/gocolly/colly"
	"log"
	"fmt"
	"time"
)

func main() {
	log.Println("Start")
	start := time.Now()
	counter:=0

	c:=colly.NewCollector(
		colly.Async(true),
		)//异步
	c.AllowURLRevisit=true

	c.OnResponse(func(r *colly.Response) {
		fmt.Println("OnResponse Visited", r.Request.URL)
		fmt.Println(string(r.Body[:]))
		counter+=1
	})

	url := "http://127.0.0.1/api"
	for a := 0; a < 10000; a++ {
		//fmt.Println(a)
		c.Visit(url)
	}
	c.Wait()


	end := time.Now()
	dlt:=end.Sub(start)
	speed:=float64(counter)/dlt.Minutes()
	fmt.Println("速度:",speed," item/minute ,",counter,dlt.Minutes())
	//速度: 149258.717455393  item/minute 995 0.0066662773

}
