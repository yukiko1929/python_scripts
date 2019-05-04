# file---organize code in a physical way
# module --- organize code in a logical way
# there is a file named module_test.py, and its content is as follows:
def find_number():
    import math
    for i in range(100000):
        cal1 = int(math.sqrt(i + 100))
        cal2 = int(math.sqrt(i + 268))
        if cal1 * cal1 == i + 100 and cal2 * cal2 == i + 268:
            print(i)

greeting = 'hello yukiko'

def pstar(n=50):
    print('*' * n)

# change the directory into Pycharm
# python3  ---> import module_test ---> module_test.greeting ---> module_test.find_number() ---> module_test.pstar()

# to import limited attribute from module
# from random import randint


