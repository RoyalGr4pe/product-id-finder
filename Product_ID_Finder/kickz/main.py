from requests import get
from bs4 import BeautifulSoup as bs
from json import load


def get_settings():
    with open("settings.json", "r") as file:
        data = load(file)
        file.close()

    return data


settings = get_settings()
COUNTRY = settings['Country']
HEADERS = settings['Headers']
LEN_ID = 9


def write_to_file(ids):
    filename = COUNTRY+'_ids.txt'
    with open(filename, 'w') as file:
        file.write('\n'.join(ids))
        file.close()
    print('Done')


def get_ids(locs):
    ids = []
    for loc in locs:
        loc = loc.text.strip()
        pos2 = int(loc.find('.html'))
        pos1 = pos2 - LEN_ID
        ids.append(loc[pos1: pos2])
    
    write_to_file(ids=ids)


def main():
    url = f'https://www.kickz.com/{COUNTRY.lower()}/sitemap_0-product.xml'
    response = get(url=url, headers=HEADERS)
    soup = bs(response.content, 'lxml')
    locs = soup.find_all('loc')
    
    get_ids(locs=locs)


if __name__ == '__main__':
    main()
