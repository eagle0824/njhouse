# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockHouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    unifiedCoding = scrapy.Field()
    uri = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    area = scrapy.Field()
    decoration = scrapy.Field()
    floor = scrapy.Field()
    ownership = scrapy.Field()
    rangeOfUse = scrapy.Field()
    address = scrapy.Field()
    listedTime = scrapy.Field()
    listedPersion = scrapy.Field()
    listedSource = scrapy.Field()
    listedPersionPhoneNumber = scrapy.Field()

class RentHouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    unifiedCoding = scrapy.Field()
    uri = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    rentway = scrapy.Field()
    paymethod = scrapy.Field()
    area = scrapy.Field()
    decoration = scrapy.Field()
    floor = scrapy.Field()
    residentialArea = scrapy.Field()
    address = scrapy.Field()
    listedTime = scrapy.Field()
    housepacking = scrapy.Field()
    details=scrapy.Field()
    listedPersion = scrapy.Field()
    listedSource = scrapy.Field()
    listedPersionPhoneNumber = scrapy.Field()
