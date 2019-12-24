import scrapy
from ..items import  HomeItem
import re,time

class HomeSpider(scrapy.Spider):
    name = 'home'
    allowed_domains = ['58.com']
    start_url = "https://zz.58.com/ershoufang/?PGTID=0d200001-0015-6611-f084-062f9b4a2f74&ClickID=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    def start_requests(self):
        return [scrapy.Request(self.start_url,callback=self.parse,headers=self.headers,)]

    def parse(self,response):
        blocks = response.xpath("//li[@class='sendsoj']")
        for block in blocks:
            item = HomeItem()
            item['title'] = block.xpath('.//h2/a/text()').extract_first('')
            item['addr'] = ' '.join(block.xpath(".//p[@class='baseinfo']/span/a/text()").extract())
            item['size'] = block.xpath(".//div[@class='list-info']/p")[0].xpath(".//span/text()").extract()[1]
            item['all_price'] = float(block.xpath(".//p[@class='sum']/b/text()").extract_first())
            item['per_price'] = int(re.findall(r'(.*)元.*',block.xpath(".//p[@class='unit']/text()").extract_first())[0])
            yield item
        for i in range(1,30):
            url_redirect = 'https://zz.58.com/ershoufang/pn%s/?PGTID=0d30000c-0015-6529-4f87-c2a7a14c3399&ClickID=2' %i
            time.sleep(5)
            yield scrapy.Request(url_redirect,callback=self.parse)

