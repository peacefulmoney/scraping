import scrapy


class EnglishWordsSpider(scrapy.Spider):
    name = "english-words"
    allowed_domains = ["www.oed.com"]
    start_urls = ["https://www.oed.com/"]

    def parse(self, response):
        pass
