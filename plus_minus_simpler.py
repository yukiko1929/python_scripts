from random import randint, choice

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def doing_math():
    cmds = {'+': add, '-': sub}
    my_num = [randint(1,500) for i in range(2)]
    my_num.sort(reverse=True)
    opera = choice('+-*')
    result = cmds[opera](**my_num)
    # if opera == '+':
    #     result = my_num[0] + my_num[1]
    # elif opera == '-':
    #     result = my_num[0] - my_num[1]
    # else:
    #     result = my_num[0] * my_num[1]
    counter = 0
    reminder = '%s %s %s = ' % (my_num[0], opera, my_num[1])
    while True:
        greet = input('%s %s %s = ' % (my_num[0], opera, my_num[1]))
        try:
            answer = int(input('please enter your answer'))
        except (KeyboardInterrupt, EOFError):  #include all possible errors
         #   print('\nbye bye')
            continue

        if answer == result:
            print('bingo')
            break
        else:
            print('wrong')
            counter += 1
    # else:
    #     print('%s%s' % (reminder, result))


def main_game():
    while True:
       # reminder = '%s %s %s = ' % (my_num[0], opera, my_num[1])
        doing_math()
        try:
            ask_him  = input('continue or not(y/n):')
        except IndexError:
            continue
        except KeyboardInterrupt:
            print('bye bye')
        except EOFError:
            print('invalid input')
        except ValueError:
            print('invalid value')

        if ask_him == 'n':
            print('\nbye bye')
            break

main_game()
