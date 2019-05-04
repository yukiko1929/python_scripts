# list generation
#
# print([1 + 5 for i in range(6)])
# print([100 + i for i in range(7)])


# host_num = [100 + i for i in range(1,155)]
# for i in host_num:
#     print('192.168.1.%s' % i)
# # print('192.168.1.%s' % host_num)
#
# #print('192.168.1.%s' % i 100 + i for i in range(1.155))

result = 0
for i in range(1,101,2):
    result += i
print(result)

result = 0
for i in range(1,101):
    result += i
print(result)

