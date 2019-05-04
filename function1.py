# function
# def gen_fibb():
#     fib = [0, 1]
#     n = int(input('please enter length:'))
#
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#     print(fib)
#
# gen_fibb()

def gen_fibb():
    fib = [0, 1]
    n = int(input('please enter length:'))

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    return fib

mylist = gen_fibb()
print(mylist)
