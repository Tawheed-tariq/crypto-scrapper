"""
To use playwright in scrapy frist install `pip3 install scrapy-playwright`
then install playwright browser `playwright install <borwser_name>`

then paste some code to settings.py file
refer to  https://github.com/scrapy-plugins/scrapy-playwright/tree/main for more 
info or this https://www.zenrows.com/blog/scrapy-playwright#how-do-you-use-scrapy-with-playwright
"""

import scrapy
from scrapy_playwright.page import PageMethod 
from ..items import CryptoDataItem




class CrypspiSpider(scrapy.Spider):
    name = "crypSpi"
# https://coinmarketcap.com/
    def start_requests(self):
        #GET request
        yield scrapy.Request("https://www.moneycontrol.com/crypto-market/market-movers/top-cryptos/inr",
         meta={
            "playwright": True,
            "playwright_page_methods" : [
                PageMethod("wait_for_timeout", 10000)
            ]
            }
         )
# The meta={"playwright": True} argument above tells Scrapy to route the request through scrapy-playwright.


    def parse(self, response):
        items = CryptoDataItem()

        table = response.xpath("//table[@class='tableWrapper_web_tbl_indices__qR1nw sortdatatable']")
        rows = table.xpath('./tr[@class="rows_rows__56D5e"]') # extracts all the row inside the table

        for row in rows:
            cols = row.xpath('./td') # extracts all the columns present in each row
            
            name = cols[0].xpath("./div/div/div/a/text()").extract() #extracts a list which contains name and the symbol
            items['name'] = name[1]
            items['symbol'] = name[0]

            price = cols[1].xpath('./text()').extract() # extracts the price of the currency
            items['price'] = price[0]

            change = cols[2].xpath('./text()').extract()
            items['change'] = change[0]

            yield items