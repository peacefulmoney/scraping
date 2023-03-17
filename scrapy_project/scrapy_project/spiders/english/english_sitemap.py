import scrapy


class EnglishSitemapSpider(scrapy.Spider):
    name = "english-sitemap"
    allowed_domains = ["www.oed.com"]
    start_urls = ["http://www.oed.com/sitemap.xml"]

    def parse(self, response):
        pass
