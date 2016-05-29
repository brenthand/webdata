from HTMLParser import HTMLParser
import re

class Parser(HTMLParser):



    HEAD_TAG_ENDED = False
    TEXT_TAGS = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'button', 'label', 'a',]
    URL_HISTORY = []
    URLS = []
    WORD_COUNT = 0


    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if self.HEAD_TAG_ENDED and tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined, print it.
               if name == "href":
                   #Handle domain specific urls and
                   # create full path urls for
                   #relative urls
                   self.URLS.append(value)

    def handle_endtag(self, tag):
        if tag == "head":
            self.HEAD_TAG_ENDED = True


    def handle_data(self, data):

        if self.HEAD_TAG_ENDED:
            self.WORD_COUNT += self.count_letters(data)


    def count_letters(self, text):
        return len(re.findall(r'\w+', text))
