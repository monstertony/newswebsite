import scrapy
import csv
import re

class DetailsSpider(scrapy.Spider):
    name = "dutchnews"
    allowed_domains = ["dutchnews.nl"]
    # f = csv.writer(open("newswebsite.csv", "wb+"))
    start_urls=["http://www.dutchnews.nl/?s=house+market"]
    for n in range(2,29):
        urls="http://www.dutchnews.nl/page/%i/?s=house+market"%(n)
        start_urls.append(urls)
    def parse(self, response):
        title=response.xpath('//div[contains(@class,"small-12 large-12 columns")]/article/header/h2/a/text()').extract()
        print title
        data=response.xpath('//div[contains(@class,"small-12 large-12 columns")]/article/header/div[contains(@class,"post-meta")]/span[contains(@class,"meta")]/text()').extract()
        print data
        # for each in data:
        #     print each.replace("\t","").replace("\n","")
        link=response.xpath('//div[contains(@class,"small-12 large-12 columns")]/article/header/h2/a/@href').extract()
        print link
        f = csv.writer(open("newswebsite.csv", "ab+"))
        # features=response.xpath('//div[contains(@class,"property-features")]/div[contains(@class,"property-feature")]/text()').extract()
        # price=response.xpath('//div[contains(@class,"property-price")]/text()').extract()
        # address_street=response.xpath('//h2[contains(@class,"property-address-street")]/text()').extract()
        # address_postcode=response.xpath('//div[contains(@class,"property-address-zipcity")]/text()').extract()
        # link=response.xpath('//a[contains(@class,"property-inner")]/@href').extract()
        for a in range(0,30):
        #     b1=0+a*3
        #     b2=1+a*3
        #     b3=2+a*3
            try:
                # f.writerow([address_street[a].encode("utf-8"),address_postcode[a].encode("utf-8").replace(",",""),price[a].encode("utf-8"),features[b1].encode("utf-8"),features[b2].encode("utf-8"),features[b3].encode("utf-8"),link[a].encode("utf-8")])
                # print address_street[a],address_postcode[a].encode("utf-8").replace(",",""),price[a],features[b1],features[b2],features[b3],link[a]
                f.writerow([title[a],data[a].replace("\t","").replace("\n",""),link[a]])
                print title[a],data[a].replace("\t","").replace("\n",""),link[a]
            except:
                pass