# -*- coding: utf-8 -*-

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"    # eşsiz bir isimde olmalı spider'ların isimleri farklı olmalı

    def start_requests(self):
        urls = [    #Burada gideceğimiz url ler var
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)