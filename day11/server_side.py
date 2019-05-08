import socket

# #tcp server
# host = ''
# port = 12345
# addr = (host, port)
# s = socket.socket()
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.bind(addr)
# s.listen(1)
# cli_soc, cli_addr = s.accept()
# print('the client host:', cli_addr)
#
# while True:
#     data = cli_soc.recv(1024)
#     if data.strip() == b'quit':
#         break
#     hdata = data.decode()
#     print(hdata, end='')
#     content = input('content>') + '\r\n'
#     cli_soc.send(content.encode())
# cli_soc.close()
#
# s.close()

# udp server
# host = ''
# port = 12345
# addr = (host, port)
# s = socket.socket(type=socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.bind(addr)
#
# data, cli_addr = s.recvfrom(1024)
# print(data.decode(), end='')
# s.sendto(b'how are you\r\n', addr)
# s.close()

host = ''
port = 12345
addr = (host, port)
s = socket.socket(socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)

while True:
    data, cli_addr = s.recvfrom(1024)
    dedata = data.decode()
    if dedata == 'quit':
        break
    print(dedata, end='')
    s.sendto(b'how are you\r\n')
s.close()












