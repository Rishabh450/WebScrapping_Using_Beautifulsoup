from bs4 import BeautifulSoup

from locators.quotepagelocator import QuotesPageLocator

from locators.QuotesLocator import QuotesLocator

from parsers.QuoteParser import QuoteParser


class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotesPageLocator.QUOTES
        quote_tags = self.soup.select(locator)
        return [QuoteParser(e) for e in quote_tags]
