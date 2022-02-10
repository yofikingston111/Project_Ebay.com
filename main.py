import os

import requests
from bs4 import BeautifulSoup

url = 'https://www.ebay.com/sch/i.html?'
params ={
'_from ': 'R40',
'_trksid': 'p2334524.m570.l1313',
'_nkw': 'iphone',
'_sacat': '0',


}
headers = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

result=[]

res = requests.get(url, params=params, headers=headers)
r = requests.get(url, params=params, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')


content = soup.find_all('div', 's-item s-item__pl-on-bottom')

try: # s
    os.mkdir('json_result')
except FileExistsError:
    pass
# scraping proccess
headers_contents = soup.find_all('li', 's-item s-item__pl-on-bottom')


for content in headers_contents:
    title = content.find('h3', 's-item__title').text

    try:
        price = content.find('span', 's-item__price').text
    except:
        continue
    try:
        location = content.find('span', 's-item__itemLocation').text
    except:
        continue
    try:
        review = content.find('span', 's-item__reviews-count').text
    except:
        review='no review'
    # print(price)
    # print(location)
    # final data
    final_data = {
    'title' : title,
    'price' : price,
    'location' : location,
    'review' : review,
    }
    result.append(final_data)

    print(final_data)

