# 200627 add crawler_sina, read_csv, write_csv, main

from bs4 import BeautifulSoup
import requests
import json

# sina爬蟲 回傳內文
def crawler_sina(sina_url):
    
    url = sina_url
    html = requests.get(url)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'html.parser')
    #data = soup.find_all('p', {'cms-style':'font-L'}, string=True)
    data = soup.find('div', {'id':'news-main-body'}).find_all('p', string=True)
    
    if data == None:
        return '抓不到'
        print('抓不到')
    content = []
    for d in data:
        content.append(d.string)
    content = ''.join(content)
    #print(content)
    return content   

#crawler_sina('https://sina.com.hk/news/article/20191205/1/27/4/Google%E5%85%A9%E5%89%B5%E8%BE%A6%E4%BA%BA%E5%BC%95%E9%80%80-%E6%88%B0%E6%99%82CEO-%E6%8E%A5%E6%A3%92%E6%8C%91%E6%88%B0%E5%A4%A7-10917926.html')

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
        clr.append([f[1], content])
        print(f[0], ' 成功')
    write_csv(clr)
    print('clr_sina.csv')

#main()
    

