import random
all_list = ['scissor','stone','palm']
I_win = [['scissor','palm'],['stone','scissor'],['palm','stone']]

x = 0
y = 0
counter = 0

while counter < 3:
    counter += 1
    com = random.choice(all_list)
    prompt = '''(0)scissor
    (1) stone
    (2)palm
    please choose(0/1/2):'''
    ind = int(input(prompt))
    my_choice = all_list[ind]
    print('my choice:%s.computer:%s' % (my_choice,com))
    if (my_choice,com) in I_win:
        print('you won')
        x += 1
    elif my_choice == com:
        print('even')
    else:
        print('defeated')

print('finished')
if x >= 2:
    print('you won the game')
else:
    print('sorry you lose the game')


# a improved version

