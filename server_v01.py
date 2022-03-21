from asyncio import tasks
from asyncio.windows_events import NULL
import socket
from inspect import classify_class_attrs
import socket
import threading
from xmlrpc.client import Server

serverip = 'localhost'
port = 3000

clist = {}

def client_msg(client,addr):
    data = NULL
    while True:
        try:
            data  = (client.recv(4096).decode('utf-8'))
        except:
            clist.pop(client)
            break
        if (not data) or data == 'exit':
            #print('not data')
            clist.pop(client)
            break
        else:
            print("mas from client{}>>>{}".format(addr,data))
            client.send('1.login\n2.regit\n3.exit'.format(data).encode('utf-8'))
            

        
    client.close()

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) #Set Socket Option ให้ Socket ใช้ Port เดียวกัน
server.bind((serverip,port))
server.listen(5)

print('server on')

while True:
    client, addr = server.accept()
    clist[client] = [addr,0,NULL]
    client.send('1.login\n2.regit\n3.exit'.encode('utf-8'))
    print(client)
    print('กำลังออนไลน์',len(clist),'คน')
    task = threading.Thread(target=client_msg,args=(client,addr))
    task.start()

#klayut 633020032-4 
