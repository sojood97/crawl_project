# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DeviceipItem(scrapy.Item):
    # define the fields for your item here like:
    text = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    img_url = scrapy.Field()
   # pass
