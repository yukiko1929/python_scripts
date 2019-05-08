from urllib import request
import re
import os

def get_pics(url, fname, patt, destdir):
    content = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = content.read(2048)
            if not data:
                break
            fobj.write(data)

    link_list = []
    cpa = re.compile(patt)
    with open(fname) as fobj2:
        for lines in fobj2:
            ma = cpa.search(lines)
            if ma:
                mag = ma.group()
                link_list.append(mag)

    for items in link_list:
        base = os.path.split('/', items)
        finame =