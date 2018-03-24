import requests
from bs4 import BeautifulSoup
import urllib.request

url = 'http://desk.zol.com.cn/dongman/1366x768/hot_3.html'
# for i in range(3):
print(url)
req = requests.get(url)
html = req.text
print(req.encoding)
soup = BeautifulSoup(html, 'lxml')#,from_encoding='utf-8'
result = soup.find_all('a', class_='pic')
print(result)
for r in result:
    img = r.find('img')
    print(img.get('href'))




    # for link in result:
    #     link = link.get('href')
    #     print('downloading', link)
    #     filename = link.split('/')[-1]
    #
    #     try:
    #         urllib.request.urlretrieve('http:' + link, 'pics/' + filename)
    #     except urllib.error.URLError as e:
    #         print(e)
    #         print(filename, 'failed')
    #     else:
    #         print(filename, 'saved')
    #
    # current_page = soup.find_all('span', class_='active')
    # current_page = current_page[0].text
    # next_page = int(current_page.strip('[]')) - 1
    #
    # url = 'http://desk.zol.com.cn/dongman/1366x768/hot_{}.html'.format(next_page)