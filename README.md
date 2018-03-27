# crawler_click_tutorial

今天教大家用 python 建立屬於自己的 command line tool :smirk:

由於最近剛好看到  [click](http://click.pocoo.org) 這個東西，所以決定要拿之前的小程式來把玩一下 :smile:，

本範例使用之前所寫的簡單爬蟲 [eynyCrawlerMega](https://github.com/twtrubiks/eynyCrawlerMega) 。

* [Youtube Tutorial](https://youtu.be/6b2iEg3J8ak)

## 特色

* 抓取 eyny 電影區 Mega and Google 文章連結

## 輸出格式

* 文字檔 ( 爬蟲結束後會自動開啟文字檔 )

## click 教學

### 安裝 click

```python
pip install click
```

### 官方範例 demo

hello.py 程式碼如下

```python
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()
```

為什麼要用 `click.echo()` 而不是 `print()`呢 ?

 因為這樣可以解決一些編碼上的問題 ( 詳細請看 [click](http://click.pocoo.org) 的 source code )。

然後我們可以這樣使用

> python hello.py --count=3

![](http://i.imgur.com/qvRWy5f.png)

>python hello.py --help

![](http://i.imgur.com/7By9mnp.png)

### 建立 command line tool

接下來介紹建立屬於自己的 command line tool，

可以參考我的 [setup.py](https://github.com/twtrubiks/crawler_click_tutorial/blob/master/setup.py) ，程式碼如下

```python
from setuptools import setup

setup(
    name='crawler_click_tutorial',
    version='0.1',
    py_modules=['crawler_click_tutorial'],
    install_requires=[
        'Click',
        'requests',
        'beautifulsoup4',
    ],
    entry_points='''
        [console_scripts]
        movie=crawler_click_tutorial:cli
    ''',
)

```

最後只需要在 cmd ( 命令提示字元 ) 執行

> pip install --editable .

***注意，最後有個  `.`***

![](http://i.imgur.com/aHSERyT.png)

以後，只要在 cmd ( 命令提示字元 )  輸入 `movie` 即可 !!

## 執行畫面

首先，讓我們先來看看有什麼指令可以使用

> movie --help

![](http://i.imgur.com/kH6D5lE.png)

> movie

![](http://i.imgur.com/XxixGcf.png)

![](http://i.imgur.com/T7gaYmf.png)

超酷 :satisfied: ，還有進度條 :open_mouth:

最後會自動幫你打開文件

![](http://i.imgur.com/fpDRbza.png)

> movie --page=5 --output=output_file.txt

![](http://i.imgur.com/8BgbudN.png)

簡單防呆機制

> movie --page=11

![](http://i.imgur.com/qy9zDPd.png)

## 結論

[click](http://click.pocoo.org) 真的超讚 :thumbsup: ，
可以利用它打造出屬於自己的  command line tool ，

不管是娛樂還是加速自己的工作流程都非常方便。

## Environment

Python 3.5.3

## Reference

* [click](http://click.pocoo.org)

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT license
