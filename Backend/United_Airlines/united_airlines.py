from bs4 import BeautifulSoup

class UnitedAirlines:

    @staticmethod
    def get_united_raw():
        united = open('./United_Airlines/united_airlines.html', 'r')
        return UnitedAirlines.united_html_to_json(united)

    def united_html_to_json(html):
        soup = BeautifulSoup(html, 'html.parser')
        merchant_groups = soup.find_all('a', attrs={'data-default-tab': 'merchant'})
        merchants = map(lambda x: {x.find('span', class_='mn_merchName').get_text(): [x["href"], UnitedAirlines.points_extractor(x.find('span', class_='mn_rebateValueWithCurrency'))]}, merchant_groups)
        return list(merchants)

    def points_extractor(raw):
        try:
            return raw.find('span', class_='mn_elevationNewValue').get_text().strip().split(' ')[0]
        except:
            return raw.get_text().strip().split(' ')[0]

    def anchor_to_data(anchor):
        try:
            inner = UnitedAirlines.points_extractor(anchor.find('span', class_='mn_rebateValueWithCurrency'))
        except:
            #Skip
            print("Nope")
