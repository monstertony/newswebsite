import scrapy
import csv
import re

class DetailsSpider(scrapy.Spider):
    name = "cbsnews"
    allowed_domains = ["dutchnews.nl"]
    # f = csv.writer(open("newswebsite.csv", "wb+"))
    start_urls=["https://www.cbs.nl/en-gb/search/?query=house%20market"]
    # for n in range(2,29):
    #     urls="http://www.dutchnews.nl/page/%i/?s=house+market"%(n)
    #     start_urls.append(urls)
    def parse(self, response):
        # title=response.xpath('//div[contains(@class,"thumbnail-searchresult")]/a/div[contains(@class,"caption")]/h3/text()').extract()
        # print title
        data=response.xpath('//div[contains(@class,"thumbnail-searchresult")]/a/div[contains(@class,"caption")]/p[contains(@class,"date")]/text()').extract()
        print data
        # link=response.xpath('//div[contains(@class,"small-12 large-12 columns")]/article/header/h2/a/@href').extract()
        # print link
        # f = csv.writer(open("newswebsite.csv", "ab+"))
        # for a in range(0,30):
        #     try:
        #         f.writerow([title[a],data[a].replace("\t","").replace("\n",""),link[a]])
        #         print title[a],data[a].replace("\t","").replace("\n",""),link[a]
        #     except:
        #         pass