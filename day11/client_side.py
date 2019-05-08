import socket

# tcp cilent
# host = '192.168.4.254'
# port = 12345
# addr = (host, port)
# c = socket.socket
# c.connect(addr)
#
# while True:
#     data = input('(quit to end)>') + '\r\n'
#     c.send(data.encode())
#     if data.strip() == 'quit':
#         break
#
#     rd = c.recv(1024)
#     print(rd.decode(), end='')
#
# c.close()

# tcp client
# host = '192.168.4.254'
# port = 12345
# addr = (host, port)
# c = socket.socket()
# c.connect(addr)
#
# while True:
#     data = input('(quit to end)')
#     c.send(data.encode())
#     if data == 'quit':
#         break
#     rdata = c.recv(1024)
#     print(rdata.decode(), end='')
#
# c.close()


# udp client
host = '192.168.4.254'
port = 12345
addr = (host, port)
c = socket.socket(socket.SOCK_DGRAM)

while True:
    data = input('quit to end>') + '\r\n'
    dedata = data.encode()
    c.sendto(dedata, addr)
    if dedata == 'quit':
        break

    info = c.recvfrom(1024)
    address = c.recvfrom(1024)[1]
    data = c.recvfrom(1024)[0]
    print(data.decode(), end='')
    print(address.decode(), end='')
c.close()
