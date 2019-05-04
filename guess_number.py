import random
num = random.randint(1,100)

counter = 1
while counter < 5:
    my_guess = int(input('please enter a number between 1 and 100:'))
    if my_guess > num:
        print('get a smaller one')
    elif my_guess < num:
        print('get a larger one')
    else:
        print('bingo')
        break
        counter += 1