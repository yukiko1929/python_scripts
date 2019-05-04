import pickle
from time import strftime
from os import path

def spend(fname):
    spend = int(input('how much did you spent:'))
    comment = input('please add comment:')
    date = strftime('%Y-%m-%d %H:%M')
    with open(fname, 'rb') as fobj:
        data = pickle.load(fobj)
    line = [date, spend, 0, int(data[-1][-2])-spend, comment]
    data.append(line)

    with open(fname, 'wb') as fobj:
        pickle.dump(data, fobj)


def save(fname):
    save = int(input('how much did you earn:'))
    comment = input('please add comment:')
    date = strftime('%Y-%m-%d %H:%M')
    with open(fname, 'rb') as fobj:
        data = pickle.load(fobj)
    line = [date, 0, save, int(data[-1][-2])+save, comment]
    data.append(line)
    with open(fname, 'wb') as fobj:
        pickle.dump(data, fobj)


def view(fname):
    with open(fname, 'rb') as fobj:
        data = pickle.load(fobj)

    print('%-20s%-20s%-15s%-15s%-15s' % ('date', 'spend', 'save', 'current_sum', 'comment'))
    for line in data:
        print('%-20s%-20s%-15s%-15s%-15s' % tuple(line))

def menu():
    fname = '/tmp/money_record'
    cmds = {0: spend, 1: save, 2: view}
    choice = '''0:spend
1: save
2: view
3: quit
please enter(0/1/2/3):'''
    if not path.exists(fname):
        date = strftime('%Y-%m-%d %H:%M')
        data = [[date, 0, 0, 100000, 'initial']]
        with open(fname,'wb') as fobj:
            pickle.dump(data, fobj)

    while True:
        sentaku = int(input(choice))
        if sentaku not in [0, 1, 2, 3]:
            print('invalid input')
        elif sentaku == 3:
            print('\nbye-bye')
            break
        cmds[sentaku](fname)

if __name__ == '__main__':
    menu()
