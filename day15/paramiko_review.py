import paramiko

def connect_one(host, user, passwd):
    cmds = input('command:')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, user, passwd)
    ssh.exec_command(cmds)
    stdin, stdout, stderr = ssh.exec_command(cmds)
    if stderr:
        print('%s error:\r\n' % (host, stderr))
    if stdout:
        print('%s outputL\r\n' % (host, stdout))
    ssh.close()

if __name__ == '__main__':
    host = '192.168.2.16'
    user = 'root'
    passwd = '1'
    connect_one(host, user, passwd)