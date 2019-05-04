# import time
#
# n = 30
# c = 0
# print('#' * 30, end = '')
#
# while True:
#     print('\r%s@%s' % ('#' * c, '#' * (n - c)), end = '')  # \r return but don't change to next line
#     c += 1
#     if c == 30:
#         c = 0
#     time.sleep(0.2)

import time

c = 0
print('#' * 30, end='')

while True:
    print('\r%s@%s' % ('#' * c, '#' * (30 - c)), end='')
    c += 1
    while c == 30:
        print('\r%s@%s' % ('#' * c, '#' * (30 - c)), end='')
        c -= 1
    time.sleep(0.2)






