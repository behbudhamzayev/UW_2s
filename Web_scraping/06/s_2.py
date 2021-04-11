#Extract links to artists’ web pages for the first of the links from the previous step.

import scrapy

class ASpider(scrapy.Spider):
    name = 'links'
    start_urls = ['https://en.wikipedia.org/wiki/Lists_of_musicians']

    def parse(self, response):
        base_url = 'https://en.wikipedia.org'

        musicians = response.xpath("//div[@class='div-col'][1]/ul/li")

        for music in musicians:
            yield {
                'url': base_url+""+music.css('li a::attr(href)').get(),
            }