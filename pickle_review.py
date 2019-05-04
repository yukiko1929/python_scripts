from os import path
import pickle
from time import strftime

def save(file):
    how_much = int(input('how much to save:'))
    comment = input('add comment:')
    date = strftime('%Y-%m-%d')
    with open(file, 'rb') as fobj:
        data = pickle.load(fobj)
    line = [date, how_much, 0, data[-1][-2] + how_much, comment]
    data.append(line)
    with open(file, 'wb') as fobj:
        pickle.dump(data, fobj)

def spend(file):
    how_much = int(input('how much spent:'))
    comment = input('add comment:')
    date = strftime('%Y-%m-%d')
    with open(file, 'rb') as fobj:
        data = pickle.load(fobj)
    line = [date, 0, how_much, data[-1][-2] - how_much, comment]
    data.append(line)
    with open(file, 'wb') as fobj:
        pickle.dump(data, fobj)

def query(file):
    with open(file,'rb') as fobj:
        data = pickle.load(fobj)
    print('%-20s%-20s%-15s%-15s%-20s' % ('date', 'save', 'spend', 'sum', 'comment'))
    for line in data:
        print('%-20s%-20s%-15s%-15s%-20s' % tuple(line))

def main_pro():
    file = '/tmp/monmanage.txt'
    date = strftime('%Y-%m-%d')
    data = [[date, 0, 0, 100000, 'initial']]
    cmds = {0: save, 1: spend, 2: query}
    if not path.exists(file):
        with open(file, 'wb') as fobj:
            pickle.dump(data, fobj)

    choices = '''0:save
    1: spend
    2: query
    3: quit
    please enter(0/1/2/3):'''

    while True:
        sentaku = int(input(choices))
        if sentaku not in [0,1,2,3]:
            print('invalid input')
        elif sentaku == 3:
            print('bye-bye')
        else:
            cmds[sentaku](file)

if __name__ == '__main__':
    main_pro()