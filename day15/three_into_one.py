import os
import re
import urllib.request

# def get_content(addr, contfile):
#     content = urllib.request.urlopen(addr)
#     with open(contfile, 'wb') as fobj:
#         while True:
#             data = content.read(2048)
#             if data == 0:
#                 break
#             fobj.write(data)
#     fobj.close()
#
# def get_link(patt, filename):
#     link_list = []
#     cpa = re.compile(patt)
#     with open(filename) as fobj:
#         for lines in fobj:
#             ma = cpa.search(lines)
#             if  ma:
#                 mag = ma.group()
#                 link_list.append(mag)
#     return link_list
#
# def pictures(links):
#     my_dict = {}
#     destdir = '/mnt/img'
#     for items in links:
#         finalone = re.split('/',items)[-1]
#         filename = os.path.join(destdir, finalone)
#         my_dict[items] = filename
#         with open(filename,'wb') as fobj:
#             fobj.write(items.encode())
    # return my_dict

def get_photos(filename, addr, patterns, destdir, encoding = 'utf8'):
    r = urllib.request.urlopen(addr)
    with open(filename, 'wb') as fobj:
        while True:
            data = r.read(2048)
            if not data:
                break
            fobj.write(data)

    link_list = []
    cpa = re.compile(patterns)
    with open(filename, encoding=encoding) as fobj2:
        for lines in fobj2:
            mg = cpa.search(lines)
            if mg:
                mgg = mg.group()
                link_list.append(mgg)
    # return link_list

    for item in link_list:
        base = re.split('/',item)[-1]
        fname = os.path.join(destdir, base)
        with open(fname,'wb') as fobj3:
            fobj3.write(item.encode())

if __name__ == '__main__':
    filename = '/mnt/web0425'
    addr = 'http://www.163.com'
    pattenrs = 'http://[\w/.-]+\.jpg'
    destdir = '/mnt/163img'
    get_photos(filename,addr,pattenrs,destdir,'gbk')


