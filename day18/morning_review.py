from urllib import request
import re
import os

def get_content(url, fname):
    content = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = content.read(2048)
            if not data:
                break
            fobj.write(data)

def get_links(fname, pattern, destdir):
    link_list = []
    cpa = re.compile(pattern)
    with open(fname, 'rb') as fobj:
        for lines in fobj:
            mapa = cpa.search(lines)
            if mapa:
                mapagr = mapa.group()
                link_list.append(mapagr)
    # return link_list
    for items in link_list:
        pic_name = re.split('/',items)[-1]
        pic_name= os.path.join(destdir, pic_name)
        with open(pic_name,'wb') as fobj2:
            fobj2.write(items)

if __name__ == '__main__':
    url = 'www.tedu.com'
    pattern = 'http://(\w./).jpg'
    filename = '/tmp/urlcontent'
    destdir = '/tmp/teduimg'
    get_content(url, filename)
    get_links(filename,pattern,destdir)



# mysql
import pymysql

connect = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    db = 'yuki4',
    user = 'root',
    charset = 'utf8'
)

cursor = connect.cursor()

create_staff = '''create table staff(
      sta_name CHAR(20),
      sta_id INT,
      sta_age INT,
      PRIMARY KEY(sta_id) 
)'''

create_department = '''create table department(
      department CHAR(20),
      
)'''







