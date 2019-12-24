import requests

'ds' \
''
url  = 'https://www.zhihu.com/hot'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Cookie':'__gads:ID=7b099d37a7ec5230:T=1554220109:S=ALNI_Ma6_1rT5Cp7RNDaly1I_Rs1uYUUAA\
__utma:1854390.567588624.1552216170.1566032544.1566034369.19\
__utmv:51854390.100--|2=registration_date=20181212=1^3=entry_date=20181212=1\
__utmz:51854390.1566034369.19.15.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/mi-luo-82-6/following/collections\
_xsrf:SvB4ALSDRXAaBSJiie5Q2dzDenpkO61q\
_zap:03f807d6-c677-4f50-9a70-273d38889fac\
cap_id:"NmEwNWUwZjUzZjBiNGI5OWJkM2UwNDJlZmQxM2QwMzk=|1566109950|f4bc8443d2e9a3c30702899904518611daba054c"\
capsion_ticket:"2|1:0|10:1566116706|14:capsion_ticket|44:MDNlYmVmOGE3YWUyNGE1MjlkNGMyMWViNGU4YWFiMDU=|dc717ae20e3852dbd25acfba72dc6ca40287975776d31cc587530e4b949fc8fe"\
d_c0:"ALAk1F_mGQ-PTsMWlzWOAiNMpmBAvvc6oJI=|1552216150"\
l_cap_id:"MmU5YjI3OWVmMjNhNGI2YmJmOGQyYWZjMmVjMWQyOWQ=|1566109950|c8652febe509d60abfa8e97bbfb79256cc48fca5"\
q_c1:139fff1f7c824df4af99510d7c5a31ae|1565917291000|1552216164000\
r_cap_id:"OTU2NWFjZTAxMGFhNGFiZGE0NjcyY2M1YzI2ZGIyOWY=|1566109950|1922207525bee861d4f66d49034243bc87d869ba"\
tgw_l7_route:f2979fdd289e2265b2f12e4f4a478330\
tshl:\
tst:h'\
}
r = requests.get(url=url,headers = headers)
print(r.text)

