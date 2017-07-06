# -*- coding: utf-8 -*-
import scrapy


class FilmscrapSpider(scrapy.Spider):
    name = 'filmscrap'
    allowed_domains = ['imdb.com']
    start_urls = ['http://www.imdb.com/chart/top']

    def parse(self, response):
    	films=response.css('tr')[1:-2]
    	average=[]
        for film in films:
            yield {
               'Year':film.css('td.titleColumn span::text').extract_first(),
               'URL':'http://imdb.com'+str(film.css('td.titleColumn a::attr(href)').extract_first()),
               'Rating':film.css('td strong::text').extract_first(),
               'Rank': film.css('td.titleColumn::text').re('[0-9]+')[0],
               'Title': film.css('td.titleColumn a::text').extract_first(),
                }

        for f in films:
        	Rating=f.css('td strong::text').extract_first()
        av=float(Rating)
        average.append(av)
        avg=sum(average)/len(average)
    	yield{
    	"Average":avg
    	}
    	