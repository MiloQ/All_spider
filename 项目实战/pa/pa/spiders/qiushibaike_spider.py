import scrapy
from ..items import  QiushibaikeItem
class QiushiSpider(scrapy.Spider):
    name = 'qiushibaike'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
    }


    def start_requests(self):
        urls = [
            'https://www.qiushibaike.com/text/page/1/',
            'https://www.qiushibaike.com/text/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,headers=self.headers)

    def parse(self,response):
        page = response.url.split('/')[-2]
        filename = 'qiusi-%s.html' %page
        with open(filename,'a',encoding='utf-8') as f:
            f.write(response.text)
        self.log('Saved file %s'%filename)
        all = response.xpath("//div[@id='content-left']")
        divs = all.xpath("./div") #每个div包含一个快
        for div in divs:
            item = QiushibaikeItem()
            item['text'] = div.xpath(".//span/text()").extract_first('')
            item['author'] = div.xpath(".//h2/text()").extract_first('')
            item['smile_number'] = div.xpath(".//span[@class='stats-vote']/i/text()").extract_first('')
            item['comments_number'] = div.xpath(".//span[@class='stats-comments']//i/text()").extract_first('')
            yield item
        next_page = response.xpath("//span[@class='next']/../@href").extract_first('')
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield  scrapy.Request(next_page,callback=self.parse)