import requests,json
from bs4 import BeautifulSoup
import pandas as pd
import csv

is_write_head = False
def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html):
    soup = BeautifulSoup(html,'lxml')
    all_movies = soup.find_all(name='dd')
    for movie in all_movies:
        name = movie.find(class_ = 'name').string
        index = movie.find(class_='board-index').string
        score =str(movie.find(class_='integer').string)+str(movie.find(class_='fraction').string)
        yield {
            'name':name,
            'index':index,
            'score':score,
        }

def write_to_json(content):
    with open('猫眼电影.txt','a',encoding='utf-8') as f :
        f.write(json.dumps(content,ensure_ascii=False,)+'\n')

def write_to_csv(content,):
    with open('猫眼电影.csv','a',encoding='utf-8',) as f:
        fieldnames = ['name','index','score']
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        global is_write_head
        if is_write_head == False:
            writer.writeheader()
        is_write_head = True
        writer.writerow({'name':content['name'],'index':content['index'],'score':content['score']})


def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)

    for item in parse_one_page(html):
        # write_to_json(item)

        write_to_csv(item)

if __name__ =='__main__':
    for i in range(10):
            main(offset=i*10)


