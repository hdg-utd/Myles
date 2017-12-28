from bs4 import BeautifulSoup

class DeltaAirlines:

    @staticmethod
    def get_delta_raw():
        delta = open('./Delta_Airlines/delta_airlines.html', 'r')
        return DeltaAirlines.delta_html_to_json(delta)

    def delta_html_to_json(html):
        soup = BeautifulSoup(html, 'html.parser')
        merchant_groups = soup.find_all('a', attrs={'data-default-tab': 'merchant'})
        merchants = map(lambda x: {x.find('span', class_='mn_merchName').get_text(): [x["href"], DeltaAirlines.points_extractor(x.find('span', class_='mn_rebateValueWithCurrency'))]}, merchant_groups)
        return list(merchants)

    def points_extractor(raw):
        try:
            return raw.find('span', class_='mn_elevationNewValue').get_text().strip().split(' ')[0]
        except:
            return raw.get_text().strip().split(' ')[0]
