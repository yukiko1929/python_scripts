from random import randint
from string import ascii_letters, digits

collection = ascii_letters + digits

user_input = input('content:')
# for element in user_input:
#     valid_chars = filter(lambda x:x in collection, element)
#     print(valid_chars)
str_list = list(user_input)
#print(str_list)
valid_chars = filter(lambda x: x in collection, str_list)
print(list(valid_chars))
