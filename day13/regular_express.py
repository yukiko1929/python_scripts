# website   https://www.baidu.com/?id=1
# [a-z]+:\/\/[a-z]+\.[a-z]+\.[a-z]+\/.+

# identification number  430381199210271948    43038119690815187X
# [0-9]{17}[0-9|X]

# import re
# m = re.search('doo', 'assoonasddooasdoohadoop')
# if m is not None:
#     print(m.group())
#
# regexp1 = '\w+<(.*)>(\d+)<\/(.*)> | <\/\w+>'
# m = re.search(regexp1, 'aa<a>1234</a>')
# if m is not None:
#     print(m.group())
#
# print('*' * 50)
#
# regexp2 = '(foo\w)(\w)'
# m = re.match(regexp2, 'fooasdfoosd')
# if m is not None:
#     print(m.group(1))
#     print(m.groups())
#
# m2 = re.findall(regexp2, 'fooasdfoodsd')
# print(m2)
#
# regexp3 = '(apple)(\d+)'
# m = re.search(regexp3, 'apple12 apple2 apple33333')
# # print('the result of finding all regexp3 is %s' % m)
# print(m.group(1))
# print(m.groups())
#
# regexp4 = 'apple\d{3,}'
# m = [g.group() for g in re.finditer(regexp4, 'apple22 apple1 apple3333')]
# print(m)

# list1 = ['aaa,bbb cccc', 'ddd,eee fff']
# for i in list1:
#     #print(re.split(', |(?= (?:[a-z]{3}))', i))
#     print(re.split(',| ', i))

# def chandler(a,b):
#     def inner(x):
#         return a * x + b
#     return inner
#
# if __name__ == '__main__':
#     func = chandler(6,7)
#     print(func(5))

import re
from random import randrange, choice, randint
from string import ascii_lowercase as lc
from time import ctime

def generate_data():
    with open('./data.txt', 'w') as fobj:
        for i in range(randint)