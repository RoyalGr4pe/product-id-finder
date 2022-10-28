from requests import get
from json import load
from bs4 import BeautifulSoup as bs


def get_settings():  # Get all the data that is stored in settings.json
    with open('settings.json', 'r') as file:
        settings = load(file)
        file.close()

    return settings


settings = get_settings()
HEADERS = {'User-Agent': settings['User-Agent']}
DOMAIN = settings['Country Domain']
LANGUAGE = settings['Language']
COUNTRY = settings['Country']


url = f'https://www.adidas{DOMAIN}/on/demandware.static/-/Sites-CustomerFileStore/default/adidas-{COUNTRY}/{LANGUAGE}/sitemaps/product/adidas-{COUNTRY}-en-{COUNTRY.lower()}-product.xml'
response = get(url=url, headers=HEADERS)

soup = bs(response.content, 'lxml')

skus = []

locs = soup.find_all('loc')
for loc in locs:
    print(type(loc))
    pos1 = int(loc.find('.html'))
    pos2 = int(pos1 - 6)

    sku = loc[pos2: pos1]

    skus.append(sku)

filename = f'{COUNTRY}_skus.txt'
with open(filename, 'w') as file:
    file.write('\n'.join(skus))
    file.close()

print('Done')
