# wechat_crawler-visualization
关于微信的工具库itchat有很多好玩的功能，比如自动回复和查看撤回消息、消息轰炸某某的微信等等。

”itchat“是由@LittleCoder开发的，当然Python关于微信的库有很多，只是”itchat“较为简单和方便。接下来的内容都是基于这个库。

第一步肯定就是工具库的安装,在这里我们主要会用到两个工具库，itchat和pyecharts。
打开cmd命令窗口，或者Anaconda Prompt，依次输入以下命令安装相关的工具库：

```python
pip install python
pip install pyecharts
```

同时，假如我们要制作词云图，比如把好友签名提取出来制作词云图，首先要安装jieba和wordcloud，同样用pip安装
```python
pip install jieba
pip install wordcloud
```

注意：代码运行开始会弹出一个二维码，需要我们扫码登录微信网页版，才能进行微信好友数据分爬取。
