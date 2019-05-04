# print('新しいクラスにようこそ')
# name = input('ご名前を入力して下さい：')
# print(name,'さん','ようこそ')

# name = input('名前をご入力ください：')
# print('ようこそ！%s'% (name))

# if 2 > 0:
#     print('2 is larger than 0,yes')
#     print('the statement is true')
#
# name = 'hikaru_yukiko_yukimi'
# if 'yuki' in name:
#     print('yuki is among the names')
#
# print('#' * 50)
#
# if [False]:
#     print('this is not an empty list')
#
# print('#' * 50)
#
# if []:
#     print('this is an empty list')
#
# print('#' * 50)
#
# if ' ':
#     print('this is not an empty string')
#
# atuple = ('kyoto','osaka','nara')
# if 'osaka' in atuple:
#     print('osaka is included in atuple')
#
# print('#' * 50)
#
# alist = {'name':'yukiko','age':25,'city':'osaka'}
# if 'city' in alist:
#     print('name is a key in alist')
#
# if 'country' not in alist:
#     print('the key country is not included in alist')

# import getpass
# name = input('please enter your name:')
# password = getpass.getpass('please enter password:')
# if name == 'bob' and password == '123456':
#     print('login successful')
# else:
#     print('login failed')



# room_reserved = input('please enter the room you want to reserve:')
# how_many = int(input('please enter the amount of your members:'))
# reserve_time = input('please choose the period you time:')
# if room_reserved == '404':
#     print('sorry the room you want to reserve is not available')
# else:
#     if how_many > 10:
#         print('sorry we can\'t handle so many people')
#     else:
#         print('you have successfully reserved')


# number guess

# import random
# number = random.randint(1,10)
# answer = int(input('please enter a number hwich should be larger than 1 but less than 10:'))
# if answer > number:
#     print('get smaller')
# elif answer < number:
#     print('get larger')
# else:
#     print('bingo')

# grade
# marks = int(input('please enter your marks:'))
# if 60 <= marks < 70:
#     print('you just escaped from flunking the test')
# elif 80 >= marks >= 70:
#     print('not so bad')
# elif 90 >= marks >= 80:
#     print('good')
# elif marks >= 90:
#     print('wonderful')
# else:
#     print('got flunk, you loser')

# a simpler grade
# marks = int(input('please enter your score:'))
# if marks > 90:
#     print('excellent')
# elif marks > 80:
#     print ('good')
# elif marks > 70:
#     print('not so bad')
# elif marks > 60:
#     print('lucky')
# else:
#     print('flunk')

# import getpass
# industry = input('please enter the industry you are in:')
# company = input('please enter the company you are working for:')
# com_list = ['Tencent','Baidu','Huawei','JD']
# department = input('please enter the department you are in:')
# age = int(input('please enter your age:'))
# salary = float(getpass.getpass('please enter your salary:'))
# if industry == 'Internet' and company == 'Tencent' and age < 35:
#     print('young and able')
# elif department == 'development' and salary > 100000.88:
#     print('young,able and rich. ignore his bald head')
# else:
#     print('Thanks for your participation. Looking forward to cooperate with you in Tecent')

# if industry == 'internet' and company in com_list:
#     print()


# a = 100
# b = 200
# if a < b:
#     s = b
# else:
#     s = a
#
# # a simpler one
# s = b if a< b else b

##version 1
# import random
# com = random.choice(['scissor','stone','palm'])
# mine = input('please choose from scissor,stone and palm:')
# if mine not in ['stone','scissor','palm']:
#     print('haha')
#     exit
# if mine == 'scissor':
#     if com == 'stone':
#         print('computer wins')
#     elif com == 'plam':
#         print('you beat computer')
#     else:
#         print('odd')
# if mine == 'stone':
#     if com == 'scissor':
#         print('you beat computer')
#     elif com == 'palm':
#         print('defeated')
#     else:
#         print('odd')
# if mine == 'palm':
#     if com == 'scissor':
#         print('defeated')
#     elif com == 'palm':
#         print('odd')
#     else:
#         print('you beat computer')

# #version 2: a simpler one
# import random
# com = random.choice(['scissor','stone','palm'])
# mine = input('please choose from scissor,stone and palm:')
# if (mine =='scissor' and com == 'palm') or (mine == 'stone' and com == 'scissor') or (mine == 'palm' and com == 'stone'):
#     print('\033[31;1myou win\033[0m')
# elif mine == com:
#     print('\033[32;1meven\033[0m')
# else:
#     print('\033[31;1myou are defeated\033[0m')
#
#
# ##version 3: to use list
# import random
# all_choice = ['scissor','stone','palm']
# win_list = [['scissor','palm'],['stone','scissor'],['palm','stone']]
# com = random.choice(all_choice)
# mine = input('please choose from scissor,stone and palm:')
# print('my choice: %s, computer choose %s' % (mine, com))
# if [mine,com] in win_list:
#     print('\033[32;1myou win\033[0m')
# elif mine == com:
#     print('\033[31;1meven\033[0m')
# else:
#     print('\033[32;1myou are defeated\033[0m')


# #version 4: to improve user experience
# import random
# all_choices = ['stone','scissor','palm']
# win_list = [['scissor','palm'],['stone','scissor'],['palm','stone']]
# prompt = '''(0) scissor
# (1) stone
# (2) palm
# please choose(0/1/2)'''
# com = random.choice(all_choices)
# ind = int(input(prompt))
# mine = all_choices[ind]
# if [mine,com] in win_list:
#     print('\033[31;1myou win!\033[0m')
# elif mine == com:
#     print('\033[32;1meven\033[0m')
# else:
#     print('\033[31;1myou lose!\033[0m')



# version 4: another version which is a little complexed than last one
# import random
# all_choice = ['scissor','stone','palm']
# com = random.choice(all_choice)
# mine = input('please enter your choice(scissor,stone or palm):')
# if mine == 'scissor':
#     if com == 'scissor':
#         print('even')
#     elif
#
# elif mine == 'stone':
#
# else:


# alist = ['yukiko','miho','']


# # while loop
# result = 0
# counter =1
#
# while counter <= 100:
#     result += counter
#     counter += 1
#
# print(result)
#
# # while + break
# import random
# num = random.randint(1,100)
#
# while True:
#     my_num = int(input('please enter your number:'))
#     if my_num > num:
#         print('it should be smaller')
#     elif my_num < num:
#         print('it should be larger')
#     else:
#         print('bingo')
#         break

# while + continue
result = 0
counter = 0

while counter < 100:
    counter += 1
    if counter % 2:
        continue
    result += counter
print(result)










