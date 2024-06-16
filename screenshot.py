import scrapy
from scrapy_playwright.page import PageMethod


class ScreenshotSpider(scrapy.Spider):
    name = "screenshot"

    custom_settings = {
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
         },
         "DUPEFILTER_CLASS": 'scrapy.dupefilters.BaseDupeFilter'
    }

    start_urls = ["https://sales-analysis-ifeanyi-darlington.streamlit.app/"]

    def start_requests(self):
        yield (
            scrapy.Request(
            url = self.start_urls[0],
            meta = {
                "playwright": True,
                "playwright_include_page": True,
                "playwright_page_methods": [
                    PageMethod("wait_for_selector", "g.xy", timeout = 600000)
                ],

                    }
                 )
             )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        await page.screenshot(path="sales.png", full_page=True)

        await page.close()
        
193, 975.85