import random
all_choices = ['stone','scissor','palm']
I_win = [['stone','scissor'],['scissor','palm'],['palm','stone']]
com = random.choice(all_choices)
prompt = '''(0)stone
(1)scissor
(2)palm
please enter(0/1/2):'''
num = int(input(prompt))
mine = all_choices[num]

print('computer:%s,mine:%s' % (com,mine))

if (mine,com) in I_win:
    print('you won')
elif mine == com:
    print('even')
else:
    print('you are defeated')
