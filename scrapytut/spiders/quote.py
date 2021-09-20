import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self,response):
        # toptags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        # h1tag = response.xpath("//h1/a/text()").extract_first()
        # yield {"H1 tag" : h1tag,"Top tags": toptags}
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            title = quote.xpath(".//*[@class='text']/text()").extract_first()
            author = quote.xpath(".//*[@itemprop='author']/text()").extract_first()
            quotetags = quote.xpath(".//*[@itemprop='keywords']/@content").extract_first()
            yield {" title ":title," author ":author," keywords ": quotetags}
        nextpage = response.xpath("//*[@class='next']/a/@href").extract_first()
        nexturl = response.urljoin(nextpage)
        yield scrapy.Request(nexturl)    
            
        


