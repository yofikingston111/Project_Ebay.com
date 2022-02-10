import requests
from bs4 import BeautifulSoup

url = 'https://www.ebay.com/sch/i.html?'
headers = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}


def get_total_pages(keywords):
    params = {
        '_from ': 'R40',        '_trksid': 'p2334524.m570.l1313',
        '_nkw': keywords,
        '_sacat': '0',
        'LH_TitleDesc':'0',
        '_odkw': keywords,
        '_osacat':'0',

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

def get_all_item(keywords):
    params = {
        '_from ': 'R40',
        '_trksid': 'p2334524.m570.l1313',
        '_nkw': keywords,
        '_sacat': '0',

    }
    r = requests.get(url, params=params, headers=headers)

    soup = BeautifulSoup(r.content, 'html.parser')


if __name__ == '__main__':
    keyword = input('Masukan Kata Kunci Pencarian: ')
    get_total_pages(keyword)



