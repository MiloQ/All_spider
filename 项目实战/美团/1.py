import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
    }
    r = requests.get(url,headers=headers)
    return r.text

url = "https://bj.meituan.com/meishi/"
html = get_html(url)
print(html)
