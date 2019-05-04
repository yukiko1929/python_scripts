# from random import randint, choice
# ops = '+-'
# def calculation():
#     nums = [randint(1,1000) for i in range(2)]
#     nums.sort(reverse=True)
#     ope = choice(ops)
#     if ope == '+':
#         result = sum(nums)
#     else:
#         result = nums[0] - nums[1]
#     while True:
#         greet = int(input('%s%s%s = :' % (nums[0], ope, nums[1])))
#         if greet == result:
#             print('bingo')
#             break
#         else:
#             print('wrong')
#
#
# def my_main():
#     while True:
#         calculation()
#         ask_him = input('continue or not(y/n):')
#         if ask_him == 'n':
#             break
#
# my_main()

from random import randint, choice
ops = '+-'
def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def calculate():
    while True:
        nums = [randint(1, 1000) for i in range(2)]
        nums.sort(reverse=True)
        ope = choice(ops)
        cmds = {'+': plus, '-': minus}
        result = cmds[ope](*nums)
        greet = int(input('%s%s%s = :' % (nums[0], ope, nums[1])))
        if greet == result:
            print('bingo')
        else:
            print('wrong')

def my_main():
    while True:
        calculate()
        try:
            ask_him = input('continue or not(n/y):')
        except (KeyboardInterrupt, EOFError):
            continue
        except ValueError:
            print('invalid value')

        if ask_him == 'n':
            print('\nbye-bye')
            break

my_main()