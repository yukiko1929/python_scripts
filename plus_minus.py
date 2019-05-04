from random import randint, choice
# from string import ascii_letters, digits
doing_math = ['plus', 'minus']

def mathmatics():
    # counter = 0
    # while counter < 3:
    #     counter += 1
    numbers = [randint(1,500), randint(1, 500)]
    which_one = choice(doing_math)
    if which_one == 'plus':
        result = numbers[-1] + numbers[-2]
        greet = int(input('%s + %s = :' % (numbers[-1], numbers[-2])))
        if greet == result:
            print('bingo')
        else:
            print('wrong')
    else:
        if numbers[-1] < numbers[-2]:
            result = numbers[-2] - numbers[-1]
            greet = int(input('%s - %s =:' % (numbers[-2], numbers[-1])))
            if greet == result:
                print('bingo')
            else:
                print('wrong')
        else:
            result = numbers[-1] - numbers[-2]
            greet = int(input('%s - %s =:' % (numbers[-1], numbers[-2])))
            if greet == result:
                print('bingo')
            else:
                print('wrong')

def main():
    while True:
        mathmatics()
        ask_him = input('continue or not(y/n):')
        if ask_him == 'n':
            print('\nbye-bye')
            break

main()

