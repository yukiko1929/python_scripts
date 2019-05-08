# import re
#
# line = 'the website is http://www.kinder.cn/ and it updates on 22:22pm everyday and closes on Sunday'
#
# match1 = re.match(r'.*(http:\/\/.*\/).*[uU]pdate.*?(\d+:\d+.*?).*?[close|closes].*on.*?(\w+)', line)
# if match1:
#     print(match1.group())
#     print(match1.group(1))
#     print(match1.group(2))
#     print(match1.group(3))
# else:
#     print('no content matches')

from urllib.request import urlopen

# single case
# def get_picture():
url = 'http://www.tedu.cn'
afile = '/mnt/webcontent'
webcontent = urlopen(url)
with open(afile, 'w') as fobj:
    fobj.write(webcontent)
    fobj.close()