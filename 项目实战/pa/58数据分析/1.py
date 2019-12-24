from pyecharts.charts import Pie,Bar
from pyecharts import options as opts
import pymysql


conn = pymysql.connect(user='root',password='qzy201818',
                             host='127.0.0.1',db='home',port=3306)
cursor = conn.cursor()
def get_num(name,start,end):
    sql = "select COUNT("+name+") from 郑州二手房信息 where "+name+" > "+start+" and "+name+" <= "+end
    cursor.execute(sql)
    return cursor.fetchone()[0]
fiv = get_num('all_price','1','50')
hun = get_num('all_price','50','100')
hun2 = get_num('all_price','100','200')
hun35 = get_num('all_price','200','500')
hun51 = get_num('all_price','500','1000')
hun10 = get_num('all_price','1000','3000')
name = ['50w以下','50w-100w','100w-200w','200w-500w','500w-1000w','>1000w']
value = [fiv,hun,hun2,hun35,hun51,hun10]

bar = Bar()
bar.add_xaxis(name)
bar.add_yaxis('58',value)
bar.set_global_opts(title_opts=opts.TitleOpts(title='郑州',subtitle='二手房信息'))
bar.render()
a  = list(zip(name,value))
pie = Pie()

pie.add('',a)
pie.set_global_opts(title_opts=opts.TitleOpts(title='郑州二手房信息'))
pie.render('pie.html')
