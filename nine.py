
# for x in range(1,10):   # how many lines
#     for y in range(1,x+1):  # how many times in a line
#         result = x * y
#         print('%s * %s= %s' % (y,x,result), end=' ')
#     print()

numbers = range(1,10)

for i in numbers:
    for j in numbers:
        result  = i * j
        print('%s*%s=%s' % (i,j,result), end=' ')
    print()

# define = int(input())