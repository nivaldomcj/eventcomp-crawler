import scrapy


class SbcEventItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    start_at = scrapy.Field()
    finish_at = scrapy.Field()
    description = scrapy.Field()
    location = scrapy.Field()
