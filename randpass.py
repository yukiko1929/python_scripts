
import random
#import sys
source = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.@*._'
password = str()

def pass_gen(n):
    global password
    #source = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.@*._'
    counter = 0
    while counter < n:
        counter += 1
        single = random.choice(source)
        password = password + str(single)
        return password

fixed = pass_gen(6)
print(fixed)

print('*' * 60)

len_define = int(input('length:'))
client_pass = pass_gen(len_define)
print(client_pass)


# while counter < :
#     counter += 1
#     single = random.choice(source)
#     password = password + str(single)
# print(password)
