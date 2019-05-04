def gen_fibb(n):
    fib = [0, 1]
#    n = int(input('please enter length:'))   avoid using input within a function
    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    return fib

fixed_list = gen_fibb(5)
print(fixed_list)

print('#' * 50)

num = int(input('length:'))
my_list = gen_fibb(num)
print(my_list)