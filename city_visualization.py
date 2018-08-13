#统计微信好友来自哪里,先定义一个函数把数据都爬下来，存到DataFrame里，再进行分析

from pandas import DataFrame

#定义一个函数，用来爬取各个变量
def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable

#调用函数得到各变量
NickName = get_var("NickName")
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Signature = get_var('Signature')


data = {'NickName': NickName, 'Sex': Sex, 'Province': Province,
        'City': City, 'Signature': Signature}
#转化成df
frame = DataFrame(data)

city_name = []
for i in list(frame['City']):
    j = '%s%s' % (i, '市')
    city_name.append(j)

import numpy as np

City_name = ['朝阳市', '潮州市', '东莞市', '佛山市', '广州市', '河源市',
             '惠州市', '汕头市', '江门市', '揭阳市', '茂名市', '梅州市',
             '清远市', '汕尾市', '韶关市', '深圳市', '肇庆市',
             '湛江市', '云浮市', '中山市', '珠海市', "阳江市"]

num = []
for i in City_name:
    num.append(city_name.count(i))

#对结果进行可视化
cc = Map('树根的微信好友分布（仅广东）',width=1200,height=600)
cc.add('',City_name,num,maptype='广东',is_visualmap=True,visual_range=[0, 150],visual_text_color='#000')
cc.render()
