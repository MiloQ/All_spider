import json
#json 字符串用双引号包围  若用单引号则报错
str = '''
[{
    "name": "Bob",   
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''

data = json.loads(str)  #把字符串转化为json对象
print(data)
print(type(data))
print(data[0].get('name'))
datastr = json.dumps(data,indent=2,ensure_ascii=False)  #把json对象转化为字符串 indent 缩进更好看 ensure_ascii=False输出中文
print(datastr)
