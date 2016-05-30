from html.parser import HTMLParser
import urllib
from urllib.parse import urljoin
import re

class Parser(HTMLParser):

    HEAD_TAG_ENDED = False
    WORD_COUNT = 0
    URLS = []

    def handle_starttag(self, tag, attrs):

        if tag == 'a' and self.HEAD_TAG_ENDED:
            for (key, value) in attrs:
                if key == 'href':
                    if value.startswith('tel:') or value.startswith('mailto:') or value.startswith('#'):
                        continue
                    newUrl = urljoin(self.url, value)
                    self.URLS.append(newUrl)

    def handle_endtag(self, tag):
        if tag == "head":
            self.HEAD_TAG_ENDED = True


    def handle_data(self, data):

        if self.HEAD_TAG_ENDED:
            self.WORD_COUNT += self.count_words(data)


    def count_words(self, text):
        return len(re.findall(r'\w+', text))
