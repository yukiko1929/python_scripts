import keyword
#from sys import argv
import sys
from string import digits, ascii_letters

first_cha = ascii_letters + '_'
other_cha = first_cha + digits

def check_idt(iden):
    if keyword.iskeyword(iden):
        return 'sorry! %s is a keyword' % iden

    if iden[0] not in first_cha:
        return 'sorry! the fisrt character is illegal'

    for ind, chr in enumerate(iden):
        if chr not in other_cha:
            return 'the %s: %s is illegal' % (ind + 1, chr)

    return 'legal input ^_^' % iden

if __name__ == '__main__':
    print(check_idt(sys.argv[1]))


