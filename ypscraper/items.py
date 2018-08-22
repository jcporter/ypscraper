# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YpscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    src = scrapy.Field()
    business_name = scrapy.Field()
    street_address = scrapy.Field()
    locality = scrapy.Field()
    address_region = scrapy.Field()
    postal_code = scrapy.Field()
    phone_number = scrapy.Field()
    website = scrapy.Field()
    pass
