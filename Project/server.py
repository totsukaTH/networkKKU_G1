#Server
from inspect import classify_class_attrs
import socket
serverip = '127.0.0.1'
port = 3000

while True:
    # create socket
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) #Set Socket Option ให้ Socket ใช้ Port เดียวกัน
    server.bind((serverip,port))
    server.listen(5)
    print('Wating for client...')
    client, addr = server.accept()
    print('Connect from: ', str(addr))
    data = client.recv(1024).decode('utf-8')
    print('Client massage : ', data)
    client.send('We Recived your message to {}'.format(data).encode('utf-8'))
    client.close()