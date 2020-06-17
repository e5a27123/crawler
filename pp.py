# 爬蟲練習
# 抓取ptt 電影版網頁原始嗎

import urllib.request as req
import bs4

url = 'https://www.ptt.cc/bbs/movie/index.html'
# 建立一個request物件，附加request headers的資訊(user資訊)
request = req.Request(url, headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

#bs4  beautifle soup 4 幫忙解析html
root = bs4.BeautifulSoup(data, 'html.parser')

titles = root.find_all('div', class_ = 'title')   #find尋找 _all所有 class = 'title' 的div標簽
for title in titles:
    if title.a != None:       #如果標題包含 a標簽
        print(title.a.string)