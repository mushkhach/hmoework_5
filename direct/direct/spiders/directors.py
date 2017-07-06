# -*- coding: utf-8 -*-
import scrapy


import json
import scrapy
class DirectorsSpider(scrapy.Spider):
    name = 'directors'
    allowed_domains = ['imdb.com']
    start_urls = []
    with open ('C:\Users\Mushegh\Mushegh_Khachatryan\AUA_MSE\Data_scrapping\homework_5\imdb\ilms.json') as f: 
       	x=f.read()
    	link=json.loads(x)
    	for i in range(10):
    		start_urls.append(link[i]['URL'])

    def parse(self, response):
        yield{
        "movie": response.xpath('//*[contains(@class, "title_wrapper")]/h1/text()').extract_first(),
        "director": response.xpath('//*[contains(@class, "credit_summary_item")]/span/a/span/text()').extract_first()
        }
        