import time

c = 0
print('#' * 30, end = '')

while True:
    print('\r%s@%s' % ('#' * c, '#' * (30 - c)), end = '')  # \r return but don't change to next line
    c += 1
    if c == 30:
        print('\r%s@%s' % ('#' * (30-c), '#' * c), end = '')
        c -= 1
