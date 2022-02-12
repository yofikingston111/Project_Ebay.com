# Ebay Scraper Template

"""
contoh scraper

"""

import requests
import pandas as pd
from bs4 import BeautifulSoup


url = 'https://www.ebay.com/sch/i.html?'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}



def get_total_page(keywords):
    # digunakan untuk mencari total Halaman

    params = {
        '_from ': 'R40',
        '_trksid': 'p2334524.m570.l1313',
        '_nkw': keywords,
        '_sacat': '0',
        '_pgn':1,

    }

    r = requests.get(url, params=params, headers=headers)

    soup = BeautifulSoup(r.content, 'html.parser')

    pages = []

    headers_contents = soup.find('ol', 'pagination__items').find_all('li')
    for i in headers_contents:
        pages.append(int(i.text))

    # print(headers_contents)

    total_pages = max(pages)

    print('Total halaman yang diinputkan:', total_pages)
    return total_pages
    
    

def get_all_item(keywords, pages):
    # digunakan untuk scraping data item seperti price dan item yang mau di scrape
    
    productslist = []
    params = {
        '_from ': 'R40',
        '_trksid': 'p2334524.m570.l1313',
        '_nkw': keywords,
        '_sacat': '0',
        '_pgn': pages,

    }
    r = requests.get(url, params=params, headers=headers)
    # file = open("ebay.html","w")
    # file.write(r.text)

    soup = BeautifulSoup(r.text, 'html.parser')
    productslist = []
    results = soup.find('ul', {'class': 'srp-results srp-list clearfix'})
    contents = results.find_all('li', {'class': 's-item s-item__pl-on-bottom'})
    # print(contents)
    for content in contents :
        title = content.find('h3', {'class':'s-item__title'}).text
        soldprice = content.find('div', {'class': 's-item__detail s-item__detail--primary'}).text
        link = content.find('div', {'class': 's-item__info clearfix'}).find('a')['href']
        data_dict = {
            'title': title,
            'soldprice': soldprice,
            'link':link,
        }
        productslist.append(data_dict)
    return productslist


def output(keywords, final_result):
    # digunakan untuk mencetak csv atau excelfile
    # paramater final result adalah hasil akhir  dari scraping dan paginstion
    df = pd.DataFrame(final_result)
    df.to_csv(f'{keywords}.csv', index=False)

def main(keywords):  # <-  digunakan untuk menggabungkan fungsi2 yang telah dibuat sebelumnya
    final_result = [] # <- digunakan untuk menampung semua data hasil paginasi
    
   
    
    total_pages = get_total_page(keywords) # <- total halaman yang diambil dari fungsi get total pages
    for page in range(total_pages):
        page += 1
        print(f'Scraping halaman ke: {page}')
        products = get_all_item(keywords, page)
        final_result += products

    
    # proses data disini (proses final result)

    total_data = len(final_result)
    print('Ini adalah total halaman yang sudah di scrape '.format(total_data))

    # generate csv menggunakan fungsi output (diluar looping)
    output(keywords, final_result)





if __name__=='__main__':
    keyword = 'iphone' # < bisa diganti input
    main(keyword)