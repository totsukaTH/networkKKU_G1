from re import I
import socket
import threading
from turtle import back
import time

from pymysql import NULL
serverip = 'localhost'
port = 3000

def server_msg(client):
    data = NULL
    while True:
        try:
            print(client.recv(4096).decode('utf-8'))
        except:
            break
        if (not data) or data == 'exit':
            break
        
    client.close()



client = socket.socket()
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)


try:
    client.connect((serverip,port))
except:
    print('not server')

task = threading.Thread(target=server_msg,args=(client,))
task.start()
time.sleep(0.5)

while True:
    data = input('mas>>>')
    if data == 'exit':
        break
    client.send(data.encode('utf-8'))
    time.sleep(0.2)
client.close()