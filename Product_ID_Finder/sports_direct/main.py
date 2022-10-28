from requests import get
from bs4 import BeautifulSoup as bs
from json import load


def get_settings():
    with open("settings.json", "r") as file:
        data = load(file)
        file.close()

    return data


settings = get_settings()
HEADERS = settings['Headers']
LEN_ID = 6


def write_to_file(ids):
    filename = 'ids.txt'
    with open(filename, 'w') as file:
        file.write('\n'.join(ids))
        file.close()
    print('Done')


def get_ids(locs):
    ids = []
    for loc in locs:
        loc = loc.text.strip()
        pos1 = len(loc) - LEN_ID
        ids.append(loc[pos1: -1])

    write_to_file(ids=ids)


def main():
    for i in range(1, 2):
        url = f'https://www.sportsdirect.com/sitemap-product-{i}.xml'
        response = get(url=url, headers=HEADERS)
        soup = bs(response.content, 'lxml')
        locs = soup.find_all('loc')

        get_ids(locs=locs)


if __name__ == '__main__':
    main()
