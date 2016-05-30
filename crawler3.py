from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse

class CrawlerParser(HTMLParser):

    HEAD_TAG_ENDED = False
    URLS = []
    URL_HISTORY = []
    WORD_COUNT = 0

    def handle_starttag(self, tag, attrs):
        local_urls =
        if tag  'a' and HEAD_TAG_ENDED:
            for (key, value) in attrs:
                if key  'href':
                    return newUrl = parse.urljoin(self.baseUrl, value)


    def handle_endtag(self, tag):
        if tag == "head":
            self.HEAD_TAG_ENDED = True

    def getLinks(self, url):
        self.links = []
        self.baseUrl = url
        response = urlopen(url)
        if response.getheader('Content-Type')=='text/html':
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return self.links
        else:
            return "",[]

class Crawler:

    def parse(html):

        p = Parser()
        p.feed(html)

        return p.WORD_COUNT

    def crawl(d):
        domain = d
        urls = [d]
        history = []

        for u in urls:

            with urllib.request.urlopen(url) as response:
                html = response.read()
                wordcount += CrawlerParser.feed(str(html))


    def get_html(link):
        pass


    def get_urls(html, link):

        links = CrawlerParser.getLinks(url)
        #html = urllib.urlopen(link).read()

        getUrls(html, link)

while URLS:
    links = CrawlerParser.getLinks(url)
