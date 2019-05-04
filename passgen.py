from random import choice
from sys import argv
from string import ascii_letters, digits
#all_list = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKZXCVBNM'
all_list = ascii_letters + digits

def pass_gen(n=6):
    result = ''
    for i in range(n):
        chr = choice(all_list)
        result += chr

    return result

# if __name__ == '__main__':
#     print(pass_gen())
#     print(pass_gen(int(argv[1])))