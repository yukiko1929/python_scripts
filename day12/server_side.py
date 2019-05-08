# tcp server
import socket

host = ''
port = 12345
addr = (host, port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen()

cli_sock, cli_addr = s.accept()
print('the host address:', cli_addr)

while True:
    data = s.recv(1024)
    # hdata = data.decode()
    if data.strip() == b'quit':
        break
    print(data.decode(),end='')
    content = input('content>') + '\r\b'
    rcontent = content.encode()
    cli_sock.send(rcontent)
    cli_sock.close()

s.close()




