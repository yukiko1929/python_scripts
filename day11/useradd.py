from random import randint
from random import choice
from string import ascii_letters
from string import digits
import subprocess

all_available = ascii_letters + digits

# def passgen():
#     ori_pass = [choice(all_available) for i in range(6)]
#     passwd = ','.join(ori_pass)
#
# def useradd():
#     name = input('username:')
#     passwd = passgen()
#     subprocess.run('useradd %s' % name, shell=True)
#     subprocess.run('echo %s | passwd --stdin %s' % (passwd,name))
def passgen(n=8):
    result = ''
    for i in range(n):
        char = choice(all_available)
        result += char
    return result

def usradd():
    name = input('username:')
    passwd = passgen()
    subprocess.run('useradd %s' % name, shell=True)
    subprocess.run('echo %s | passwd --stdin %s' % (passwd, name))

if __name__ == '__main__':
    print(passgen())
    print(passgen(6))