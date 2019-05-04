import random
all_choices = ['stone','scissor','palm']
I_win = [['stone','scissor'],['scissor','palm'],['palm','stone']]
com = random.choice(all_choices)
win_count = 0
even_count = 0
fail_count = 0
counter = 0

while counter <= 3:
    counter += 1
    prompt = '''(0)stone
    (1)scissor
    (2)palm
    please enter(0/1/2):'''
    num = int(input(prompt))
    mine = all_choices[num]

#print('computer:%s,mine:%s' % (com,mine))
if (mine,com) in I_win:
    print('you won')
    win_count += 1
elif mine == com:
    print('even')
    even_count += 1
else:
    print('you are defeated')
    fail_count += 1
    counter += 1

if win_count >= 2:
    print('won more than 2 out of 3')
else:
    print('you losed the game')