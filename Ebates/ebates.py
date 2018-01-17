from bs4 import BeautifulSoup

class Ebates:

    @staticmethod
    def get_ebates_raw():
        ebates = open('./ebates.html', 'r')
        return Ebates.ebates_html_to_json(ebates)

    def ebates_html_to_json(html):
        soup = BeautifulSoup(html, 'html.parser')
        stores = soup.find_all('li', attrs={'class': 'store'})
        merchants = map(lambda x: {Ebates.name_extractor(x): Ebates.url_extractor(x)}, stores)
        return list(merchants)

    def name_extractor(raw):
        return raw.find('span', attrs={'class': 'store-name'}).find('a').find(text=True, recursive=False)

    def url_extractor(raw):
        return 'https://www.ebates.com' + raw.find('span', attrs={'class': 'store-shop'}).find('a')['href']


print(Ebates.get_ebates_raw())
