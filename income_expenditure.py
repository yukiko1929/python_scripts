# a temporary one

import pickle
from time import ctime

# original = 100000
my_money = [['', 100000, '']]
# current = int((my_money[-1])[1])

def spend_record():
    how_much = int(input('please enter the money you spent:'))
    comment = input('please add a comment:')
    current = int((my_money[-1])[1])
    c_money = [ ctime(), current - how_much, comment ]
    # with open('/tmp/money.txt', 'rb') as mobj:
         #so_far = my_money.append(c_money)
       # pickle.dump(so_far, mobj)
    my_money.append(c_money)

def income_record():
    how_much = int(input('please enter how much money you are to add:'))
    comment = input('please add a comment:')
    current = int((my_money[-1])[1])
    now_money = [ctime(), current + how_much, comment]
    #with open('/tmp/money.txt', 'rb') as mobj:
        # so_far = my_money.append(now_money)
        #pickle.dump(so_far, mobj)
    my_money.append(now_money)


def view():
    # reader = open('/tmp/money.txt', 'r')
    # content = pickle.load(reader)
    # print(content)
    print(my_money)

menu = '''0:add
1:spend
2:view
3:quit
please enter your choice(0/1/2/3)'''

while True:
    sentaku = int(input(menu))
    if sentaku == 0:
        income_record()
    elif sentaku == 1:
        spend_record()
    elif sentaku == 2:
        view()
    else:
        print('bye-bye')
        break
