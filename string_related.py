# from string import *
#
# my_string = input('please enter the string:')
# length = len(my_string)
# print(length)
# for ind, chars in enumerate(my_string):
#     x = 0
#     y = 0
#     if chars == ' ':
#         #print('%s is an empty string' %(ind + 1))
#         x += 1
#     else:
#         y += 1
# print(x, y, x+y)


whitesps = '\s'

def rmlsps(my_string):
    for i in range(len(my_string)):
        if my_string[i] not in whitesps:
            return my_string[i:]
    else:
        return ''

if __name__ == '__main__':
    print(rmlsps('   \my yukiko   '))








