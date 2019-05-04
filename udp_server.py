import socket
from time import strftime

host = ''
port = 12345
addr = (host, port)

s = socket.socket(type=socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
while True:
    data, cli_addr = s.recvfrom(1024)
    data = data.decode()
    print(data, end= '')
    sdata = '%s: %s' % (data, strftime('%Y%m%d'))
    s.sendto(sdata.encode(), cli_addr)

s.close()

#白い恋人
#面白い恋人