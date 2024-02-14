import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address
#server_address = ('192.168.4.3', 20000)
server_address = ('172.24.197.51', 20000)
print "Server Adrress server_address",server_address
sock.bind(server_address)
sock.listen(1)

# Endless loop
while 1:
    connection, client_address = sock.accept()
    data = connection.recv(8)
    # do sth with data
    connection.sendall(data)

connection.close()