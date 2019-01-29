#pywin32
#scrapy

import scrapy

class yt_url_spider(scrapy.Spider):
	name = 'yt_url'
	def __init__(self, url=None, *args, **kwargs):
		super(yt_url_spider, self).__init__(*args, **kwargs)
		url_edit = []
		url_edit.append(url)
		self.start_urls = url_edit
		#print(self.start_urls)

	def parse(self, response):
		for url in response.css("div div div div div div div div div h3 a"):
			A = url.xpath('@href').extract_first()
			print(A)
			break


#os_cmd = '''scrapy runspider yt_url_spider_v2.py -a url="%s"''' % url
