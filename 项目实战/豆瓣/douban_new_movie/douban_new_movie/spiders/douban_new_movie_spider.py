from scrapy.spiders import Spider
from scrapy.selector import Selector
from ..items import  DoubanNewMovieItem

class DoubanNewMovieSpider(Spider):
    name = 'douban_new_movie_spider'
    allowed_domains = ['www.movie.douban.com']
    start_url = [
        'http://movie.douban.com/chart'
    ]
    def parse(self,response):
        sel = Selector(response)
        movie_names = sel.xpath("//div[@class='pl2']/a/text()").extract()
        movie_urls = sel.xpath("//div[@class='pl2']/a/@href").extract()
        movie_stars  = sel.xpath("//span[@class='rating_nums']/text()").extract()
        item = DoubanNewMovieItem()
        item['movie_name'] = [n for n in movie_names]
        item['movie_star'] = [n for n in movie_stars]
        item['movie_url']= [n for n in movie_urls]
        yield item


