from random import choice
all_list = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKZXCVBNM'
result = ''

for i in range(100):
    chr = choice(all_list)
    result += chr

print(result)
