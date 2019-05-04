from random import randint, choice

def doing_math():
    cmds = {'+': lambda x, y : x + y, '-': lambda x, y: x - y}   # further simplify
    my_num = [randint(1,500) for i in range(2)]
    my_num.sort(reverse=True)
    opera = choice('+-*')
    result = cmds[opera](*my_num)

