# -*- coding: utf-8 -*-

'''
scrapy crawl example -s CLOSESPIDER_ITEMCOUNT=10000

统计结果
2020-02-06 20:48:55 [scrapy.extensions.logstats] INFO: Crawled 1581 pages (at 524 pages/min), scraped 1580 items (at 524 items/min)
2020-02-06 20:49:55 [scrapy.extensions.logstats] INFO: Crawled 2104 pages (at 523 pages/min), scraped 2103 items (at 523 items/min)
'''
import scrapy
from scrapy import Request
from scrapy_demo.items import ScrapyDemoItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    # allowed_domains = ['example.com']
    url='http://127.0.0.1:8080/'
    start_urls = [url]

    def parse(self, response):
        # print(response.body)
        it=ScrapyDemoItem()
        it['json']=response.body
        yield it

        yield Request(self.url,callback=self.parse,dont_filter=True)
        pass
