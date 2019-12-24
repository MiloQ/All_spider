# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QiushibaikeItem(scrapy.Item):
    author = scrapy.Field()
    text = scrapy.Field()
    smile_number = scrapy.Field()
    comments_number = scrapy.Field()

class HomeItem(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field()
    addr = scrapy.Field()
    size = scrapy.Field()
    all_price = scrapy.Field()
    per_price = scrapy.Field()
