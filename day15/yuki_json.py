import json
from urllib import request
import requests

url = 'http://www.weather.com.cn/data/sk/101230201.html'
brow = request.urlopen(url)
data = brow.read()
print(data)
print(json.loads(data))


# url = 'http://www.weather.com.cn/data/sk/101121301.html'
# r = request.urlopen(url)
# ori_data = r.read()
# print(ori_data)
# json_data = json.loads(ori_data)
# print(json_data)

# r1 = requests.get()
# result = r1.text
# print(result)
#
# r2 = requests.get()
# with open('/tmp.haha', 'wb') as fobj:
#     fobj.write(r2.content)
#
# r3 = requests.get()
# result3 = r3.json()


