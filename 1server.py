import socket
def read_from_file(filename):
    with open(filename, 'rb') as f:
       return f.read()

host = ''
port = 2000
s = socket.socket()
s.bind((host, port))

while True:
    s.listen(3)
    connection, ip = s.accept()
    request = connection.recv(1023)
    print '{}'.format(request)
    line = request.split('\r\n')[0]
    path = line.split()[1]
    print '{}'.format(path)
    normal_response = b'hello world'
    doge_response = b'''HTTP/1.1 200 OK
Content-Type: text/html

hello doge!<img src="doge.jpg"><img src="doge1.gif">'''
    if path =='/doge':
        response = doge_response
    elif path == '/doge.jpg':
        response = read_from_file("doge.jpg")
    elif path == '/doge1.gif':
        response = read_from_file("doge1.gif")
    else:
        response = normal_response
    connection.sendall(response)
    connection.close()
