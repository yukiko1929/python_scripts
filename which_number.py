# # [100 + i for i in alist]
# import math
# def isSqr(n):
#     check = int(math.sqrt(n))
#     return check * check
# for i in range(100000):
#     isSqr(i)

import math
for i in range(100000):
    cal1 = int(math.sqrt(i + 100))
    cal2 = int(math.sqrt(i + 268))
    if cal1*cal1 == i + 100 and cal2 * cal2 == i + 268:
        print(i)

