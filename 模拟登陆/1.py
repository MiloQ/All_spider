import requests

class Login(object):
    def __init__(self):
        self.headers = {
            'Referer' : 'https://github.com/',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url ='https://github.com/session'
        self.logined_url='https://github.com/settings/prrfile'
        self.session = requests.Session() #处理cookies
