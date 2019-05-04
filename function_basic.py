# 関数に関する基本的な知識
# def sentence(name, department, years):
#     print('%s is at %s for %s years' % (name, department, years))

# print(sentence())
#TypeError: sentence() missing 3 required positional arguments: 'name', 'department', and 'years'

# print(sentence('yuki'))

# print(sentence('yuki', 'MP', '5'))
# print(sentence('yuki', 'mass production', '5', 'yukiko'))
# print(sentence('miho', name='yuki', years='5', department='RD')) # got multiple values

# # print(sentence(years='5', department='RD', name='yuki'))
# print(sentence(years='5', 'RD', name='yuiko'))
#
# def func1(*args):
#     print(args)
#
# def func2(**kwargs):
#     print(kwargs)
#
# if __name__ == '__main__':
#     print(func1('yuki',23,'tokyo'))
#     print(func2(name = 'tom', age = 39, city = 'tokyo'))
#     print(func1())
#     print(func2())

def info(name, age):
    print('%s : %s' % (name, age))

print(info(**{'name':'yuki', 'age':25}))
print(info(name='yuki', age=25))