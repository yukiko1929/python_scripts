from random import choice

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
    x = 0
    y = 0
    z = 0
    if (my, com) in win_list:
        print('you won')
        x += 1
    elif real_my == com:
        print('even')
        y += 1
    else:
        print('\033[1;33myou lose\033[0m')
        print('com:%s, yours: %s' % (com, real_my))
        z += 1
    return 'win: %s, even: %s, loose: %s' % (x, y, z)


def menu():
    # tries = int(input('how many rounds do you want to play(0-100):'))
    # counter = 0
    while True:
        tries = int(input('how many rounds do you want to play(0-100):'))
        counter = 0
        while counter < tries:
            three_game()
            counter += 1
        print(three_game())

        ask_him = input('continue or not(y/n):')
        if ask_him == 'Yy':
            continue
        elif ask_him in 'Nn' or ask_him == 'quit':
            print('bye-bye')
            break
        else:
            break

        # if ask_him not in 'yYnN':
        #     print('invalid input')
        #     break
        # elif ask_him in 'nN' or ask_him == 'quit':
        #     print('bye-bye')
        #     break
        # else:
        #     continue

if __name__ == '__main__':
    menu()