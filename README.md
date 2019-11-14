# Python Scraper

Playing around to learn scraping with python & scrapy

## Scrapy

Run the following command in current project directory to create a scraper

```bash
$ scrapy startproject <project>
$ scrapy startproject scraper
```

Getting started with a new spider

```bash
$ scrapy genspider example example.com
```

### Running the spider

```bash
$ scrapy crawl <spider_name>
$ scrapy crawl quotes-1

Write the output to a JSON file
$ scrapy crawl quotes-3 -o quotes.json

Write the output to a CSV file
$ scrapy crawl quotes-3 -o quotes.csv

Write the output to a XML file
$ scrapy crawl quotes-3 -o quotes.xml

Note: By default scrapy appends to a file rather than overwriting the content existing in it
```

### Using the shell

```bash
$ scrapy shell <url>
$ scrapy shell "http://quotes.toscrape.com/page/1/"
```
