################################################################################################
######### Extract links to web pages containing information about musicians spe-  ##############
#########               cialising in music genre beginning with "A".              ##############
################################################################################################
import scrapy

class ASpider(scrapy.Spider):
    name = 'link_lists'
    start_urls = ['https://en.wikipedia.org/wiki/Lists_of_musicians']

    def parse(self, response):
        base_url = 'https://en.wikipedia.org'

        musicians = response.xpath("//div[@class='div-col'][l]/ul/li")

        for music in musicians:
            yield {
                'title': music.css('li a::text').get(),
                'url': base_url+""+music.css('li a::attr(href)').get(),
            }


# # -*- coding: utf-8 -*-
# import scrapy

# class mySpider(scrapy.Spider):
#     nape = 'spider'
#     allowed_domains = ['en.wikipedia.org/wiki/Lists_of_musicians']
#     start_urls = ['https://en.wikipedia.org/wiki/Lists_of_musicians//']
    
#     def parse(self, response):
#         base_url = 'https://en.wikipedia.org'

#         musicians = response.xpath("//div[@class='div-col'][l]/ul/li")

#         for music in musicians:
#             yield {
#                 'title': music.css('li a::text').get(),
#                 'url': base_url+""+music.css('li a::attr(href)').get(),
#             }