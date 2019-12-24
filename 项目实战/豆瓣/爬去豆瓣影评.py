from bs4 import BeautifulSoup
import requests

s = requests.Session()#生成Session 对象 保存cookie
def  login_douban():

    login_url = 'https://accounts.douban.com/j/mobile/login/basic'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Referer':'https://accounts.douban.com/passport/login'
    }
    data = {
        'name':'15056944199',
        'password':'qzy8910234',
        'remember':'false'
    }#用户名和密码
    try:
        r = s.post(login_url,headers=headers,data=data)#每次请求都会带上cookie
    except:
        print("爬失败")

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
    }
    try:
        r = s.get(url,headers=headers)
        r.raise_for_status()
        return r.text
    except:
        print('error')
def parse_html(html):
    soup = BeautifulSoup(html,'lxml')
    divs = soup.find_all(class_='main review-item')
    for div in divs:
        id = div['id']
        url = 'https://book.douban.com/j/review/'+id+'/full'
        r = requests.get(url)
        if r.status_code == 200:
            dict = r.json()
            h = dict['html']
            soup2 = BeautifulSoup(h,'lxml')
            text = soup2.text
            yield text



def write_to_txt(text):
    with open('九州缥缈录.txt','a',encoding='utf-8') as f :
        f.write(text+'\n\n')


def main():
    jiuzhou_url = 'https://book.douban.com/subject/1321017/reviews'
    login_douban()
    html = get_html(jiuzhou_url)
    for text in parse_html(html):
        write_to_txt(text)

if __name__ == '__main__':
    main()









