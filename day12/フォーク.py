import subprocess
import os


def ping_batch(host):
    rv = subprocess.run('ping -c2 %s' % host, shell=True)
    if rv:
        print('%s is down' % host)
    else:
        print('%s is up' % host)

if __name__ == '__main__':
    ip_list = ['192.168.4.%s' % i for i in range(1,254)]
    for ips in ip_list:
        retval = os.fork()
        if not retval:
            ping_batch(ips)
            exit()
