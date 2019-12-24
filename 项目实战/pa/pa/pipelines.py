# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo,pymysql,re

class PaPipeline(object):
    def process_item(self, item, spider):
        return item

class QiushibaikePipeline(object):
    def __init__(self):
        self.connection = pymongo.MongoClient('localhost',27017)
        self.db = self.connection.scrapy
        self.collection = self.db.qiushibaike
    def process_item(self,item,spider):
        if not self.connection or not item:
            return
        self.collection.save(item)
    def __del__(self):
        if self.connection:
            self.connection.close()

class HomePipeline(object):
    def process_item(self,item,spider):

        conn = pymysql.connect(host='127.0.0.1',user='root',password='qzy201818',
                               db='home',charset='utf8')
        cursor = conn.cursor()
        try:
            sql = "insert into 郑州二手房信息(title,addr,size,all_price,per_price)" \
                  " values('%s','%s','%s','%s','%s')"%(item['title'],item['addr'],
                            item['size'],item['all_price'],item['per_price'])
            cursor.execute(sql)
            conn.commit()


        except Exception:
            print('有错误')

        return item



