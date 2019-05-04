# recursive
from random import randint
def recur1(x):
    if x == 1:
        return 1
    else:
        return x * recur1(x-1)

def guess():
    while True:
        result  = recur1(randint(1,10))
        guess = input('the number is %s, please guess the base number:' % result)


# if __name__ == '__main__':
#     print(recur1(randint(1,10)))
