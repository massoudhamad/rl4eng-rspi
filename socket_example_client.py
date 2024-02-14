import socket
# Create a TCP/IP socket
server_address = ('192.168.4.3', 2000)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect(server_address)
except socket.error:
    # provide some error message
    print("Error")
