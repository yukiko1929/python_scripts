from string import ascii_letters, digits
#from sys import argv
import sys
from random import choice
import subprocess


source = ascii_letters + digits

def pass_gen(n=6):
    for i in range(n):
        passwd = str()
        single = choice(source)
        passwd = passwd + single
    return passwd

def add_user(namae, pss):
    subprocess.run('useradd %s' % namae, shell = True)
    subprocess.run('echo %s | passwd --stdin %s' % (namae, pss), shell = True)

def info_file(uname,pswd,fname):
    with open(fname, 'a') as fobj:
        fobj.write('user: %s --- password: %s' % (uname, pswd))

if __name__ == '__main__':
    pwd = pass_gen(sys.argv[2])
    add_user(sys.argv[1],pwd)
    info_file(sys.argv[1], pwd, sys.argv[3])