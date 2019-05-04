from random import randint
my_list = [randint(1,100) for i in range(10)]
print(my_list)
print(my_list.append(99))
#print(my_list.index(5))
print(my_list.insert(5, 100))
print(my_list.pop(6))

blist = my_list.copy()
print('blist is : %s' % blist)

clist =  my_list
print('clist is : %s ' % clist)

my_list.clear()
print('after my list is cleared, blist is : % s' % blist)
print('after my list was cleared, clist is : %s' % clist)





