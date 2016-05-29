from webdata import Parser
import urllib.request


def parse(html):

    """with open('test.html' , 'r') as myfile:
        html=myfile.read()"""

    p = Parser()
    p.feed(html)

    #print("Word Count: " + str(p.WORD_COUNT))
    return p.WORD_COUNT

def webdata(t, list):
    wordcount = 0
    if t == 'f':
        for item in list:
            with open(item, 'r') as f:
                wordcount += parse(f.read())
    if t == 'u':
        for url in list:
            with urllib.request.urlopen(url) as response:
                html = response.read()
                wordcount += parse(str(html))


    print('Wordcount: ' + str(wordcount))




#l = ['test.html', 'test2.html', 'test3.html']
l = ['http://novastellatranslations.com']
webdata('u', l)
