from functools import partial
def add(a, b, c, d, e):
    return a+b+c+d+e

myadd = partial(add, 10,20,30,40)
print(myadd(5))
print(myadd(100))

