# teacher's demo
from os import path
from time import strftime
import pickle

ori_data = [['', 0, 0, 10000, '']]
def save(fname):
    how_much = int(input('how much to save:'))
    comment = input('comment:')
    date = strftime('%Y-%m-%d')
    with open(fname, 'rb') as fobj:
        data = pickle.load(fobj)
        delta = data[-1][-2] + how_much
    line = [date, how_much, 0, delta, comment]
    ori_data.append(line)

    with open(fname, 'wb') as fobj:
        pickle.dump(ori_data, fobj)

def spend(fname):
    how_much = int(input('how much to save:'))
    comment = input('comment:')
    date = strftime('%Y-%m-%d')
    with open(fname, 'rb') as fobj:
        data = pickle.load(fobj)
        delta = data[-1][-2] - how_much
    line = [date, 0, how_much, delta, comment]
    ori_data.append(line)

    with open(fname, 'wb') as fobj:
        pickle.dump(ori_data, fobj)

def view(fname):
    with open(fname) as fobj:
        print('-10%s-10%s-10%s-10%s-10%s' % ('date','plus', 'minus', 'sum', 'comment'))
        for line in fobj:
            print( '-10%s-10%s-10%s-10%s-10%s' % (line[0], line[1], line[2], line[3], line[4]))

choice = '''0: add
1: spend
2: query
3: quit
please enter(0/1/2/3):'''

