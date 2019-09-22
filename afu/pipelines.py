# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
class AfuPipeline(object):
    def process_item(self, item, spider):
        return item



class AFuImgPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:

            yield scrapy.Request(image_url, meta={'item':item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        name = item['name']
        name_strip = name.strip()
        image_guid = request.url.split('/')[-1]
        filename = f'{name_strip}/{image_guid}'
        return filename

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok,x in results if ok]
        if not image_path:
            raise DropItem('---------无图片--------')
        return item



