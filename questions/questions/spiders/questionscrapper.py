# -*- coding: utf-8 -*-
import scrapy


class QuestionscrapperSpider(scrapy.Spider):
    name = 'questionscrapper'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['https://stackoverflow.com/questions/tagged/python?page=1&sort=newest&pagesize=50',
    'https://stackoverflow.com/questions/tagged/python?page=2&sort=newest&pagesize=50',
    'https://stackoverflow.com/questions/tagged/python?page=3&sort=newest&pagesize=50'
   ]

    def parse(self, response):
    	questions=response.css('div.summary')
        for quesion in questions:
            yield {
                'question': quesion.css('h3 a.question-hyperlink::text').extract_first(),
                'link':'https://stackoverflow.com'+str(quesion.css('h3 a.question-hyperlink::attr(href)').extract_first())
                
            }
