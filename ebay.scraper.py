import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.ebay.com/sch/i.html?'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}


def get_total_pages(keywords):
    params = {
        '_from ': 'R40', '_trksid': 'p2334524.m570.l1313',
        '_nkw': keywords,
        '_sacat': '0',
        'LH_TitleDesc': '0',
        '_odkw': keywords,
        '_osacat': '0',

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


def get_all_item(keywords, x):
    productslist = []
    params = {
        '_from ': 'R40',
        '_trksid': 'p2334524.m570.l1313',
        '_nkw': keywords,
        '_sacat': '0',

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

def output(productslist):
    productsdf = pd.DataFrame(productslist)
    productsdf.to_csv('output.csv', index=False)
# def main
def main(pages, keywords):
    params = {
        '_from ': 'R40',
        '_trksid': 'p2334524.m570.l1313',
        '_nkw': keywords,
        '_sacat': '0',
        '_pgn':pages,

    }
    for x in pages(1,5):
        print('')


if __name__ == '__main__':
    keyword = input('Masukan Kata Kunci Pencarian: ')
    result = get_all_item(keyword)
    output(result)

