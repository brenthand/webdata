import sys, thread, Queue, re, urllib, urlparse, time, os, sys
dupcheck = set()
q = Queue.Queue(100)
q.put(sys.argv[1])

def getUrls(html, baseUrl):
    for url in re.findall('''<a[^>]+href=["'](.[^"']+)["']''', html, re.I):
        link = url.split("#", 1)[0] if url.startswith("http") else '{uri.scheme}://{uri.netloc}'.format(uri=urlparse.urlparse(baseUrl)) + url.split("#", 1)[0]
        newUrl = parse.urljoin(self.baseUrl, value)
        if link in dupcheck or baseUrl  not in link:
            continue
        dupcheck.add(link)

        q.put(link)

def getHTML(link):
    try:
        html = urllib.urlopen(link).read()
        #open(str(time.time()) + ".html", "w").write("" % link  + "\n" + html)
        getUrls(html, link)
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception:
        pass

while True:
    thread.start_new_thread( getHTML, (q.get(),))
    time.sleep(0.5)
