from webdata import Parser
import urllib.request
import tkinter
import sys


def parse(html):

    """with open('test.html' , 'r') as myfile:
        html=myfile.read()"""

    p = Parser()
    p.feed(html)

    #print("Word Count: " + str(p.WORD_COUNT))
    return p.WORD_COUNT

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

    if t == 'u':
        for url in l:
            with urllib.request.urlopen(url) as response:
                html = response.read()
                wordcount += parse(str(html))


    print('Wordcount: ' + str(wordcount))


def get_list(f):
    with open(f, 'r') as x:
        text_list = x.read()
        l = text_list.split(',')

    return(l)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Invalid arguments")
    else:

        #l = ['test.html', 'test2.html', 'test3.html']
        #l = ['http://novastellatranslations.com']
        #l = ['file_list.txt']
        #webdata('fl', l)
        webdata(sys.argv[1], sys.argv[2:])
