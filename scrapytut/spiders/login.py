import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/login']

    def parse(self, response):
        csrf_token = response.xpath("//*[@name='csrf_token']/@value").extract_first()
        yield FormRequest("https://quotes.toscrape.com/login",formdata={'csrf_token':csrf_token,"username":"ankur","password":"fooobar"},callback=self.parse_after)
    
    def parse_after(self, response):
        if response.xpath("//a[text()='logout']"):
            self.log("you are logged in")
        open_in_browser(response)    
