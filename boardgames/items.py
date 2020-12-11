# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BoardgamesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    year = scrapy.Field()
    rank = scrapy.Field()
    description = scrapy.Field()
    geek_rating = scrapy.Field()
    avg_rating = scrapy.Field()
    num_rating = scrapy.Field()
    url = scrapy.Field()