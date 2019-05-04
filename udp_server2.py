import socket
from time import strftime

host = ''
port = 12345
addr = (host, port)
s = socket.socket()
s.bind(addr)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

while True:
    data, cli_addr  = s.recvfrom(1024)
    data = data.decode()
    print(data, end='')
    sdata = '%s: %s' % (data, strftime('%H:%M:%S'))
    s.sendto(sdata.encode(), cli_addr)
s.close()