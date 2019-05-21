# -*- coding: utf-8 -*-
import scrapy
import json


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/user-agent']

    def parse(self, response):
        print('*'*80)
        user_agent = json.loads(response.text)['user-agent']
        print(user_agent)
        print('*'*80)
        yield scrapy.Request(self.start_urls[0],dont_filter=True) #start_urls[0] 再次请求上面个url，ont_filter=True 不要过滤这个重复的url
