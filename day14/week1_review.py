# 0o --- 8; 0x --- 16; 0b --- 2
# from de to others
# data = 1000
# result1 = bin(data)
# result2 = hex(data)
# result3 = oct(data)
# print(result1)
# print(result2)
# print(result3)

# from others to de
# print(int('ff',16))
# print(int('1111010', 2))

# result1 = hex(0b101)
# print(result1)

# import socket
# import struct
#
# def ip2hex(ip):
#     return hex(struct.unpack("!|", socket.inet_aton(ip)))[0]
#
# if __name__ == '__main__':
#     ip_addr = '192.168.1.221'
#     resultfi = ip2hex(ip_addr)
#     print(resultfi)

# fobj = open('/mnt/capture')
# result1 = fobj.readline()
# result2 = fobj.readline()
# result3 = fobj.tell()
# print(result1)
# print(result2)
# print(result3)

# print(__name__)
#
# from keyword import kwlist
#
# for items in kwlist:
#     print(items)

# from string import ascii_letters, digits
#
# firstchar = ascii_letters
# from_second = ascii_letters + digits
#
# def judge_char():
#     user_con = input('content:')
#     for sin in list(user_con):
#        if sin[0] not in firstchar:
#              print('illegal first character')
#
#     for ind, char in enumerate(user_con):
#         if char not in from_second:
#              print('%s:%s illegal character' % (ind + 1, char))

    # for sin in list(user_con):
    #     for ind, char in enumerate(user_con):
    #         if sin[0] not in firstchar:
    #             print('illegal first character')
    #         elif char not in from_second:
    #             print('%s:%s illegal character' % (ind + 1, char))
    #         else:
    #             print('created successfully')

# if __name__ == '__main__':
#     judge_char()


# format_related contents

form1 = 'my name is {},{} years old'.format('yukiko',99)
# form2 = 'my name is {name}, {age} years old'.format({'name':'yukiko', 'age':99})
form3 = 'my name is {0[0]},{0[1]} years old'.format(['yukiko',99])
print(form1)
# print(form2)
print(form3)