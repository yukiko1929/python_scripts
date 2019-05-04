#num = int(input('please enter the first number:'))
#second_num = int(input('please enter the second number:'))

# fib = [0,1]
# for i in range(8):
#     fib.append(fib[-1] + fib[-2])
#
# print(fib)

# to define list's length
fib = [0,1]
n = int(input('please enter length:'))

for i in range(n-2):
    fib.append(fib[-1] + fib[-2])
print(fib)

