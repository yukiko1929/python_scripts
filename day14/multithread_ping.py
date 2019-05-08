import os
import threading
import subprocess
import time

def ping_batch(host):
    ret = subprocess.run('ping -c2 %s > /dev/null' % host, shell=True)
    if ret:
        print('the host %s is down' % host)
    else:
        print('the host %s is up' % host)

if __name__ == '__main__':
    ip_list = ['192.168.4.%s' % i for i in range(11, 50)]
    # start = time.time()
    # for ip in ip_list:
    #     reva = os.fork()
    #     if reva == 0:
    #         ping_batch(ip)
    #         exit()
    # for i in range(49):
    #     os.waitpid(-1,0)
    # ended = time.time()
    # print(ended - start)

    start2 = time.time()
    for ip in ip_list:
        tts = threading.Thread(target=ping_batch(ip))
        tts.start()
        tts.join()
    end2 = time.time()
    print(end2 - start2)
