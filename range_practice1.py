# to practice range

name = input('please enter your name:')
first_num = int(input('first number:'))
second_num = int(input('second number:'))
counter = 0

for i in range(8):
    starting = [first_num, second_num]
    counter += 1
    if first_num > second_num:
        starting.append(starting[-2] - starting[-1])
    else:
        starting.append(starting[-1] - starting[-2])

num = int(input('length:'))
print(starting)