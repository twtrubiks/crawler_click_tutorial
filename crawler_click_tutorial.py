import re

import click
import requests
from bs4 import BeautifulSoup

targetURL = 'http://www.eyny.com/forum-205-1.html'


def pattern_mega_google(text):
    patterns = [
        'mega', 'mg', 'mu', 'ＭＥＧＡ', 'ＭＥ', 'ＭＵ',
        'ｍｅ', 'ｍｕ', 'ｍｅｇａ', 'GD', 'MG', 'google',
    ]

    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True


@click.command()
@click.option('--page',
              default=5,
              type=click.IntRange(1, 10),
              help='Crawler page (default 5 pages)')
@click.option('--output',
              default='eyny-Movie-Mage.txt',
              type=click.File('wb'),
              help='output fileName (default eyny-Movie-Mage.txt)')
def cli(page, output):
    # 變數 page 為要對網頁爬的頁數，預設為 5 頁
    click.echo('Start parsing eyny movie....')
    rs = requests.session()
    res = rs.get(targetURL, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    page_url, page_link_all = [], []

    # first page
    page_url.append(targetURL)
    page_link_all = soup.select('.pg')[0].find_all('a')
    # 得到每頁的page link
    for index in range(1, page, 1):
        page_url.append('http://www.eyny.com/' + page_link_all[index]['href'])

    content = ''

    # 得到每篇包含 mega 的文章
    with click.progressbar(page_url) as urls:
        for url in urls:
            res = rs.get(url, verify=False)
            soup = BeautifulSoup(res.text, 'html.parser')
            for title_url in soup.select('.bm_c tbody .xst'):
                if pattern_mega_google(title_url.text):
                    name_write = title_url.text
                    url_write = 'http://www.eyny.com/{}'.format(title_url['href'])
                    content += '{}\n{}\n\n'.format(name_write, url_write)
            content += '----next page-----\n\n'

    with output as f:
        f.write(content.encode('utf8'))

    click.echo('----------END----------')
    path = click.format_filename(output.name, shorten=True)
    click.launch(path)


if __name__ == '__main__':
    cli()
