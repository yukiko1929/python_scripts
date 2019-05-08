import os
import subprocess

def ping_batch(host):
    rv = subprocess.run('ping -c2 %s > /dev/null' % host, shell=True)
    if rv:
        print('%s is down' % host)
    else:
        print('%s is up' % host)

if __name__ == '__main__':
    ip_list = ['176.121.202.%s' % i for i in range(1,100)]
    for ip in ip_list:
        myfork = os.fork()
        if not myfork:
            ping_batch(ip)
            exit()

