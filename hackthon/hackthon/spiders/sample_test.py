import scrapy
import pandas as pd



class QuotesSpider(scrapy.Spider):
    name = "quotes"

    

    def start_requests(self):
        df = pd.read_csv('C:\Hackathon\hackathon_input_veirdo.csv')
        urls = df['Amazon_URL'].to_list()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        mrp = response.css("div.a-section span.a-price span.a-offscreen::text").get()

