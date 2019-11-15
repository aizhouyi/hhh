import scrapy


class QuotesSpider(scrapy.Spider):

    name = "quotes"

    def start_requests(self):
        urls = ['https://tieba.baidu.com/p/4723392743?pn=1',
                'https://tieba.baidu.com/p/4723392743?pn=2']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"})

    def parse(self, response):
        page = response.url[-1]
        file_name = 'quotes-%s.html' % page
        with open(file_name, "wb") as f:
            f.write(response.body)
        self.log("Saved file %s" % file_name)
