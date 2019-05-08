import re

def rmb_to_usd():
    amount = int(input('amount:'))
    result = amount / 6.72
    print('%.2f' % result)

def usd_to_rmb():
    amount = int(input('amount:'))
    result = amount * 6.72
    print('%.2f' % result)