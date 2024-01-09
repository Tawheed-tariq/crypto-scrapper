import scrapy


class CrypspiSpider(scrapy.Spider):
    name = "crypSpi"
    allowed_domains = ["coinmarketcap.com"]
    start_urls = ["https://coinmarketcap.com/"]

    def parse(self, response):
        pass
# https://github.com/scrapy-plugins/scrapy-playwright/tree/main