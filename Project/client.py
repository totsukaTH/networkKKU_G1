import socket
import threading
import time
import sys
from pymysql import NULL

serverip = 'localhost'
port = 3000

def str_to(data):
    return "{}".format(data)

def server_msg(client):
    data = NULL
    while True:
        try:
            data = client.recv(4096).decode('utf-8')

        except:
            break
        
        exec(data)

        # exit
        if (not data) or data == 'exit':
            sys.exit()

    client.close()


client = socket.socket()
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

try:
    client.connect((serverip,port))
except:
    print('not server')

task = threading.Thread(target=server_msg,args=(client,))
task.start()
task.join()
time.sleep(1.5)
client.close()


