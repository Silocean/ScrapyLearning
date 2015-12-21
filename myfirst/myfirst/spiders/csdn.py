# -*- coding: utf-8 -*-
import scrapy
from myfirst.items import CsdnItem

class CsdnSpider(scrapy.Spider):
    name = "csdn"
    allowed_domains = ["csdn.net"]
    start_urls = (
        'http://blog.csdn.net/tracysilocean?viewmode=list',
    )

    def parse(self, response):
        for sel in response.xpath("//h1/span"):
            item = CsdnItem()
            item["title"] = sel.xpath("a/text()").extract()
            yield item
