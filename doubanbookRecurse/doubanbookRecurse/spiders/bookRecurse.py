# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from doubanbookRecurse.items import DoubanbookrecurseItem


class BookrecurseSpider(CrawlSpider):
    name = 'bookRecurse'
    allowed_domains = ['douban.com']
    start_urls = ['http://www.douban.com/tag/%E7%BC%96%E7%A8%8B/book']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'http://www.douban.com/tag/%E7%BC%96%E7%A8%8B/book\?start=\d+.*'),
             callback='parse_item'),
    )

    def parse_item(self, response):
        for sel in response.xpath("//dl"):
            item = DoubanbookrecurseItem()
            item["title"] = sel.xpath("dd/a/text()").extract()
            item["description"] = sel.xpath("dd/div[@class='desc']/text()").extract()
            yield item
