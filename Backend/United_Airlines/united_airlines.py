from bs4 import BeautifulSoup
from common.db_setup import AirlineDatabase
import sqlite3

class UnitedAirlines:

    @staticmethod
    def get_united_raw():
        united = open('./United_Airlines/united_airlines.html', 'r')
        return UnitedAirlines.united_html_to_json(united)

    def united_html_to_json(html):
        soup = BeautifulSoup(html, 'html.parser')
        merchant_groups = soup.find_all('a', attrs={'data-default-tab': 'merchant'})
        merchants = map(lambda x: {x.find('span', class_='mn_merchName').find(text=True, recursive=False): [x["href"], UnitedAirlines.points_extractor(x.find('span', class_='mn_rebateValueWithCurrency')), UnitedAirlines.domain_finder(x.find('span', class_='mn_merchName').find(text=True, recursive=False))]}, merchant_groups)
        return list(merchants)

    def points_extractor(raw):
        try:
            return raw.find('span', class_='mn_elevationNewValue').find(text=True, recursive=False).strip().split(' ')[0]
        except:
            return raw.find(text=True, recursive=False).strip().split(' ')[0]

    def anchor_to_data(anchor):
        try:
            inner = UnitedAirlines.points_extractor(anchor.find('span', class_='mn_rebateValueWithCurrency'))
        except:
            #Skip
            print("Nope")

    def domain_finder(storename):
        conn = sqlite3.connect('airlineusa.db')
        c = conn.cursor()
        data_check = AirlineDatabase.check_data(conn, c, storename)
        if data_check == '':
            AirlineDatabase.insert_data(conn, c, storename, 'www.testurl.com')
            AirlineDatabase.close_table(conn, c)
        else:
            AirlineDatabase.close_table(conn, c)
            return data_check
