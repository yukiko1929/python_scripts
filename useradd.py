import subprocess
from string import ascii_letters, digits
from random import choice
from passgen import pass_gen

import sys

# pass_source = ascii_letters + digits

def add_user(user,passwd,fname):
    info = '''user info:
    username:%s
    password:%s
    ''' % (user, passwd)
    subprocess.run('useradd %s' % user, shell = True)
    subprocess.run('echo %s | passwd --stdin %s' % (passwd, user), shell = True)

    with open(fname,'a') as fobj:
        fobj.write(info)

if __name__ == '__main__':
    username = sys.argv[1]
    pw = pass_gen()
    add_user(username, pw, sys.argv[2])
# def pass_gen():
#
#
# def info_file(info,userna,pword):
#     with  open(info,'w') as user_info:
#         user_info.write(userna,pword)
#
# uname = add_user(sys.argv[1])
# passwo = pass_gen()
# info_file(sys.argv[2],uname,passwo)


