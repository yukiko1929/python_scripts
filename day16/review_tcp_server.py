import socket

# host = '127.0.0.1'
# port = 12345
# addr = (host, port)
# s = socket.socket()
# # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.bind(addr)
# s.listen()
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
# while True:
#     try:
#         cli_soc,cli_addr = s.accept()
#     except KeyboardInterrupt:
#         print('')
#         break
#
#     print('host addr:', cli_addr)
#
#     while True:
#         data = cli_soc.recv(1024)
#         if data.strip() == b'quit':
#             break
#         print(data.decode(),end='')
#         content = input('content>')
#         cli_soc.send(b'%s\r\n' % content.encode())
#     cli_soc.close()
# s.close()


#
# host = '127.0.0.1'
# port = 12345
# addr = (host, port)
# s = socket.socket()
# s.bind(addr)
# s.listen()
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
#
#
# while True:
#     try:
#         cli_soc, cli_addr = s.accept()
#     except KeyboardInterrupt:
#         print('')
#         break
#
#     print('host address:', cli_addr)
#     while True:
#         data = cli_soc.recv(1024)
#         if data.strip() == b'quit':
#             break
#         print(data.decode(), end='')
#         content = input('content>')
#         cli_soc.send(b'%s\r\n' % content.encode())
#     cli_soc.close()
# s.close()

import socket
import time

host = '0.0.0.0'
port = 21212
addr = (host, port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind(addr)
s.listen(1)

cli_soc, cli_addr = s.accept()  # to accept a new link
print('client address', cli_addr)
data = str(cli_soc.recv(1024), encoding = 'utf8')
#print(data.decode(), end='')
data = '%s[%s]' % (time.strftime('%H:%M:%S'), data)
print(data)
cli_soc.sendall(bytes(data, encoding='utf8'))
cli_soc.close()
s.close()

