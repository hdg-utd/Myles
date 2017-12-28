from bs4 import BeautifulSoup
from common.domain_name import DomainFinder
print(DomainFinder.get_domain_name("Testereed"))
class AmericanAirlines:

    @staticmethod
    def get_aa_raw():
        aa = open('./American_Airlines/american_airlines.html', 'r')
        return AmericanAirlines.aa_html_to_json(aa)

    def aa_html_to_json(html):
        soup = BeautifulSoup(html, 'html.parser')
        merchant_groups = soup.find_all('a', attrs={'data-default-tab': 'merchant'})
        merchants = map(lambda x: {x.find('span', class_='mn_merchName').get_text(): [x["href"], AmericanAirlines.points_extractor(x.find('span', class_='mn_rebateValueWithCurrency'))]}, merchant_groups)
        return list(merchants)

    def points_extractor(raw):
        try:
            return raw.find('span', class_='mn_elevationNewValue').get_text().strip().split(' ')[0]
        except:
            return raw.get_text().strip().split(' ')[0]
