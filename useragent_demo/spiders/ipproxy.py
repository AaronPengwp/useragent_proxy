# -*- coding: utf-8 -*-
import scrapy
import json


class IpproxySpider(scrapy.Spider):
    name = 'ipproxy'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        print('*'*80)
        origin = json.loads(response.text)['origin']
        print(origin)
        print('*'*80)
        yield scrapy.Request(self.start_urls[0],dont_filter=True) #start_urls[0] 再次请求上面个url，ont_filter=True 不要过滤这个重复的url
