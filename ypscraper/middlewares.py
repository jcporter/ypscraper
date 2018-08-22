from scrapy import signals
#from fake_useragent import UserAgent
#from user_agent import generate_user_agent
import random
import json

class JamesBond(object):
    def __init__(self):
        #with open('proxies.json','r') as f:
        #    self.proxies = json.loads(f.read())
        self.ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'#generate_user_agent()
        #print('initialized')
    def process_request(self, request, spider):
        #request.meta['proxy'] = random.choice(self.proxies)
        request.headers['User-Agent'] = self.ua#.random
        #print('processing with ip: '+request.meta['proxy'])
