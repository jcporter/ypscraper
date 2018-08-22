# -*- coding: utf-8 -*-
import scrapy
import json

from ypscraper.items import YpscraperItem

# annoying error message fix
#from scrapy import optional_features
#optional_features.remove('boto')

class YellowpagesSpider(scrapy.Spider):
    name = 'yellowpages'
    allowed_domains = ['yellowpages.com']
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES' : {
            'ypscraper.middlewares.JamesBond' : 300
        },
        'ITEM_PIPELINES' : {
            'ypscraper.pipelines.YellowpagesCSV' : 300
        }
    }
    
    def __init__(self,max_listings=None,infile=None,search_term=None,
                 city=None,state=None,*args,**kwargs):
        super(YellowpagesSpider,self).__init__(*args,**kwargs)

        if max_listings is not None:
            self.MAX_LISTINGS = int(max_listings)
        else:
            self.MAX_LISTINGS = 30

        print(self.MAX_LISTINGS)
        if infile is not None:
            with open(str(infile),'r') as f:
                searches = json.loads(f.read())
            for i in range(len(searches)):
                SEARCH_TERM = searches[i]['search_term']
                CITY        = searches[i]['city']
                STATE       = searches[i]['state']
                url  = 'https://www.yellowpages.com/search?search_terms='+SEARCH_TERM
                url += '&geo_location_terms='+CITY+'%2C+'+STATE
                self.start_urls.append(url)
        elif(city is not None and state is not None and search_term is not None):
            url  = 'https://www.yellowpages.com/search?search_terms='+search_term
            url += '&geo_location_terms='+city+'%2C+'+state
            self.start_urls = [url]
        else:
            self.start_urls = None

        print("start_urls:  "+str(self.start_urls))
    def parse(self, response):

        business_name_xpath  = '//a[@class="business-name"]/span[@itemprop="name"]/text()'
        street_address_xpath = '//p[@class="adr"]/span[@itemprop="streetAddress"]/text()'
        locality_xpath       = '//p[@class="adr"]/span[@itemprop="addressLocality"]/text()'
        address_region_xpath = '//p[@class="adr"]/span[@itemprop="addressRegion"]/text()'
        postal_code_xpath    = '//p[@class="adr"]/span[@itemprop="postalCode"]/text()'
        phone_number_xpath   = '//div[@itemprop="telephone"]/text()'
        website_xpath        = '//div[@class="v-card"]//a[@class="track-visit-website"]/@href'
        listings = response.xpath('(//div[@class="result"])')
        for j in range(1,len(listings)+1):
            i = YpscraperItem()
            root_xpath          = '(//div[@class="result"])['+str(j)+']'
            try:
                i['business_name']  = response.xpath(root_xpath+business_name_xpath).extract()
            except:
                i['business_name']  = "N/A"
            try:
                i['street_address'] = response.xpath(root_xpath+street_address_xpath).extract()
            except:
                i['street_address'] = "N/A"
            try:
                i['locality']       = response.xpath(root_xpath+locality_xpath).extract()
            except:
                i['locality']       = "N/A"
            try:
                i['address_region'] = response.xpath(root_xpath+address_region_xpath).extract()
            except:
                i['address_region'] = "N/A"
            try:
                i['postal_code']    = response.xpath(root_xpath+postal_code_xpath).extract()
            except:
                i['postal_code']    = "N/A"
            try:
                i['phone_number']   = response.xpath(root_xpath+phone_number_xpath).extract()
            except:
                i['phone_number']   = "N/A"
            try:
                i['website']        = response.xpath(root_xpath+website_xpath).extract()
            except:
                i['website']        = "N/A"
                    
            # uncomment code below to activate scrapy shell
            #from scrapy.shell import inspect_response
            #inspect_response(response, self)
            yield i

        # Code to handle pagination
        next_page = response.xpath('//a[@class="next ajax-page"]/@href').extract()
        nxt_pg    = "https://yellowpages.com"+next_page[0]
        if next_page is not None:
            if (float(nxt_pg[-1:]) <= self.MAX_LISTINGS/30):
                yield scrapy.Request(nxt_pg)
