import requests
from bs4 import BeautifulSoup
import pymysql
from 项目实战.豆瓣.常用函数.常用函数 import get_proxy
class  Douban:
    def __init__(self,base_url,):
        self.base_url = base_url
        self.s = requests.Session()
    #登陆豆瓣
    def login_douban(self):
        login_url = 'https://accounts.douban.com/j/mobile/login/basic'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
            'Referer': 'https://accounts.douban.com/passport/login'
        }
        data = {
            'name': '15056944199',
            'password': 'qzy8910234',
            'remember': 'false'
        }  # 用户名和密码
        try:
            r = self.s.post(login_url, headers=headers, data=data)  # 每次请求都会带上cookie
        except:
            print("爬失败")

    #得到该页原代码
    def get_page(self,page):
        try:
            url = self.base_url+'?start='+str(page*20)
            headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
      }
            proxy = get_proxy()
            proxies = {
                'http': 'http://' + proxy,
                'https': 'https://' + proxy,

            }
            r = self.s.get(url,headers=headers,proxies=proxies)
            if r.status_code == 200:
                return r.text
        except:
            print('error')


    def parse_page(self,html):
        soup = BeautifulSoup(html,'lxml')
        divs = soup.find_all(class_='main review-item')
        for div in divs:
            id = div['id']
            title = div.find('h2').string

            url ='https://book.douban.com/j/review/' +id+'/full'
            r = self.s.get(url)
            dict = r.json()
            ht = dict['html']
            soup2 = BeautifulSoup(ht,'lxml')
            text = soup2.text
            yield{
                'title':title,
                'text':text,
            }
    def write_to_mysql(self,dict):
        conn = pymysql.connect(host='localhost',user='root',password='qzy201818',port=3306,db='blog')
        cursor = conn.cursor()
        sql = "INSERT IN '九州'('title','text') VALUES(%s,%s)"
        try:
            cursor.execute(sql,(dict['title'],dict['text']))
            conn.commit()
        except:
            conn.rollback()
        conn.close()

    #开启爬虫
    def start(self):
        self.login_douban()
        for page in range(10):
            html = self.get_page(page)
            print('正在爬去第'+str(page)+'页评论')
            for dict in self.parse_page(html):
                self.write_to_mysql(dict)


spider = Douban('https://book.douban.com/subject/1321017/reviews')
spider.start()














