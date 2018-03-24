from lxml import etree
import requests

page = eval(input("请输入需要爬取的总页数："))
#print(type(page))
#page = 3
for p in range(1,page+1):
    url = "https://www.qiushibaike.com/8hr/page/{}/".format(p)
    print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
    }
    res = requests.get(url, headers = headers)
    tree = etree.HTML(res.text)
    all = tree.xpath('//div[@id="content-left"]/div')

    data = ""
    x = ""
    data += url+'\n'
    for div in all:
        author = div.xpath('.//h2/text()')
        age = div.xpath('.//div[contains(@class, "articleGender")]/text()')
        content = div.xpath('.//span/text()')
        xinbie = div.xpath('.//div[contains(@class, "articleGender")]/@class')
        funny = div.xpath('.//span[@class="stats-vote"]/i/text()')
        conment = div.xpath('.//a[@class="qiushi_comments"]/i/text()')
        if xinbie == 'articleGender manIcon':
            x ='男'
        elif xinbie =='articleGender womenIcon':
            x = '女'
        else:
            x = "性别不明"
        up = '作者：' + author[0].strip() + '\t性别：'+x+'\t年龄：' + str(age)
        middle = content[0].strip()
        bottom = '好笑数：'+ funny[0] + '\t评论数：' + conment[0]
        data+= up + '\n' + middle +'\n'+bottom+'\n'
        #print(data)
        # print('author:',author[0].strip())
        print(type(author[0].strip()))  #取到字符串就可以使用strip()
        # print('age:',age[0])
        print(type(age))
        # print(type(xinbie))
        # print(content[0].strip())
        # print(funny[0])
        # print(conment[0])
with open('xiushibaike_spider.txt', 'w', encoding="utf-8") as f:
    f.write(data)