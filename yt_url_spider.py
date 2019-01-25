url = ['https://www.youtube.com/results?search_query=overwatch+rap+battle']
#pywin32
#scrapy

import scrapy

class yt_url_spider(scrapy.Spider):
    global url
    name = 'yt_url'
    start_urls = url
    def parse(self, response):
        for url in response.css("div div div div div div div div div h3 a"):
yield {'url_text': url.xpath('@href').extract_first()}
