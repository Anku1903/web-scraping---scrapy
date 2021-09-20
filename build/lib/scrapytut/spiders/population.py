import scrapy


class PopulationSpider(scrapy.Spider):
    name = 'population'
    allowed_domains = ['worldometers.info/world-population/population-by-country/']
    start_urls = ['http://worldometers.info/world-population/population-by-country//']

    def parse(self, response):
        countries = response.xpath("//tbody/*/td[2]/a/text()").extract()
        yield {"All countries": countries,"Total": len(countries)}
