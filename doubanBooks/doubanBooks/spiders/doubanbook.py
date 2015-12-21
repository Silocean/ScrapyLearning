# -*- coding: utf-8 -*-
import scrapy
from doubanBooks.items import DoubanbooksItem


class DoubanbookSpider(scrapy.Spider):
    name = "doubanbook"
    allowed_domains = ["douban.com"]
    start_urls = (
        'http://www.douban.com/tag/%E7%BC%96%E7%A8%8B/book',
    )

    def parse(self, response):
        for sel in response.xpath("//dl"):
            item = DoubanbooksItem()
            item["title"] = sel.xpath("dd/a/text()").extract()
            item["description"] = sel.xpath("dd/div[@class='desc']/text()").extract()
            yield item
