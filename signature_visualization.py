1#微信工具库
import itchat
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

itchat.login() #生成二维码，扫描登录微信

#获取好友信息
friends = itchat.get_friends(update=True)[:]

#定义一个函数，用来爬取好友签名
def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable

Signature = get_var('Signature')

#正则表达式清洗文本
siglist = []

for i in Signature:
    signature_1 = i.strip().replace("span","").replace("class","").replace("emoji","")
    rep = re.compile("1f\d+\w*|[<>/=]")
    signature_1 = rep.sub("", signature_1)
    siglist.append(signature_1)

text = "".join(siglist)

#分词
import jieba

wordlist = jieba.cut(text, cut_all=True)
word_space_split = " ".join(wordlist)

coloring = np.array(Image.open(".../0101.jpg"))
my_wordcloud = WordCloud(background_color="white", max_words=2000,
                         mask=coloring, max_font_size=120, random_state=42, scale=2,
                         font_path=".../msyh.ttc").generate(word_space_split)

image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")

plt.show()
