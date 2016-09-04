import socket
host = ''
port = 2000
s = socket.socket()
s.bind((host, port))

while True:
    s.listen(3)
    connection, ip = s.accept()
    request = connection.recv(1023)
    print request
    response = b'hello world'
    print response
    connection.sendall(response)
    connection.close()
