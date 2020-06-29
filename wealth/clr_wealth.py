# 200627 add crawler_wealth, read_csv, write_csv, main

from bs4 import BeautifulSoup
import requests
import json

# wealth爬蟲 回傳內文
def crawler_wealth(wealth_url):
    
    url = wealth_url
    html = requests.get(url)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'html.parser')
    #data = soup.find_all('p', {'cms-style':'font-L'}, string=True)
    data = soup.find('div', {'itemprop':'articleBody'}).find_all('p', string=True)
    #print(data)
    if data == None:
        return '抓不到'
    #     print('抓不到')
    content = []
    for d in data:
        content.append(d.string)
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
        clr.append([f[1], content])
        print(f[0], ' 成功')
    write_csv(clr)
    print('clr_wealth.csv')

main()
    

