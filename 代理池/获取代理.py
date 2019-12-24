import requests

PROXY_POOL_URL = 'http://localhost:5555/random'
def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None

# print(get_proxy())
# proxy = get_proxy()
proxy = '222.132.41.192:9999'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,

}

r = requests.get('https://www.baidu.com/',proxies=proxies)
pass
