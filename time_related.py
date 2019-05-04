# import time
#
# print(time.time())
# print(time.ctime())
# print(time.localtime())
#
# t1 = time.strftime('%Y-%m-%d %H-%M-%S')
# t2 = time.strptime(t1, '%Y-%m-%d %H-%M-%S')
#
# t3 = time.localtime()
#
# result = t2 > t3
# print(result)

import time
from datetime import datetime
t1 = datetime.now()
print(t1)
t2 = datetime(2018, 12, 24, 10)
t3 = time.strftime('%Y-%m-%d %H')
# t4 = time.strptime()
result = t1 > t2
print(result)

