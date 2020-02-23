# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class ExampleSpider(scrapy.Spider):
    name = 'example'
    # allowed_domains = ['example.com']
    start_urls = ['http://192.168.0.222:8888/']

    def parse(self, response):
        for a in response.xpath('//a'):
            href=a.xpath('@href').extract_first()
            text=a.xpath('text()').extract_first().strip()

            print('网址:',href)
            print('文本:',text)
            print('-'*10)

        for src in response.xpath('//img/@src').extract():
            print('图片:', src)
        
        #TODO yield item
        #scrapy crawl example  -s CLOSESPIDER_ITEMCOUNT=100
        
        # 重复访问
        print('重复访问',response.url)
        yield Request(url=response.url, callback=self.parse,dont_filter=True)
        pass
