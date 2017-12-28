from bs4 import BeautifulSoup
from common.db_setup import AirlineDatabase
import sqlite3

class SouthwestAirlines:

    @staticmethod
    def get_southwest_raw():
        southwest = open('./Southwest_Airlines/southwest_airlines.html', 'r')
        return SouthwestAirlines.southwest_html_to_json(southwest)

    def southwest_html_to_json(html):
        soup = BeautifulSoup(html, 'html.parser')
        merchant_groups = soup.find_all('a', attrs={'data-default-tab': 'merchant'})
        merchants = map(lambda x: {x.find('span', class_='mn_merchName').find(text=True, recursive=False): [x["href"], SouthwestAirlines.points_extractor(x.find('span', class_='mn_rebateValueWithCurrency')), SouthwestAirlines.domain_finder(x.find('span', class_='mn_merchName').find(text=True, recursive=False))]}, merchant_groups)
        return list(merchants)

    def points_extractor(raw):
        try:
            return raw.find('span', class_='mn_elevationNewValue').find(text=True, recursive=False).strip().split(' ')[0]
        except:
            return raw.find(text=True, recursive=False).strip().split(' ')[0]

    def domain_finder(storename):
        conn = sqlite3.connect('airlineusa.db')
        c = conn.cursor()
        data_check = AirlineDatabase.check_domain(conn, c, storename)
        if data_check == '':
            AirlineDatabase.insert_domain(conn, c, storename, 'www.testurl.com')
            AirlineDatabase.close_table(conn, c)
        else:
            AirlineDatabase.close_table(conn, c)
            return data_check
