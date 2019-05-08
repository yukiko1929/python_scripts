# from keyword import kwlist
# from string import ascii_letters
# from string import digits
#
# user_string = input('please enter your id:')
# if user_string in kwlist:
#     print('sorry, the id is already existed')
#     exit(1)
# else:
#     for ind,char in enumerate(user_string):
#         if char not in ascii_letters + digits + '_':
#             print('%s:%s is illegal' % (ind + 1,char))

from string import ascii_letters
from string import digits
import subprocess
import pickle
from sys import argv

userdb = {}

def register():
    name = input('username:')
    passwd = input('password:')
    if name in userdb.keys():
        print('sorry the username %s is already used' % name)
    elif len(passwd) < 6:
        print('get a more complexed password for the security of your account')
    else:
        print('account created successfully')
        userdb[name] = passwd
    # with open(recordfile, 'a') as fobj:
    #     #pickle.dump(fobj, userdb)
    #     fobj.write(userdb)

def login():
    name = input('username:')
    passwd = input('password:')
    #if name == userdb.get(name):
    if name == userdb[name]:
        print('login successful')
    else:
        print('login failed')

def query():
    print(userdb)

def menu():
    cmds = {0:register, 1:login, 2:query}
    options = '''0: register
1: login
2: query
3: quit
please enter(0/1/2/3):'''

    while True:
        sentaku = int(input(options))
        if sentaku not in [0,1,2,3]:
            print('invalid input. please choose among 0,1,2,3')
        elif sentaku == 0:
            register()
        elif sentaku == 1:
            login()
        elif sentaku == 2:
            query()
        else:
            print('bye-bye')
            break

if __name__ == '__main__':
    # file = argv[1]
    menu()