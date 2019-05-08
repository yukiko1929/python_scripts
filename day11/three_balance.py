from random import choice

# def three_game():
#     options  = ('scissor', 'stone', 'palm')
#     #com = choice(options)
#     win_list = [('scissor', 'palm'), ('stone', 'scissor'), ('palm', 'stone')]
#
#     prompt = '''0: scissor
# 1: stone
# 2: palm
# 3: quit
# please input(0/1/2/3):'''
#
#     com = choice(options)
#     my = input(input(prompt))
#     if (my, com) in win_list:
#         print('you won')
#     elif my == com:
#         print('even')
#     else:
#         print('you lose')


def three_game():
    options = ('scissor', 'stone', 'palm')
    win_list = [('0','palm'), ('1', 'scissor'), ('2','stone')]
    sen_dict = {'0':'scissor', '1':'stone', '2':'palm'}
    propmt = '''0:scissor
1:stone
2:palm
please choose(0/1/2):'''
    com = choice(options)
    my = input(propmt)
    real_my = sen_dict[my]
    if (my, com) in win_list:
        print('you won')
    elif real_my == com:
        print('even')
    else:
        print('\033[1;33myou lose\033[0m')
        print('com:%s, yours: %s' % (com, real_my))

def menu():
    while True:
        three_game()
        ask_him = input('continue or not(y/n):')
        if ask_him not in 'yYnN':
            print('invalid input')
            break
        elif ask_him in 'nN' or ask_him == 'quit':
            print('bye-bye')
            break
        else:
            continue

if __name__ == '__main__':
    menu()

