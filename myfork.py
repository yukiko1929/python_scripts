import os

# print('yukiko')
#
# os.fork()
# print('I said I am yukiko')

# print('yukiko')
# retval = os.fork()
# if retval:
#     print('parent process')
# else:
#     print('child process')
#
# print('reunion')


# print('a summer day')
# for i in range(3):
#     retval = os.fork()
#     if not retval:
#         print('hahaha')


import os
import subprocess

def ping(ips):
    ping_ip = subprocess.call('ping -c2 %s &> /dev/null' % ips, shell=True)
    if ping_ip != 0:
        print('%s is down' % ips)
    else:
        print('%s is up' % ips)

if __name__ == '__main__':
    ip_range = ('192.168.4.%s' % i for i in range(5))
    for the_ip in ip_range:
        ip_fork = os.fork()
        if not ip_fork:
            ping(the_ip)
            exit()
