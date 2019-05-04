# import os
# import subprocess
#
# def batch_ping(host):
#     result = subprocess.call('ping -c2 %s' % host, shell = True)
#     if result:
#         print('%s is down' % host)
#     else:
#         print('%s is up' % host)
#
# if __name__ == '__main__':
#     ip_addrs = ['192.168.4.%s' % i for i in range(1,10)]
#     for ip in ip_addrs:
#         retval = os.fork()
#         if not retval:
#             batch_ping(ip)
#             exit()


import subprocess
import os

def ping_batch(host):
    rc = subprocess.call('ping -c2 %s &> /dev/null' % host, shell=True)
    if rc:
        print('%s : down' % host)
    else:
        print('%s : up' % host)

if __name__ == '__main__':
    ips = ('192.168.4.%s' % i for i in range(1,20))
    for ip in ips:
        pid = os.fork()
        if not pid:
            ping_batch(ip)
            exit()