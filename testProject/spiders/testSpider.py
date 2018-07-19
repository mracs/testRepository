import scrapy
import base64


class testSpider(scrapy.Spider):
    name = "test"
    start_urls = [
        'http://proxydb.net/',
    ]

    def parse(self, response):
        for quote in response.css("td script::text"):
            m = quote.re_first("([\d.]+)\'.split.+reverse")[::-1]
            pp = quote.re_first("atob\(\'(.*)\'").encode().decode("unicode-escape")
            pp = base64.b64decode(pp).decode('utf-8')

            # get port value
            attr = quote.re_first("data-.{5}")
            yy = int(response.css('div::attr(' + attr + ')').extract_first())
            num = int(quote.re_first("\(\d{1,6}")[1:])

            # save
            yield {
                'ip_address': m + pp,
                'port': num + yy,
            }
