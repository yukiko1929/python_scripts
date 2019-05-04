# my_stack = []
#
#     #choice = input('input a number(0 for view, 1 for push, 2 for pop, 3 for quit):')
# menu = '''choices:
# (0) to view the stack
# (1) to push into stack
# (2) to pop an element
# (3) quit
# please input(0/1/2/3)'''
#
# def view_stack():
#     print(my_stack)
#
# def push_into_stack():
#     push = input('please input the content you want to push into the stack:')
#     my_stack.insert(0,push)
#
# def pop_stack():
#     print(my_stack.pop(0))
#
# while True:
#     #choice = input(menu).strip()[0]
#     choice = int(input(menu))
#     if choice not in [0,1,2,3]:
#         print('invalid input, try again')
#         continue
#     if choice == 0:
#         view_stack()
#     elif choice == 1:
#         push_into_stack()
#     elif choice == 2:
#         pop_stack()
#     else:
#         print('bye-bye')
#         break
#
# # to improve the script by adding if judgement
# the_stack = []
# sentaku = '''0: to view the stack
# 1: to push into the stack
# 2: to pop from the stack
# 3: to quit
# please enter(0/1/2/3):'''
#
# def view_stack():
#     print(the_stack)
#
# def push_into():
#     push_con = input('please enter your content:')
#     if push_con:
#         the_stack.append(push_con)
#     else:
#         print('please input something')
#
# def pop_from():
#     if the_stack:
#         print(the_stack.pop())
#     else:
#         print('empty stack')
#
# while True:
#     choice = int(input(sentaku))
#     if choice not in range(4):
#         print('invalid input')
#         continue
#     if choice == 0:
#         view_stack()
#     elif choice == 1:
#         push_into()
#     elif choice == 2:
#         pop_from()
#     else:
#         print('bye-bye')
#         break


#さらに改善したら
the_stack = []

def view():
    print(the_stack)

def push():
    content = input('please enter your content:')
    if content:
        the_stack.append(content)
    else:
        print('empty input')

def pop():
    print(the_stack.pop())

#def show_menu():
mydic = {0: view, 1: push, 2: pop}
sentaku = '''0: view_stack
1: push
2: pop
3: exit
please enter(0/1/2/3):'''

while True:
    choice  = int(input(sentaku))
    if choice == 3:
        print('bye-bye')
        break

    mydic[choice]()
