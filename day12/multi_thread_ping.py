# main thread creates working threads
# working threads finish specific tasks
# the difference with os.fork is that multi-thread generate no zombie process
# it exits after finishing tasks
# windows have only multi-thread.

import threading
import time
import subprocess
# def greeting():
#     print('hello yukiko')
#     time.sleep(3)
#     print('done')
#
# if __name__ == '__main__':
#     print('start')
#     t1 = threading.Thread(target=greeting)   # create working thread
#     t1.start()        # start working thread
#     t2 = threading.Thread(target=greeting)
#     t2.start()
#
# def ping_batch(host):
#     rv = subprocess.run('ping -c2 %s > /dev/null' % host, shell=True)
#     if rv:
#         print('%s is down' % host)
#     else:
#         print('%s is up' % host)
#
# if __name__ == '__main__':
#     ip_list = ['192.168.4.%s' % i for i in range(1,10)]
#     #
#     #while counter < length:
#     for ip in ip_list:
#             #for i in range(length - 1):
#         mt = threading.Thread(target=ping_batch, args=(ip,))
#         mt.start()
                #counter += 1
# class MultiThread:
#     def __init__(self, host):
#         self.host = host
#
#     def __call__(self):
#         rv = subprocess.run('ping -c2 %s > /dev/null' % self.host, shell=True)
#         if rv:
#             print('%s is down' % self.host)
#         else:
#             print('%s is up' % self.host)
#
# if __name__ == '__main__':
#     # m = MultiThread()
#     ip_list = ['192.168.4.%s' % i for i in range(1,10)]
#     for ip in ip_list:
#         t = threading.Thread(target=MultiThread(ip))
#         t.start()

import subprocess

class MultiThread:
    def __init__(self, host):
        self.host = host

    def __call__(self):
        rv = subprocess.run('ping -c2 %s > /dev/null' % self.host, shell=True)
        if rv:
            print('%s is down' % self.host)
        else:
            print('%s is up' % self.host)

if __name__ == '__main__':
    ip_list = ['192.168.4.%s' % i for i in range(1,255)]
    for ip in ip_list:
        t = threading.Thread(target=MultiThread(ip))
        t.start()

