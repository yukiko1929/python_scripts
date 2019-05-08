import os
import re

def get_link(patt, filename):
    link_list = []
    cpa = re.compile(patt)
    with open(filename) as fobj:
        for lines in fobj:
            ma = cpa.search(lines)
            if  ma:
                mag = ma.group()
                link_list.append(mag)
    return link_list

def pictures(links):
    my_dict = {}
    destdir = '/mnt/img'
    for items in links:
        finalone = re.split('/',items)[-1]
        filename = os.path.join(destdir, finalone)
        my_dict[items] = filename
        with open(filename,'wb') as fobj:
            fobj.write(items.encode())
    # return my_dict

if __name__ == '__main__':
    patt = r'http://.*\.jpg'
    files = '/mnt/webcontent'
    middle = get_link(patt, files)
    # mid_res = pictures(middle)
    # print(mid_res)
    pictures(middle)
