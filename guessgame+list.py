import random
all_list = ['stone','scissor','palm']
I_win = [['stone','scissor'],['scissor','palm'],['palm','stone']]
com = random.choice(all_list)
my_choice = input('please choose among stone, scissor and palm:')
print('computer:%s,my choice:%s' % (com,my_choice))
if (my_choice,com) in I_win:
    print('you won')
elif my_choice == com:
    print('even')
else:
    print('you are defeated')