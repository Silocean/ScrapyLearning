# -*- coding: utf-8 -*-
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from movieSpider.items import MoviespiderItem


class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'http://movie.douban.com/top250\?start=\d+.*')),
        Rule(SgmlLinkExtractor(allow=r'http://movie.douban.com/subject/\d+'), callback="parse_item"),
    )

    def parse_item(self, response):
        item = MoviespiderItem()
        item['name'] = response.xpath('//html/body/div[3]/div[1]/h1/span[1]/text()').extract()
        item['year'] = response.xpath('//html/body/div[3]/div[1]/h1/span[2]/text()').re(r'\((\d+)\)')
        item['score'] = response.xpath('//html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/strong/text()').extract()
        item['director'] = response.xpath('//a[@rel="v:directedBy"]/text()').extract()
        item['classification'] = response.xpath('//span[@property="v:genre"]/text()').extract()
        item['actor'] = response.xpath('//a[@rel="v:starring"]/text()').extract()
        yield item
