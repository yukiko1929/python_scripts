import random
num = random.randint(1,50)

while True:
    my_num = int(input('please have a guess:'))
    if my_num > num:
        print('get a smaller one')
    elif my_num < num:
        print('get a larger one')
    else:
        print('bingo')
        break