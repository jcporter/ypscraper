import scrapy
import sys, getopt
from scrapy.crawler import CrawlerProcess
from ypscraper.spiders.yellowpages import YellowpagesSpider
from scrapy.utils.project import get_project_settings

    
process = CrawlerProcess(get_project_settings())

process.crawl('yellowpages',max_listings='100',infile='searches.json')
process.start()
