#AIRLINE_ID = 1

from bs4 import BeautifulSoup
from common.db_setup import AirlineDatabase
import sqlite3
from common.google import GoogleSearch

class AmericanAirlines:
    @staticmethod
    def get_aa_raw():
        aa = open('./American_Airlines/american_airlines.html', 'r')
        return AmericanAirlines.aa_html_to_json(aa)
        #return AmericanAirlines.aa_html_to_json(aa)

    def aa_html_to_json(html):
        soup = BeautifulSoup(html, 'html.parser')
        merchant_groups = soup.find_all('a', attrs={'data-default-tab': 'merchant'})
        merchants = map(lambda x: {x.find('span', class_='mn_merchName').find(text=True, recursive=False): [x["href"], AmericanAirlines.points_extractor(x.find('span', class_='mn_rebateValueWithCurrency')), AmericanAirlines.domain_finder(x.find('span', class_='mn_merchName').find(text=True, recursive=False))]}, merchant_groups)
        #conn = sqlite3.connect('airlineusa.db')
        #c = conn.cursor()
        #for merchant in merchant_groups:
        #    domain = AmericanAirlines.domain_finder(merchant.find('span', class_='mn_merchName').find(text=True, recursive=False))
        #    store_name = merchant.find('span', class_='mn_merchName').find(text=True, recursive=False)
        #    affiliate_link = merchant["href"]
        #    points = AmericanAirlines.points_extractor(merchant.find('span', class_='mn_rebateValueWithCurrency'))
        #AirlineDatabase.close_table(conn, c)
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
        if data_check == '' or data_check == 'none':
            domain = GoogleSearch(storename)
            AirlineDatabase.insert_domain(conn, c, storename, domain)
            AirlineDatabase.close_table(conn, c)
            return domain
        else:
            AirlineDatabase.close_table(conn, c)
            return data_check
