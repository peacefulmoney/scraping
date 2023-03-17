import scrapy


class SpanishCrawler(scrapy.Spider):
    name = "spanish-crawler"
    allowed_domains = ["www.listasdepalabras.es"]
    start_urls = ["https://www.listasdepalabras.es/todaspalabras.htm"]

    def parse(self, response):
        pass
