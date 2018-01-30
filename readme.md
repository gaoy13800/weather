# scrapy 学习并爬取新浪天气全过程

标签（空格分隔）： python scrapy 爬虫

---

## 环境及包安装

1、 pip install scrapy #python环境默认3.6  scrapy环境1.5.0

2、因为实在windows上开发所以还需要安装pypiwin32
    > pip install pypiwin32
    > 下载exe可执行文件 http://sourceforge.net/projects/pywin32/files/ 下载并直接安装

3、scrapy genspider weather weather.sina.com.cn




## 需求分析

    1、 分析待爬取的主页内容，哪些是需要的还有哪些是不需要的。
    2、通过页面浏览看到所有的省份可以拿到，所以第一步我们需要先把所有省份的url拿到
        提取出html页面中的所有url 并跟踪这些url进行一步爬取

## 爬取结果
![Image text](test.jpg)



## 执行爬取
    在根目录直接执行 main文件即可
