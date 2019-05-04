import socket

host = ''
port = 12345
addr = (host, addr)
s = socket.socket()  #to create socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)    #to bind the address to socket
