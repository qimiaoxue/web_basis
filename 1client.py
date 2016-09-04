import socket
s = socket.socket()
host = 'www.thebeijinger.com'
port = 80
s.connect((host, port))
ip, port = s.getsockname()
print '{} and {}'.format(ip, port)
http_request = """GET / HTTP/1.1
host: {}
Connection: close

""".format(host)
s.send(http_request.encode('utf-8'))
response = b''
while True:
    r = s.recv(1023)
    if len(r) == 0:
        break
    response += r
    print 'hello jay'
with open('beijinger.response.txt','wb') as f:
    f.write(response)

