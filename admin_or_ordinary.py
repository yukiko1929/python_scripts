from string import ascii_letters, digits
import getpass

ordinary_user = {}
admin = {'admin':'AdMin123.'}

def user_chk():
    name = input('please entee your name:')
    passwd = input('please enter password:')
    if name == 'admin' and passwd == admin.get(admin):
        print('------welcome to the system, administrator!------')
    else:
        print('------sorry, you have no access------')

def register():
    print('------now you are going to register an account, my friend!------')
    name = input('please enter your name:')
    passwd = input('please enter a password')
    if name not in ordinary_user.keys():
        ordinary_user[name] == passwd
    else:
        print('sorry, the user already existed')

def login():
    name = input('please enter your name:')
    passwd = getpass.getpass('please enter your password:')
    if passwd == ordinary_user.get(name):
        print('login successful')
    else:
        print('login failed')

def remove_user():
    name = input('please enter the user you want to delete:')

choice0 = '''you are 
0: administrator
1: '''

choice1 = '''0:register
1: login
2: quit
please enter(0/1/2)'''

choice2 = '''0: login
1: view database
2: remove user
3: quit
please enter(0/1/2/3)'''

while True:
    user_chk()
