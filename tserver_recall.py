import socket

host = ''
port = 12345
addr = (host, port)
s = socket.socket()

s.bind(addr)
s.listen(1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
while True:

    c_sock, c_addr = s.accept()
    print('the client host:', c_addr)
    while True:
        data = c_sock.recv(1024)
        if data.strip() == b'quit':
            break
        else:
            print(data.decode(), end='')
        content = input('content>')
        c_sock.send(b'%s\r\n' % content.encode())
    c_sock.close()
s.close()
