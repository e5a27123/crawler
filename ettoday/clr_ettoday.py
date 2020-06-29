# 200626 add crawler_ettoday
# 200627 add read_csv, write_csv, main

from bs4 import BeautifulSoup
import requests
import json

# ettoday爬蟲 回傳內文
def crawler_ettoday(ettoday_url):
    
    url = ettoday_url
    html = requests.get(url)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'html.parser')
    
    if soup.find('script', {'type':'application/ld+json'}) == None:    # 判斷是否有內文
        return '沒有內文'
    
    js = json.loads(soup.find('script', {'type':'application/ld+json'}).string, strict=False)
    #js = json.loads(soup.select('script[type=application/ld+json]').text)
    if 'articleBody' in js:
        return js['articleBody']
    else:
        if 'description' in js:          # 若沒有 articleBody 則抓 description ，再沒有回傳
            return js['description']
        else:    
            return '沒有內文'
#print(crawler_ettoday('https://www.ettoday.net/news/20190917/1536776.htm'))

# 讀取檔案
def read_csv(filename):
    
    file = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            id, url = line.strip().split(',')
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

main()
    

