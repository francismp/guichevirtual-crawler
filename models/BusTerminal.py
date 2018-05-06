import scrapy

class BusTerminal(scrapy.Item):
    name = scrapy.Field()
    fullName = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    fullDescription = scrapy.Field()
    address = scrapy.Field()
    position = scrapy.Field()
    routes = scrapy.Field()