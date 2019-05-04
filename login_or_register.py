info_dict = {}

# choice = '''0: I am new user
# 1: I have registered already
# 2: quit
# pleased enter your choice(0/1/2):'''

def register():
    name = input('please enter your name:')
    passwd = input('please enter your password:\n')
    if name in info_dict.keys():
        print('the user already existed')
    else:
        info_dict[name] = passwd
        print('register successful')

def login():
    name = input('please enter your name:')
    passwd = input('please enter your password\n:')
    if info_dict.get(name) == passwd:
    # if name in info_dict.keys() and passwd == info_dict[name]:
        print('login successful')
    else:
        print('login failed')

# def quit():
#     print('bye-bye')
#     exit()

choice = '''0: I am new user
1: I have registered already
2: quit
pleased enter your choice(0/1/2):'''

the_dict = {0 : register, 1 : login}

while True:
    sentaku = int(input(choice))
    if sentaku == 2:
        print('bye-bye')
        break

    the_dict[sentaku]()


# while True:
#     sentaku = int(input(choice))
#     if sentaku ==  0:
#         register()
#     elif sentaku == 1:
#         login()
#         break
#     else:
#         print('invalid input')
