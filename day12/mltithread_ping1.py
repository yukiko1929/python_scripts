import threading
import time
import os
import subprocess

def ping_batch(host):
    rv = subprocess.run('ping -c2 -w1 %s > /dev/null' % host, shell=True)
    if rv:
        print('%s is down' % host)
    else:
        print('%s is up' % host)

if __name__ == '__main__':
    ip_list = ['192.168.4.%s' % i for i in range(10,51)]

    start1 = time.time()
    for ip in ip_list:
        ping_batch(ip)
    end1 = time.time()
    print(end1 - start1)

    start2 = time.time()
    for ip in ip_list:
        retval = os.fork()
        if not retval:
            ping_batch(ip)
            exit()
    for i in range(40):
        os.waitpid(-1, 0)
    end2 = time.time()
    print(end2 - start2)

    start3 = time.time()
    for ip in ip_list:
        t = threading.Thread(target=ping_batch, args=(ip,))
        t.start()
    for i in range(40):
        t.join()
    end3 = time.time()
    print(end3 - start3)


