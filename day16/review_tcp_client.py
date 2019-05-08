import socket

server = '176.121.202.32'
port  = 12345
addr = (server, port)
c = socket.socket()
c.connect(addr)

while True:
    data = input('quit to end>') + '\r\n'
    c.send(data.encode())
    if data.strip() == 'quit':
        break
    sdata = c.recv(1024)
    print(sdata.decode(), end='')
c.close()