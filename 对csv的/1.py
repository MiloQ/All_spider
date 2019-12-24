import csv
#写csv文件
with open('data.csv','w') as csvfile:
    writer= csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerow(['100','mike','23'])
    writer.writerow(['1','lucy','24'])
    writer.writerow(['2','ds','24'])
    writer.writerows(['1','d','12'],['12','dsa','23'])
with open('data2.csv','w',encoding='utf-8') as csvfile2:
    fieldnames=['id','name','age']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()#写入头信息
    writer.writerow({'id':'12','name':'mike','age':20})
