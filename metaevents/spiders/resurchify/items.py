import scrapy


class ResurchifyEventItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    start_at = scrapy.Field()
    finish_at = scrapy.Field()
    location = scrapy.Field()
    website = scrapy.Field()
    categories = scrapy.Field()
    description = scrapy.Field()
    metadata = scrapy.Field()
