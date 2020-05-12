import requests

from pages.quotes_pages import QuotesPage

page_content = requests.get('http://quotes.toscrape.com')
page = QuotesPage(page_content.text)

for quote in page.quotes:
    print(quote)