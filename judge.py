import keyword
from string import digits, ascii_letters

user_input = input('please input:')
input_transfer = list(user_input)
for ind,char in enumerate(input_transfer):
    if char in keyword.kwlist:
        print('sorry! your identification include keyword %s' % char)
    else:
        if char not in digits+ascii_letters+'_':
            print('sorry! illegal input')
            print('the %s: %s is illegal' % (ind + 1, char))
