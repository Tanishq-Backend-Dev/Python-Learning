import socket

s = socket.socket()
print('Socket Created')

s.bind(('localhost',10000))

s.listen(3)
print('Waiting for Connection')


while True:
    c,addr = s.accept()
    print("Connected with",addr)
    
    c.send(bytes("Welcome","utf-8"))
    
    c.close()