import socket

host = ''
port = 12345
addr = (host, port)
s = socket.socket()    #default is TCP socket

# after program executed, OS will kep the socket for 1 minute, thus within 1 minute we can not connect more than once
# such a problem can be solved by adding the following:

s.bind(addr)    #bind the address to host
s.listen(1)    #to start listening process   netstat -tunpl | grep 12345
client_soc, cli_addr = s.accept()    #wait for connection from client side
print('client address:' , cli_addr)
data = client_soc.recv(1024)
print(data)
client_soc.send(b'how are you\r\n')    # the data sent by client should be byte category.
client_soc.close()
s.close()


