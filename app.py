from tkinter import Tk, ttk
from scrapy.crawler import CrawlerProcess
from tracker import TrackerSpider

root = Tk()
root.title( "Tracker" )

#create a frame to hold the components of the app
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

label = ttk.Label(frame, text="Search:")
label.grid(row=0, column=0, padx=(0, 5))

#Create entry fielf
keyword = ttk.Entry(frame)
keyword.grid(row=0, column=1)

#define the function
def run_spider():
    TrackerSpider.query = keyword.get()

    crawler = CrawlerProcess()
    crawler.crawl(TrackerSpider)
    
    crawler.start()

#creat a button to run a function (spider)
btn = ttk.Button(frame, text="Run", command=run_spider)
btn.grid(row=1, column=0, pady=10, columnspan=2)




root.mainloop()
