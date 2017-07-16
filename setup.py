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
