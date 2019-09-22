# -*- coding: utf-8 -*-
from urllib import request

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from afu.items import AfuItem

class ImgSpider(CrawlSpider):
    name = 'img'
    allowed_domains = ['69amd.com']
    start_urls = ['https://www.69amd.com/meinv/list-兔宝宝.html']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.69amd.com/meinv/list-兔宝宝.+'), follow=True),
        Rule(LinkExtractor(allow=r'https://www.69amd.com/meinv/\d.+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        name = response.xpath('//span[@class="cat_pos_l"]/a[4]/text()').get()
        image_urls = response.xpath('//img[starts-with(@class,"videopic")]/@data-original').getall()
        item = AfuItem(name=name, image_urls=image_urls)
        yield item

