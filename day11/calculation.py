from random import randint
from random import choice

# def plus(x, y):
#     return x + y
#
# def minus(x, y):
#     return  x - y

def calculation():
    ops = choice('-+')
    nums = [randint(1,500) for i in range(2)]
    nums.sort(reverse=True)

    prompt = '%s %s %s = :' % (nums[0], ops, nums[1])
    # if ops == '+':
    #     result = sum(nums)
    # else:
    #     result = nums[0] - nums[1]
    cmds = {'-': lambda x, y: x - y, '+': lambda x, y: x + y}
    result = cmds[ops](*nums)

    # try:
    answer  = int(input(prompt))
    # except ValueError:
    #     print('invlid input. please input a number')
    if answer == result:
        print('bingo')
    else:
        print('wrong')

if __name__ == '__main__':

    while True:
        calculation()
        try:
            ask_him = input('continue or not(n/y):')
        except (KeyboardInterrupt, EOFError):
            print('')
            continue
        if ask_him in 'nN' or ask_him == 'quit':
            break
        else:
            continue