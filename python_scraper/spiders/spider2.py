import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quotes-2'

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/'
    ]

    # Scrapy's default callback method
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'quotes-%s.html' % page

        with open(filename, 'wb') as f:
            f.write(response.body)
            self.log('Saved file %s' % filename)
