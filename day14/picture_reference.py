# import urllib.request
# import re
#
# url = "http://www.tedu.cn"
# webPage=urllib.request.urlopen(url)
# data = webPage.read()
# # data = data.encode()
# # data = data.decode('UTF-8')
# patt = 'http:\/\/.*\.jpg'
# # elements = re.split(r'\s', data)
# # pic_addr_list = []
# # for items in elements:
# #     if (re.match(r'http:\/\/.*\.jpg', items)):
# #         pic_addr_list.append(items)
# # print(pic_addr_list)

from urllib.request import urlopen

# single case
# def get_picture():
#     url = 'http://www.tedu.cn'
#     afile = '/mnt/webcontent'
#     webcontent = urlopen(url)
#     with open(afile) as fobj:
#         fobj.write(webcontent)
#
# def get_link():
#     patt = 'http:\///.*\.jpg'
#     cpa = re.compile(patt)
#     bfile = '/mnt/webcontent'
#     link_list = []
#     with open(bfile) as fobj:
#         for lines in fobj:
#             m = cpa.search(lines)
#             if not m:
#                 break
#             mg = m.group()
#             link_list.append(mg)

import urllib.request
def get_content(addr, contfile):
    content = urllib.request.urlopen(addr)
    with open(contfile, 'wb') as fobj:
        while True:
            data = content.read(2048)
            if data == 0:
                break
            fobj.write(data)
    fobj.close()

if __name__ == '__main__':
    addr = 'http://www.tedu.cn'
    filena = '/mnt/webcontent'
    get_content(addr, filena)




