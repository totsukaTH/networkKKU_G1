import socket
import threading
import time
from pymysql import NULL
from login import checkUser
from type import checktype
from post import insertPost
from Reading import Reading
# import file for making login and register
import login
import register

serverip = 'localhost'
port = 3000

clist = {}


userlogininput = '''
data = input('user name is "{}" >>> ')
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

postsrt = '''
def post():
    print("Enter the message you want to post.")
    message = input('>>>')
    client.send(str_to(['upPost',message]).encode('utf-8'))
post()
'''
Readingstr = """

def Reading():
    print("Enter '>>' or '<<'")
    #message = input('>>>')
    #client.send(str_to([message]).encode('utf-8'))
post()

"""


def logSuccess(data):
    if checktype(data[1]) == 'a':
        client.send("print('1. Request\\n2. Allow\\n3. Delete\\n4. Delete_User\\n5.Reading\\n6. offserver')".encode('utf-8'))
        clist[client] = [addr,'a',data[1]]
    else :
        clist[client] = [addr,'u',data[1]]
        client.send("print('1. Post\\n2. Search\\n3. Reading')".encode('utf-8'))


def upPost(data,add):
    pass



def client_msg(client,addr):
    while True:
        data = NULL
        try:
            data  = eval(client.recv(4096).decode('utf-8'))
        except:
            clist.pop(client)
            break
        print(data)
        if (not data[0]) or data[0] == 'exit':
            client.send("data = exitw".encode('utf-8'))
            clist.pop(client)
            break
        if data[0] == 'login' :
            if clist[client][1]==0:
                print("mas from client{}>>>{}".format(addr,data))
                client.send(loGin.encode('utf-8'))
            else :
                client.send("print('You are already logged in')".encode('utf-8'))
                client.send(userlogininput.format(clist[client][2]).encode('utf-8'))
        elif data[0] == 'checkUser':
            if checkUser(data[1],data[2]) == True:
                client.send("print('=============login Successful=============')".encode('utf-8'))
                time.sleep(0.2)
                logSuccess(data)
                client.send(userlogininput.format(clist[client][2]).encode('utf-8'))
            else :
                client.send("print('The name or password is incorrect.')".encode('utf-8'))
                client.send(userinput.encode('utf-8'))

        elif data[0] == 'register' :
            if clist[client][1]==0:
                print("mas from client{}>>>{}".format(addr,data))
                client.send("print('Your register.')".encode('utf-8'))
                client.send(userinput.encode('utf-8'))
            else :
                client.send("print('You are already logged in')".encode('utf-8'))
                client.send(userlogininput.format(clist[client][2]).encode('utf-8'))

        elif data[0] == 'post' and clist[client][1]=='u':
            client.send(postsrt.encode('utf-8'))
            client.send(userlogininput.format(clist[client][2]).encode('utf-8'))
        elif data[0] == 'upPost':
            insertPost(data,clist[client][2])

        elif data[0] == 'reading' and clist[client][1]!=0:
            for data in Reading():
                time.sleep(0.2)
                client.send("print('id:{} userpost:{} :::>>>{}')".format(data[0],data[1],data[2]).encode('utf-8'))
            client.send(userlogininput.format(clist[client][2]).encode('utf-8'))
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

#klayut 633020032-4 