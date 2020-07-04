# 200628 add crawler_tvbs, read_csv, write_csv, main

from bs4 import BeautifulSoup
import requests
import json
import time

# tvbs爬蟲 回傳內文
def crawler_tvbs(tvbs_url):
    
    url = tvbs_url
    html = requests.get(url, headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    })
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'html.parser')
    soup.prettify()
    
    #data = soup.find_all('div', id='table01')
    data = soup.find('div', {'class':'h7 margin_b20'}).find_all('body')      #.find_all('table', {'class':'noBorder'})
    if data == None:
    #    return '抓不到'
        print('抓不到')
    #print(data)
    
    for d in data:
        print(d.text)

    # content = []
    # for d in data:
    #     # if d.find('table', {'class':'noBorder'}) == None:
    #     #     print('抓不到')

    #     note = d.find('td', {'class':'note'})
    #     if note != None:
    #         d.find('td', {'class':'note'}).clear()
    #     #print(d)
    #     content.append(d.get_text().replace('\n', '').replace('\u3000', '').replace('\xa0', '').replace('\r', ''))
        
    # content = ''.join(content)
    # print(content)
    # #time.sleep(2)
    # return content   


crawler_tvbs('https://news.tvbs.com.tw/politics/1165023')
#crawler_tvbs('https://tvbs.twse.com.tw/tvbs/web/t05st02?step=1&off=1&firstin=1&TYPEK=otc&i=84&h840=%AD%CA%B1%6A%AA%D1%A5%F7&h841=3219&h842=20191230&h843=161024&h844=%A4%BD%A7%69%A5%BB%A4%BD%A5%71%B0%5D%B0%C8%A5%44%BA%DE%A1%42%B7%7C%AD%70%A5%44%BA%DE%A1%42%B5%6F%A8%A5%A4%48%A4%CE%A5%4E%B2%7A%B5%6F%A8%A5%A4%48%B2%A7%B0%CA&h845=6&pgname=t05st02')
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

    with open('clr_tvbs.csv', 'w', encoding = 'utf-8') as f:
        for c in clr:
            f.write(c[0] + ',' + c[1] + '\n')



def main():

    clr = []
    filename = 'tvbs.csv'
    file = read_csv(filename)
    
    for f in file:
        content = crawler_tvbs(f[1])
        clr.append([f[1], content])
        print(f[0], ' 成功')
        time.sleep(5)
    write_csv(clr)
    print('clr_tvbs.csv')

#main()
    

