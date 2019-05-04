# use else in while loop

import random
answer = random.randint(1,50)
counter = 0

while counter < 5:
    counter += 1
    guess = int(input('please enter a number between 1 and 50:'))
    if guess < answer:
        print('get a bigger one')
    elif guess > answer:
        print('get a smaller one')
    else:
        print('bingo')
        break
else:
    print('the answer is %s' % answer)