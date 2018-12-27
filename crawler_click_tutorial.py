import click
from eynyMovieCrawler import EynyMovie, WriteFile


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
    click.echo('Start parsing eyny movie....')
    url = 'http://www.eyny.com/forum-205-1.html'
    # 變數 page 為要對網頁爬的頁數，預設為 5 頁
    eyny_movie = EynyMovie(url, page)

    with click.progressbar(eyny_movie) as data:
        content = ''.join(text for text in data)

    WriteFile(output.name, content)
    click.echo('----------END----------')

    # launch file
    path = click.format_filename(output.name, shorten=True)
    click.launch(path)


if __name__ == '__main__':
    cli()
