my_stack = []

def view():
    if my_stack:
        print(my_stack)
    else:
        print('an empty stack')

def push():
    content = input('please enter the content:')
    my_stack.append(content)

def pop():
    if my_stack:
        print(my_stack.pop())
    else:
        print('an empty stack')

choice = '''0: view
1: push
2: pop
3: quit
please enter(0/1/2/3):'''

while True:
    sentaku = int(input(choice))
    if sentaku == 0:
        view()
    elif sentaku == 1:
        push()
    elif sentaku == 2:
        pop()
    else:
        print('bye-bye')
        break