#微信工具库
import itchat
#画图的库，Bar柱状图，Pie饼图，Map地图
from pyecharts import Pie,Map,Bar
from pandas import DataFrame
import numpy as np

itchat.login() #生成二维码，扫描登录微信

#我们可以给文件传输助手发一些东西，检验是否登录成功
image_1 = '.../1.jpg'
itchat.send_image(image_1,'filehelper')

#获取好友信息
friends = itchat.get_friends(update=True)[:]

#总好友数，记得减去自己
total = len(friends)-1

#爬取好友的各种信息
result=[('RemarkName','备注'),('NickName','微信昵称'),
        ('Sex','性别'),('City','城市'),('Province','省份'),
        ('UserName','用户名'),('Signature','个性签名')]

#执行以下代码print一下男女比例结果
male = female = other = 0
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other +=1

print("男性好友： %.2f%%" % (float(male)/total*100) + "\n" +
"女性好友： %.2f%%" % (float(female) / total * 100) + "\n" +
"不明性别好友： %.2f%%" % (float(other) / total * 100))

#我们把结果绘制成图表，也就是数据可视化
pie = Pie('震惊！原来树根的微信好友是这样的')
pie.add(' ',['男' ,'女','外星人'],[(float(male)/total*100),(float(female) / total * 100),(float(other) / total * 100)],
        is_label_show=True)
#执行以上代码会在默认文件路径生成名为render的html文件，打开即可得可视化结果
pie.render()

#还可以是柱状图
ar = Bar('震惊！原来xx的微信好友是这样的')
bar.add(' ',['男' ,'女','外星人'],[(float(male)/total*100),(float(female) / total * 100),(float(other) / total * 100)],
        is_label_show=True,)

bar.render()
