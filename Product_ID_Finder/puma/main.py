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
LEN_ID = 5


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
    return ids


def main():
    ids = []
    for i in range(1, 30):
        url = f'https://{COUNTRY}.puma.com/assets/sitemaps/{COUNTRY}/sitemap_{i}.xml'
        response = get(url=url, headers=HEADERS)
        soup = bs(response.content, 'lxml')
        locs = soup.find_all('loc')
        for ID in get_ids(locs=locs):
            ids.append(ID)

    write_to_file(ids=ids)


if __name__ == '__main__':
    main()
