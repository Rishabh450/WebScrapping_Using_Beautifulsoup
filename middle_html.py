import requests
from bs4 import BeautifulSoup

page = requests.get('http://14.139.205.171/NITJ_NEW')
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.select_one('head title').string)
