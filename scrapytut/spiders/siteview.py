import scrapy


class SiteviewSpider(scrapy.Spider):
    name = 'siteview'
    website = "amazon.com"
    allowed_domains = ['www.similarweb.com']
    start_urls = ['https://www.similarweb.com/website/'+website]

    def parse(self, response):
        views = response.xpath("/html/body/div[1]/main/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/span[2]/span[1]/text()").extract()
        yield {"website traffic":views}
