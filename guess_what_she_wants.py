#to practice index
import random
all_listed = ['SK-II','a diamond ring','a channel bag','hotpot','travel','a romantic dinner','nothing']
what_she_wants = random.choice(all_listed)
num_trans = '''(0) SK-II
(1) a diamond ring
(2)a channel bag
(3)hotpot
(4)travel
(5)a romantic dinner
(6)nothing
please enter(0-6)'''
ind = int(input(num_trans))
my_guess = all_listed[ind]
print('what she wants: %s, my guess %s' % (what_she_wants,my_guess))
if my_guess == what_she_wants:
    print('bingo')
else:
    print('you know you will be punished')