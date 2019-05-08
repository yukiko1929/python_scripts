import requests
from urllib import request

import re
# when there is Chinese characters in url
url = 'http://www.sogou.com/web?query=复联4'
#request.urlopen(url)   # there would be error
#tran_char = request.quote('复联4')
fina = re.split('=', url)[-1]
ori = re.split('=', url)[0]
new_url = ori + request.quote(fina)
print(new_url)

