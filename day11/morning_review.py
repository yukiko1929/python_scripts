from random import randint
from random import choice
from string import ascii_letters
from string import digits
import subprocess

all_available = ascii_letters + digits

def passgen():
    ori_pass = [choice(all_available) for i in range(6)]
    passwd = ','.join(ori_pass)
    print(passwd)

if __name__ == '__main__':
    passgen()