import requests
from bs4 import BeautifulSoup
import os
import time
import threading

PROXY_POOL_URL = 'http://localhost:5555/random'
def get_proxy():
    """
    获取代理
    :return:
    """
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None
def download_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',

    }


    r = requests.get(url,headers = headers)
    if r.status_code  == 200:
        return r.text
    print('连接失败')
    return None

def get_img(url):
    """
    下载本页面图片
    :return:

    """
    path = os.path.abspath('.')
    dir_path=path+'/女'
    if not dir_path:
        os.mkdir(dir_path)  # 在上级目录下新建文件夹
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',

    }
    html = download_page(url)
    soup = BeautifulSoup(html,'lxml')
    divs = soup.find_all(class_='main-image')
    for div  in divs:
        img = div.find(name='img')

        de_url = img['src']
        r = requests.get(de_url,headers=headers)
        with open(path+'/女'+'/{}/{}'.format(url,de_url.split('/')[-1]),'wb') as f:
            f.write(r.content)
            time.sleep(1)








def  parse_html(html):
    soup = BeautifulSoup(html,'lxml')
    all_list = soup.find('ul',id = 'pins')
    lis = all_list.find_all(name='li')
    for li in lis:
        a = li.find(name='a')
        url = a['href']
        yield url


def main():
    url = 'https://www.mzitu.com/mm/'
    html = download_page(url)
    for url in parse_html(html):
        get_img(url)
    queue = [i for i in range(1,72)]
    threads = []
    while len(queue) > 0:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
        while len(threads) < 5 and len(queue) > 0:  # 最大线程数设置为 5
            cur_page = queue.pop(0)
            url = 'http://meizitu.com/a/more_{}.html'.format(cur_page)
            thread = threading.Thread(target=execute, args=(url,))
            thread.setDaemon(True)
            thread.start()
            print('{}正在下载{}页'.format(threading.current_thread().name, cur_page))
            threads.append(thread)





if __name__ =='__main__':
    main()