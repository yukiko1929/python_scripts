userinfo = {}
from string import ascii_letters, digits
import getpass
from sys import argv

def register():
        name = input('username:')
        passwd = input('please set a password:\n')
        if name in userinfo.keys():
            print('sorry, this username already existed, please try another')
        # midway = enumerate(passwd)
        # for char in enumerate(passwd):
        #     if char not in ascii_letters + digits:
        #         print('the password should be characters and digits')
        #if name not in userinfo.keys() and passwd in ascii_letters + digits:
        else:
            userinfo[name] = passwd


def login():
    name = input('username:')
    passwd = input('password:\n')
    if userinfo.get(name) == passwd:
        print('login successful')
    else:
        print('login failed')

def record(fname):
    data = str(userinfo)
    with open(fname, 'w') as reobj:
        reobj.write(data)

choice = '''0: register (if you are a new user)
1: login
2: quit
please enter(0/1/2):'''

while True:
    sentaku = int(input(choice))
    if sentaku == 0:
        register()
        record(argv[1])
    elif sentaku == 1:
        login()
    else:
        print('bye-bye')
        break