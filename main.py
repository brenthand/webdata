from webdata import Parser


def main():

    with open('test.html', 'r') as myfile:
        data=myfile.read()

    p = Parser()
    p.feed(data)

    print("Word Count: " + str(p.WORD_COUNT))


main()
