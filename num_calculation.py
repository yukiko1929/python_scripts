from random import randint
from random import choice

def num_cal():
    opera = choice('-+')
    cmds = {'-':lambda x,y: x - y, '+': lambda x,y:x - y}
    ori_nums = [randint(1,500), randint(1,800)]
    ori_nums.sort(reverse=True)
    result = cmds[opera](*ori_nums)
    prompt = '%s %s %s =:' % (ori_nums[0], opera, ori_nums[1])
    counter = 0

    while counter < 3:
        try:
            answer = int(input(prompt))
        except:
            print()
            continue

        if answer == result:
            print('bingo')
            break
        print('wrong')
        counter += 1
    else:
        print('%s%s' % (prompt, result))

def main():
    while True:
        num_cal()
        try:
            yn = input('continue or not(y/n)?').strip()[0]
        except IndexError:
            continue
        except KeyboardInterrupt:
            yn = 'n'
        except EOFError:
            yn = 'n'

        if yn in 'nN':
            print('/nBye-bye')
            break

if __name__ == '__main__':
    main()