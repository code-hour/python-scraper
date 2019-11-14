import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quotes-1'

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Scrapy's default callback method
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'quotes-%s.html' % page

        with open(filename, 'wb') as f:
            f.write(response.body)
            self.log('Saved file %s' % filename)
            # response.css("title")
            # response.css("title::text").extract()
            # response.css("title::text").extract_first()
            # response.css("title::text")[0].extract()
            # response.css("title::text").get()
            # response.css("title::text").getall()
            # response.xpath("//title")
