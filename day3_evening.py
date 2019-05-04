# for loop
# fib = [1,1]
# n = int(input('length:'))
#
# for i in range(n):
#     fib.append(fib[-1] + fib[-2])
#
# print(fib)

# # to use function
# def fib(n):
#     fib = [1,1]
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#         return fib
#
# default_fib = fib(7)
# print(default_fib)
#
# #user_defined available
# rounds = int(input('length:'))
# self_fib = fib(rounds)
# print(self_fib)

#file object
# old_file = open('/tmp/passwd','rb')
# new_file = open('/opt/passwd','wb')
#
# data = old_file.read()
# new_file.write(data)
#
# new_file.close()
# old_file.close()

#to use sys.argv module in file object
#from sys import argv
# import sys
# old_file = sys.argv[1]
# new_file = sys.argv[2]
#
# data = old_file.read()
# new_file.write(data)
#
# old_file.close()
# new_file.close()

# import sys
# def copy(src_file, dest_file):
#     src_fo = open(src_file,'rb')
#     dest_fo = open(dest_file,'wb')
#     data = src_fo.read()
#     dest_fo.write(data)
#     src_fo.close()
#     dest_fo.close()
#
# copy(sys.argv[1],sys.argv[2])
#
# # file seek, concerning pointer
# # to type directly in command line
# old_file = open('/tmp/lyrics')
# old_file.read(4)
# old_file.tell()  # to check the pointer position
# old_file.seek(0,0)  # back to the start
# old_file.seek(-10,2)
# old_file.close()
#
# # if you don't want to type file_name.close() to close the file, use "with"
# with open('/tmp/1.txt') as file1:
#     file1.read()       # the result i---reading the whole passage and close the file.

# # else in while loop
# import random
# counter = 0
# answer = random.randint(0,40)
#
# while counter < 4:
#     counter += 1
#     guess = int(input('have a guess:'))
#     if guess < answer:
#         print('get a bigger one')
#     elif guess > answer:
#         print('get a smaler one')
#     else:
#         print('bingo')
#         break
# else:
#     print('the answer is %s' % answer)


# default parameter
import random
#source = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg'
def pass_gen(n = 6):
    counter = 0
    password = str()
    while counter < n:
        counter += 1
        source = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg'
        single = random.choice(source)
        password = password + str(single)
    return password


num = int(input('length'))
de_pass = pass_gen(num)
print(de_pass)

















