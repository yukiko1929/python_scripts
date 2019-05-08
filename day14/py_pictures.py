import urllib
from urllib import request
import re
import pickle
import codecs

def get_data(filename):
    all_list = []
    patt = 'http:\/\/.*\.png'
    cpa = re.compile(patt)
    with codecs.open(filename,'r',encoding='utf-8', errors='ignore') as fobj:
        for lines in fobj:
            # orig = re.search(cpa, lines)
            orig = cpa.search(lines)
            origg = orig.group()
            if not orig:
                break
            all_list.append(origg)
    return all_list
    # websource = urllib.request.urlopen(aurl)
    # data = websource.read()

    # pic_list = []
    # for line in data:
    #     matchurl = re.match(r'.*?(http:\/\/.*\.png).*', line)
    #     if not matchurl:
    #         break
    #     matchg = matchurl.group(1)
    #     pic_list.append(matchg)
    # return pic_list

if __name__ == '__main__':
    # aurl = 'http://ww.163.com'
    filena = '/mnt/163.txt'
    result = get_data(filena)
    print(result)







    # data = data.decode('UTF-8')
#     with open(filename,'wb') as fobj:
#         fobj.write(data)
#
# if __name__ == '__main__':
#     filena = '/mnt/163.txt'
#     urll = 'http://www.163.com'
#     get_data(urll, filena)