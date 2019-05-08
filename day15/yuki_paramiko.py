import paramiko


class ConnectMany:
    def __init__(self, iden, passwd):
        self.iden = iden
        self.passwd = passwd

    def paracomman(self):
        cmds = input('enter the command to be executed on %s:' % self)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self, username = self.iden, password= self.passwd)
        ssh.exec_command(cmds)
        stdin, stdout, stderr = ssh.exec_command(cmds)
        out = stdout.read()
        err = stderr.read()
        if out:
            print('%s OUT\n %s' % ())
        ssh.close()

if __name__ == '__main__':
    # host = '192.168.4.16'
    # iden = 'root'
    # passwd = '1'
    # paracomman(host, iden, passwd)
    cm = ConnectMany()
    # '192.168.4.15' = cm.paracomman('root','1')