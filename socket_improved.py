import socket

host = ''
port = 12345
addr = (host, port)
s = socket.socket()    #default is TCP socket

# after program executed, OS will kep the socket for 1 minute, thus within 1 minute we can not connect more than once
# such a problem can be solved by adding the following:
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)    #bind the address to host
s.listen(1)    #to start listening process   netstat -tunpl | grep 12345

while True:

    try:
        client_soc, cli_addr = s.accept()    #wait for connection from client side
    except KeyboardInterrupt:
        print('')
        break

    print('client address:' , cli_addr)

    # while True:
    #     data = client_soc.recv(1024)
    #     print(data)
    #     server_se = input('content:')
    #     server_send = server_se.encode()
    #     client_soc.send(b'%s\r\n' % server_send)# the data sent by client should be byte category.
    #     if data.decode() == 'quit':
    #         client_soc.close()
        # client_soc.close()
        # s.close()

    while True:
        data = client_soc.recv(1024)
        if data.strip() == b'quit':
            break
        print(data.decode(), end='')
        cont = input('content:')
        content = cont.encode()
        client_soc.send(b'%s\r\n' % content)
    client_soc.close()
s.close()

