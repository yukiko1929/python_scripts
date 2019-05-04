import random
all_choices = ['scissor','stone','palm']
com = random.choice(all_choices)
mine = input('please choose among scissor,stone and palm:')
print('computer:%s, my choice:%s' % (com, mine))

if mine == 'scissor':
    if com == 'palm':
        print('you won')
    elif com == 'scissor':
        print('even')
    else:
        print('you are defeated')
elif mine == 'stone':
    if com == 'scissor':
        print('you won')
    elif com == 'stone':
        print('even')
    else:
        print('you are defeated')
else:
    if com == 'stone':
        print('you won')
    elif com == 'palm':
        print('even')
    else:
        print('you are defeated')