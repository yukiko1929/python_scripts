import os
import sys
from string import ascii_letters, digits

file_char = ascii_letters + digits
first_char = ascii_letters + '_'
other_char = first_char + digits

def chk_fexit(filename):
    while True:
        filename = input('input a filename:')
        if os.path.exists(filename):
            print('%s already exist' % filename)
        else:
            break
        return filename

def chk_fname()
