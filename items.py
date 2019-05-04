alist = ['amami','bukiko','cikiko','daisuke']

for i in range(4):
    print('%s: %s' % (i, alist[i]))

print('*' * 50)

for i in range(len(alist)):
    print('%s: %s' % (i, alist[i]))

print('*' * 50)

for items in enumerate(alist):
    print('%s: %s' % items)

print('*' * 50)

for ind,name in enumerate(alist):
    print('%s: %s' % (ind, name))

re_list = reversed(alist)
print(re_list)