# 200627 add crawler_sina, read_csv, write_csv, main

from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

# sina爬蟲 回傳內文
def crawler_sina(sina_url):
    
    url = sina_url
    html = requests.get(url)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'html.parser')
    #data = soup.find_all('p', {'cms-style':'font-L'}, string=True)
    #data = soup.find('div', {'id':'news-main-body'}).find_all('p', string=True)
    data = soup.find('div', {'id':'news-main-body'})
    #print(soup.find('div', {'id':'news-main-body'}))
    if soup.find('div', {'id':'news-main-body'}) == None:
        print('抓不到')
        return '沒有內文'
    else:
        data = soup.find('div', {'id':'news-main-body'}).find_all('p', string=True)
    
    if data == None:
        print('抓不到')
        return '沒有內文'
        
    content = []
    for d in data:
        content.append(d.string.strip().replace('\n', '').replace(' ', ''))
    content = ''.join(content)
    #print(content)
    return content   

#crawler_sina('https://sina.com.hk/news/article/20190930/1/27/2/%E7%BE%8E%E6%BF%AB%E7%94%A8%E8%A3%BD%E8%A3%81%E5%A4%A7%E6%A3%92-%E4%BF%84%E5%B8%8C%E6%9C%9B%E8%81%AF%E5%90%88%E5%9C%8B%E7%B8%BD%E9%83%A8%E6%90%AC%E9%9B%A2%E7%BE%8E%E5%9C%8B-10673226.html')

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

    with open('clr_sina.csv', 'w', encoding = 'utf-8') as f:
        for c in clr:
            f.write(c[0] + ',' + c[1] + '\n')



def main():

    clr = []
    filename = 'sina.csv'
    file = read_csv(filename)
    for f in file:
        content = crawler_sina(f[1])
        clr.append([f[0], f[1], content])
        print(f[0], ' 成功')
    #write_csv(clr)
    df = pd.DataFrame(clr, columns=['id', 'url', 'hyperlink'])
    df.to_csv('clr_sina.csv', encoding='utf-8', index=False)
    print('clr_sina.csv')

main()
    

