from webdata import Parser
import urllib.request
import sys


def parse(html):

    p = Parser()
    p.url = ""
    p.feed(html)

    return p.WORD_COUNT

def parseWeb(html, u):
    p = Parser()
    p.url = u
    p.feed(html)

    return p.WORD_COUNT, p.URLS

def webdata(t, l):
    wordcount = 0
    if t == 'f':
        for item in l:
            with open(item, 'r') as f:
                wordcount += parse(f.read())
    if t == 'fl':
        with open(l[0], 'r') as f:
            text_list = f.read()
            l = text_list.split(',')
        for item in l:
            with open(item.strip(), 'r') as f:
                wordcount += parse(f.read())

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
    # Need to handle redirects on first url
    # that way if a site redirects the main url will
    # be the redirected url not the original url
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
    if t == 'u':
        for url in l:
            wordcount = crawler(url)
            """"with urllib.request.urlopen(url) as response:
                html = response.read()
                wordcount += parse(str(html))"""


    print('Wordcount: ' + str(wordcount))


def crawler(u):
    domain = u
    urls = [u]
    print(urls)
    history = []
    wordcount = 0

    for url in urls:
        print(urls)
        if url not in history:
            try:
                with urllib.request.urlopen(url) as response:
                    html = response.read()
                    w, u = parseWeb(str(html), url)
                    wordcount += w
                    for x in u:
                        if domain in x:
                            urls.append(x)
                    history.append(url)
            except Exception:
                print("Error: " + url)
    return wordcount


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Invalid arguments")
    else:

        #l = ['test.html', 'test2.html', 'test3.html']
        #l = ['http://novastellatranslations.com']
        #l = ['file_list.txt']
        #webdata('fl', l)
        #print(sys.argv[1], sys.argv[2])
        webdata(sys.argv[1], sys.argv[2:])
