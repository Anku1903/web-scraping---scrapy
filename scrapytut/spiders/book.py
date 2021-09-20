import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['https://stackoverflow.com/questions?pagesize=4&sort=newest']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        
        questions = response.xpath("//div[@class='summary']/h3")
        for que in questions:
            item = {}
            item['url'] = que.xpath("a[@class='question-hyperlink']/@href").extract()[0]
            item['text'] = que.xpath("a[@class='question-hyperlink']/text()").extract()[0]
            yield item
            
        
