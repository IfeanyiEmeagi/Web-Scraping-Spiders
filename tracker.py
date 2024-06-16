import scrapy
import json
from datetime import date


class TrackerSpider(scrapy.Spider):
    name = "tracker"

    def __init__(self, query="python for beginners", *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        self.base_url = "https://www.amazon.com"
        self.search_url = "https://www.amazon.com/s?k={query}"

        self.query = query
        self.rank = None
        self.page_number = 1

        self.start_urls = [ self.search_url.format(
            query = query.replace(" ", "+")
            ) ]

    def parse(self, response):
        title = "Python 3.10: A Complete Guide Book To Python Programming For Beginners"
        search_results = response.css("div.s-result-item "
                                      "h2 > a > span::text").getall()

        if title in search_results:
            position = search_results.index(title) + 1
            self.rank = (self.page_number - 1) * 48 + position
        else:
            next_btn = response.css("a.s-pagination-next")

            #check if there is next_btn
            if next_btn:
                self.page_number += 1
                next_page_url = self.base_url + next_btn.attrib['href']
                yield scrapy.Request(next_page_url)
            else:
                #if the next_btn is none, indicate that the book rank is not found
                self.rank = "Not Found"
        
        #export the rank result
        self.export()

    def export(self):
        today = date.today().strftime("%d-%m-%Y")
        with open("track.json") as file:
            dt = json.load(file)
        
        if self.query in dt:
            dt[self.query][today] = self.rank
        else:
            dt[self.query] = {
                today: self.rank
            }

        with open("track.json", "w") as file:
            #dumps the data inside the file
            json.dump(dt, file)
