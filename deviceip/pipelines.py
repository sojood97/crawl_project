# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import json
from itemadapter import ItemAdapter

from deviceip.spiders.spiderip import SpideripSpider


class DeviceipPipeline:

    def open_spider(self , SpideripSpider):
        self.file = open('items.jl', 'w')
        
    def close_spider(self, SpideripSpider):
        self.file.close()

    def process_item(self, resulted_data, SpideripSpider):

        return resulted_data


