from bs4 import BeautifulSoup
import sqlite3
from common.db_setup import EbatesDatabase
from common.google import GoogleSearch
import json

class Ebates:

    @staticmethod
    def get_ebates_raw():
        ebates = open('./ebates.html', 'r')
        return Ebates.list_cleaner(Ebates.ebates_html_to_json(ebates))

    def ebates_html_to_json(html):
        soup = BeautifulSoup(html, 'html.parser')
        stores = soup.find_all('li', attrs={'class': 'store'})
        merchants = map(lambda x: {Ebates.name_extractor(x): [Ebates.url_extractor(x), Ebates.points_extractor(x), Ebates.domain_finder(Ebates.name_extractor(x))]}, stores)
        return list(merchants)

    def name_extractor(raw):
        return raw.find('span', attrs={'class': 'store-name'}).find('a').find(text=True, recursive=False)

    def url_extractor(raw):
        return 'https://www.ebates.com' + raw.find('span', attrs={'class': 'store-shop'}).find('a')['href']

    def points_extractor(raw):
        points_str = raw.find('span', attrs={'class': 'store-rebate'}).find('a').find(text=True, recursive=False)
        if '\n' in points_str:
            points_str = points_str.split('\n')[0]
        for item in points_str.split(' '):
            if '%' in item:
                return item.split('%')[0]
        return ''

    def domain_finder(storename):
        conn = sqlite3.connect('ebates.db')
        c = conn.cursor()
        data_check = EbatesDatabase.check_domain(conn, c, storename)
        if data_check == '' or data_check == 'none':
            domain = GoogleSearch(storename)
            EbatesDatabase.insert_domain(conn, c, storename, domain)
            EbatesDatabase.close_table(conn, c)
            return domain
        else:
            EbatesDatabase.close_table(conn, c)
            return data_check

    def list_cleaner(raw):
        result = {}
        for item in raw:
            print()
            if item[list(item.keys())[0]][1] == '':
                continue
            else:
                result[list(item.keys())[0]] = item[list(item.keys())[0]]
        return result

ebates = {}
ebates["ebates"] = Ebates.get_ebates_raw()

with open('./ebates.json', 'w') as fp:
    json.dump(ebates, fp)
