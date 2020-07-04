# 200626 add crawler_ettoday
# 200627 add read_csv, write_csv, main
# 200630 去除空格

from bs4 import BeautifulSoup
import requests
import json

# ettoday爬蟲 回傳內文
def crawler_ettoday(ettoday_url):
    
    url = ettoday_url
    html = requests.get(url)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'html.parser')
    
    #if soup.find('script', {'type':'application/ld+json'}) == None:    # 判斷是否有內文
    #    return '沒有內文'
    
    # js = json.loads(soup.find('script', {'type':'application/ld+json'}).string, strict=False)
    # #js = json.loads(soup.select('script[type=application/ld+json]').text)
    # if 'articleBody' in js:
    #     #return js['articleBody']
    #     print(js['articleBody'].replace('\n', '').replace(' ', ''))   #200630
    # else:
    #     if 'description' in js:          # 若沒有 articleBody 則抓 description ，再沒有回傳
    #         #return js['description']
    #         print(js['description'].replace('\n', '').replace(' ', ''))   #200630
    #     else:    
    #         return '沒有內文'
    data = soup.find_all('div', {'itemprop':'articleBody'})
    #print(len(data))
    content = []
    for d in data:
        d.find('img').extract()
        d.find('strong').extract()
        print(d.get_text())


#crawler_ettoday('https://www.ettoday.net/news/20191008/1553091.htm')

# 讀取檔案
def read_csv(filename):
    
    file = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            name_id = []
            id, url = line.strip().split(',')
            if 'news' in url:
                name_id = url.split('/')
                name_id = name_id[-1]
                name_id = name_id[0:6]
                url = 'https://www.ettoday.net/amp/amp_news.php?news_id=' + name_id + '&from=rss'
                #print(url)
                #https://www.ettoday.net/amp/amp_news.php?news_id=1521289&from=rss 
            file.append([id, url])
    return file

#print(read_csv('test.csv'))

# 寫入csv
def write_csv(clr):

    with open('clr_ettoday.csv', 'w', encoding = 'utf-8') as f:
        for c in clr:
            f.write(c[0] + ',' + c[1] + '\n')



def main():

    clr = []
    filename = 'ettoday.csv'
    file = read_csv(filename)
    for f in file:
        content = crawler_ettoday(f[1])
        clr.append([f[1], content])
        print(f[0], ' 成功')
    write_csv(clr)
    print('clr_ettoday.csv')

#main()
    

