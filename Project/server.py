import socket
import threading
import time
from pymysql import NULL
from register import insertUser
from login import checkUser

# import file for making login and register
from register import insertUser

serverip = 'localhost'
port = 3000

clist = {}


userlogininput = '''
data = input('user name is "{}" : ')
client.send(str_to([data]).encode('utf-8'))
'''
userinput = '''
data = input('Enter your choice : ')
client.send(str_to([data]).encode('utf-8'))
'''
 
# login
loGin = '''
def login():
    print("Your login")
    userName = input('Username : ')
    passWord = input('Password : ')
    client.send(str_to(['checkUser',userName,passWord]).encode('utf-8'))
login()
'''
# register
register = '''
def registerUser():
    # insert data of register
    email = input('Email : ')
    userName = input('Username : ')
    passWord = input('Password : ')
    client.send(str_to(['insertUser',email,userName,passWord]).encode('utf-8'))
registerUser()
'''

def client_msg(client,addr):
    while True:
        data = NULL
        try:
            data  = eval(client.recv(4096).decode('utf-8'))
        except:
            clist.pop(client)
            break
        print(data)

        if (not data) or data == 'exit':
            #print('not data')
            clist.pop(client)
            break
        # login
        if data[0] == 'login' :
            if clist[client][1]==0:
                print("mas from client{}>>>{}".format(addr,data))
                client.send(loGin.encode('utf-8'))
            else :
                client.send("print('You are already logged in')".encode('utf-8'))
                client.send(userlogininput.format(clist[client][2]).encode('utf-8'))
        # check user and password
        elif data[0] == 'checkUser':
            if checkUser(data[1],data[2]) == True:
                client.send("print('login Successful')".encode('utf-8'))
                clist[client] = [addr,1,data[1]]
                client.send(userlogininput.format(clist[client][2]).encode('utf-8'))
            else :
                client.send("print('The name or password is incorrect.')".encode('utf-8'))
                client.send(userinput.encode('utf-8'))
        # register
        elif data[0] == 'register' :
            if clist[client][1]==0:
                print("mas from client{}>>>{}".format(addr,data))
                client.send(register.encode('utf-8'))
                client.send(userinput.encode('utf-8'))
            else :
                client.send("print('You are already logged in')".encode('utf-8'))
                client.send(userlogininput.format(clist[client][2]).encode('utf-8'))
        # insert data from register
        elif data[0] == "insertUser" :
            insertUser(data[1],data[2],data[3])
            client.send("print('your insert register success')".encode('utf-8'))
        else:
            client.send("print('error')".encode('utf-8'))
            client.send(userinput.encode('utf-8'))

        
    client.close()

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) #Set Socket Option ให้ Socket ใช้ Port เดียวกัน
server.bind((serverip,port))
server.listen(5)

print('server on')

while True:
    client, addr = server.accept()
    clist[client] = [addr,0,NULL]
    client.send("print('1. Login\\n2. Register\\n3. Exit')".encode('utf-8'))
    client.send(userinput.encode('utf-8'))
    print(client)
    print('กำลังออนไลน์',len(clist),'คน')
    task = threading.Thread(target=client_msg,args=(client,addr))
    task.start()