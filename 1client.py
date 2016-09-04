import socket 
s = socket.socket()
host = 'g.cn'
port = 80
s.connect((host, port))
ip, port = s.getsockname()
print '{} and {}'.format(ip, port)
http_request = """GET / HTTP/1.1
host: {}

""".format(host)
s.send(http_request.encode('utf-8'))
response = s.recv(1023)
print response.decode('utf-8')
