#Scrap the award winning films on Oscar table in each year

from scrapy_playwright.page import PageMethod
import scrapy

class OscarSpider(scrapy.Spider):
    name="oscar"
    start_urls = ["https://www.scrapethissite.com/pages/ajax-javascript/#"]

    custom_settings = {
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
         },
         "DUPEFILTER_CLASS": 'scrapy.dupefilters.BaseDupeFilter'
    }

    def parse(self, response):
        #get all the years
        years = response.css("a.year-link::text").getall()
        url = ["https://www.scrapethissite.com/pages/ajax-javascript/#{}".format(year) for year in years]
        for pos, year in enumerate(years):
            yield scrapy.Request(
                        url=url[pos],
                        meta={
                                "playwright": True,
                                "playwright_page_methods": [
                                PageMethod("wait_for_selector", "tr.film")
                                ]
                            },
                            callback=self.parse_details,
                            cb_kwargs= { "year": year },
                            dont_filter=True    
                        )
    
    def parse_details(self, response, year):
        items = []
        for row in response.css("tr.film"):
           item =  {
                    "title": row.css("td.film-title::text").get().strip(),
                    "nominations": row.css("td.film-nominations::text").get(),
                    "awards": row.css("td.film-awards::text").get()
                }
           items.append(item)
        yield { year: items }
        
        
    

