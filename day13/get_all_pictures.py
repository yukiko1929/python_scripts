from urllib import request
import pickle
import re
import os

def get_pictures(fname, destdir):
    # get source code
    r = request.urlopen('http://www.163.com')
    with open(fname, 'wb') as fobj:
        while True:
            data = r.read(1024)
            if not data:
                break
            fobj.write(data)

    patterns = '\w{4}:\/\/.*\.png'
    fin_res = []
    p1 = re.compile(patterns)
    with open(fname,'r') as fobj2:
        data = pickle.load(fobj2)
        for lines in data:
            result = p1.search(lines)
            if result:
                break
            else:
                fin_res.append(result)

    for item in fin_res:
        files = os.path.join(destdir,item)
        for file in files:
            with open(file, 'r') as fnobj:
                fnobj.write(item)

if __name__ == '__main__':
    fname = '/tmp/source.record'
    destdir = '/mnt'
    get_pictures(fname, destdir)

