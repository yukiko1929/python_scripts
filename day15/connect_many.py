import paramiko
import getpass
import sys
import os
import threading

def paracomman(host, user,passwd, cmds):
    # cmds = input('enter the command to be executed on %s:' % self)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd)
    ssh.exec_command(cmds)
    stdin, stdout, stderr = ssh.exec_command(cmds)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('%s OUT:\n %s' % (host, out.decode()))
    if err:
        print('%s \033[31;1mERR\033[0m:\n %s' % (host, err.decode()))
    ssh.close()

if __name__ == '__main__':
    # user = 'root'
    # passwd = '1'
    # cmds = input('please enter command:')
    # ip_list = ['192.168.4.%s' % i for i in range(13,17)]
    # for ip in ip_list:
    #     paracomman(ip, user,passwd,cmds)
    # if len(sys.argv) != 3:
    #     print('%s usage hostfile command' % sys.argv[0])
    # ipfile = sys.argv[1]
    # user = 'root'
    # if not os.path.isfile(ipfile):
    #     print('file not existed')
    # passwd = getpass.getpass()
    # cmds = sys.argv[2]
    # with open(ipfile) as fobj:
    #     for lines in fobj:
    #         ip = lines.strip()
    #         paracomman(ip, user, passwd=passwd, cmds = cmds)
    #
    # if len(sys.argv) != 3:
    #     print('%s usage filename command' % sys.argv[0])

    ipfile = sys.argv[1]
    user = 'root'
    if not os.path.isfile(ipfile):
        print('file not existed')
    passwd = getpass.getpass()
    cmds = sys.argv[2]
    with open(ipfile) as fobj:
        for lines in fobj:
            ip = lines.strip()
            tcon = threading.Thread(target=paracomman, args=(ip,), kwargs={'passwd':passwd, 'cmds':cmds})
            tcon.start()

            #args 位置参数
            #kwargs 关键字参数

