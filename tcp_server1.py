import socket

host = ''
port =12345
addr = (host, port)
s = socket.socket()

s.bind(addr)
s.listen(1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

while True:
    try:
        cli_soc, cli_addr = s.accept()

    except KeyboardInterrupt:
        print('')
        break

    print('the client host:', cli_addr)

    while True:
        data = cli_soc.recv(1024)
        if data.strip() == b'quit':
            break
       # print('the client host:', cli_addr)
        print(data.decode(), end='')
        content = input('content>')
        cli_soc.send(b'%s\r\n' % content.encode())
    cli_soc.close()
s.close()