# -*- coding: utf-8 -*-
import scrapy
from ..items import keylFansItem

class KeylSpider(scrapy.Spider):
    name = 'keyl'
    allowed_domains = ['weibo.cn']
    headers={
        'Cookies':'_T_WM=53905cdcd1c05bf431e8b33d06c17576; ALF=1569055835; SUB=_2A25wWuVbDeRhGeBJ71MY9SbOyjqIHXVTpIsTrDV6PUJbkdANLXHYkW1NRl1ATWcJTYj7Rv-BrYJb4nF5X34bQN3F; SUHB=0YhRP2Fn4qjuaC; SCF=At1fB1X1tC8TMoD4WyaSt8OJ4sjgVLnuJYlhLcZt877pp1V2qsXkQu8MPhgFfdG6VgbadVK4lQGzC5VzV318q78.; SSOLoginState=1566479627'
    }

    def start_requests(self):
        urls = ['https://weibo.cn/comment/I2xeshQHb?uid=1801769410&rand=3891&p=r&display=0&retcode=6102']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse,headers=KeylSpider.headers)
    def parse(self, response):



