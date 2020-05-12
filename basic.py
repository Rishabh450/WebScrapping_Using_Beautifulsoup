from bs4 import BeautifulSoup
from collections import defaultdict

SIMPLE_HTML = """
<html>
<head>
</head>
<body>
<h1>This is the title</h1>
<p class="subtitle">Subtitle paragraph</p>
<p>Non</p>
<ul>
<li>Rolf</li>
<li>Rolf</li>
<li>Rolf</li>
<li>Rolf</li>
<li>Rolf</li>

</ul>

</body>
</html>
"""
simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():
    return simple_soup.find('h1').string


def find_list_items():
    return [list_item.string for list_item in simple_soup.find_all('li')]


def find_subtitle():
    para = simple_soup.find('p', {'class': 'subtitle'})
    return para.string


def find_para():
    all_para = simple_soup.find_all('p')
    other_para = [para.string for para in all_para if
                  para.attrs.get('class') is None or 'subtitle' not in para.attrs.get('class')]
    return other_para


print(find_para())
