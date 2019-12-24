import requests

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
}
url ='https://www.zhihu.com/explore'
r =requests.get(url,headers=headers)
print(r.status_code)
print(type(r.text))
print(r.json())
# with open('1.txt','w') as f:
#     f.write(r.json())