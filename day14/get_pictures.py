import urllib.request
import re

url = "http://findicons.com/pack/2787/beautiful_flat_icons"
webPage=urllib.request.urlopen(url)
data = webPage.read()
data = data.decode('UTF-8')

k = re.split(r'\s+',data)
s = []
sp = []
si = []
for i in k :
    if (re.match(r'src',i) or re.match(r'href',i)):
        if (not re.match(r'href="#"',i)):
            if (re.match(r'.*?png"',i) or re.match(r'.*?ico"',i)):
                if (re.match(r'src',i)):
                    s.append(i)

for it in s :
    if (re.match(r'.*?png"',it)):
        sp.append(it)

cnt = 0
cou = 1
for it in sp:
    m = re.search(r'src="(.*?)"',it)
    iturl = m.group(1)
    print(iturl)
    if (iturl[0]=='/'):
        continue;
    web = urllib.request.urlopen(iturl)
    itdata = web.read()
    if (cnt%3==1 and cnt>=4 and cou<=30):
        f = open('d:/pythoncode/simplecodes/image/'+str(cou)+'.png',"wb")
        cou = cou+1
        f.write(itdata)
        f.close()
        print(it)
    cnt = cnt+1