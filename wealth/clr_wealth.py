# 200627 add crawler_wealth, read_csv, write_csv, main

from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

# wealth爬蟲 回傳內文
def crawler_wealth(wealth_url):
    
    url = wealth_url
    html = requests.get(url)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'html.parser')
    #data = soup.find_all('p', {'cms-style':'font-L'}, string=True)
    #data = soup.find('div', {'itemprop':'articleBody'}).find_all('p', string=True)
    data = soup.find('div', {'itemprop':'articleBody'})
    #print(data)
    if soup.find('div', {'itemprop':'articleBody'}) == None:
        print('抓不到')
        return '沒有內文'
    else:
        data = soup.find('div', {'itemprop':'articleBody'}).find_all('p', string=True)

    if data == None:
        print('抓不到')
        return '沒有內文'
    
    content = []
    for d in data:
        content.append(d.string.strip().replace('\n', '').replace(' ', ''))
    content = ''.join(content)
    # print(content)
    return content   

#crawler_wealth('https://www.wealth.com.tw/home/articles/22906')

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

    with open('clr_wealth.csv', 'w', encoding = 'utf-8') as f:
        for c in clr:
            f.write(c[0] + ',' + c[1] + '\n')



def main():

    clr = []
    filename = 'wealth.csv'
    file = read_csv(filename)
    for f in file:
        content = crawler_wealth(f[1])
        clr.append([f[0], f[1], content])
        print(f[0], ' 成功')
    #write_csv(clr)
    df = pd.DataFrame(clr, columns=['id', 'url', 'hyperlink'])
    df.to_csv('clr_wealth.csv', encoding='utf-8', index=False)
    print('clr_wealth.csv')

main()
    

