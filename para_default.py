def gen_fibb(n=8):
    fib = [0, 1]
    n = int(input('please enter length:'))

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    return fib

my_list = gen_fibb()
print(my_list)
plus_list = [10 + i for i in my_list]
print(plus_list)
