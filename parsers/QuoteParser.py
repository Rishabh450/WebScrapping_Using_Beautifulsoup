from locators import QuotesLocator
from bs4 import BeautifulSoup


class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Quote: {self.content}\n--- {self.author}\ntags: {self.tags}'

    @property
    def content(self):
        locator = QuotesLocator.QuotesLocator.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuotesLocator.QuotesLocator.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuotesLocator.QuotesLocator.TAGS
        return self.parent.select_one(locator).string

