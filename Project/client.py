import socket
import threading
import time


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
        if (not data) or data == 'exit':
            print("exit")
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
    data = ''
    if data == 'exit':
        break
client.close()