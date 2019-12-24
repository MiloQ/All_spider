from bs4 import BeautifulSoup as bs
import requests

def get_html(url):
    r = requests.get(url)
    try:
        if r.status_code == 200:
            return r.text
    except:
        return None
def parse_html(html):
    soup = bs(html,'lxml')
    items = soup.select('.name')
    for item in items:
        print(item.text)



def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-'+str(page)
    html = get_html(url)
    parse_html(html)


if __name__=='__main__':
    main(1)