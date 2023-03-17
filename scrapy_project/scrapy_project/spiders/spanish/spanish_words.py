import scrapy


class SpanishWordsSpider(scrapy.Spider):
    name = "spanish-words"
    allowed_domains = ["www.listasdepalabras.es"]
    start_urls = ["https://www.listasdepalabras.es/todaspalabras.htm"]

    def parse(self, response):
        pass
