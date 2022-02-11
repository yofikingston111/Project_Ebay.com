# Ebay Scraper Template

"""
contoh scraper

"""


def get_total_page(keywords):
    # digunakan untuk mencari total Halaman

    params = {
        '_from ': 'R40',
        '_trksid': 'p2334524.m570.l1313',
        '_nkw': keywords,
        '_sacat': '0',
        '_pgn':1,

    }
    

def get_all_item(keywords, pages):
    # digunakan untuk scraping data item seperti price dan item yang mau di scrape
    pass

def output():
    # digunakan untuk mencetak csv atau excelfile
    pass

def main():
    # digunakan untuk menggabungkan fungsi2 yang telah dibuat sebelumnya
    pass


if __name__=='__main__':
    main() 