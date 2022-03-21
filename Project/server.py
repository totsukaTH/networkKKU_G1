# import important
from curses.ascii import NUL
import socket
import threading
import time
from pymysql import NULL

# import option
from register import insertUser
from login import checkUser
from type import checktype
from post import insertPost
from Reading import Reading
from register import insertUser
from Request import Request

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

# display option of client.
def logSuccess(data):
    if checktype(data[1]) == 'a':
        client.send("print('1. Request\\n2. Allow\\n3. Delete\\n4. Delete_User\\n5.Reading\\n6. offserver\\n7. Exit')".encode('utf-8'))
        clist[client] = [addr,'a',data[0],data[2]]
    else :
        clist[client] = [addr,'u',data[0],data[2]]
        client.send("print('1. Post\\n2. Search\\n3. Reading\\n4. Exit')".encode('utf-8'))


def upPost(data,add):
    pass


# massage
def client_msg(client,addr):
    while True:
        data = NULL
        try:
            data  = eval(client.recv(4096).decode('utf-8'))
        except:
            clist.pop(client)
            break
        print(data)
        
        # condition
        if data[0] == 'exit':
            client.send("data = exit".encode('utf-8'))
            clist.pop(client)
            break
        ########################### Client ###########################
        if data[0] == 'login' :
            if clist[client][1]==0:
                print("mas from client{}>>>{}".format(addr,data))
                client.send(loGin.encode('utf-8'))
            else :
                client.send("print('You are already logged in')".encode('utf-8'))
                client.send(userlogininput.format(clist[client][2]).encode('utf-8'))
        ########################### Option of Client ###########################
        # ----- check user and get data of user in database for doing post-----
        elif data[0] == 'checkUser':
            # for loop for checking username and passwork of user with data in database,
            check = False
            detailLogin = checkUser()
            for dataIndatabase in detailLogin :
                if dataIndatabase[0] == data[1] and dataIndatabase[1] == data[2] :
                    # username and password is correct.
                    check = True
                    client.send("print('=============login Successful=============')".encode('utf-8'))
                    time.sleep(0.2)
                    logSuccess(dataIndatabase)
            if check == True : 
                client.send(userlogininput.format(clist[client][2]).encode('utf-8'))
            else :
                # fail
                client.send("print('The name or password is incorrect.')".encode('utf-8'))
                client.send(userinput.encode('utf-8'))
        # ----- option post -----
        elif data[0] == 'post' and clist[client][1]=='u':
            client.send(postsrt.encode('utf-8'))
            client.send(userlogininput.format(clist[client][2]).encode('utf-8'))
        # ----- option uppost -----
        elif data[0] == 'upPost':
            insertPost(data,clist[client][3])
        # ----- option reading -----
        elif data[0] == 'reading' and clist[client][1]!=0:
            for data in Reading():
                time.sleep(0.2)
                client.send("print('id:{} userpost:{} :::>>>{}')".format(data[0],data[1],data[2]).encode('utf-8'))
            client.send(userlogininput.format(clist[client][2]).encode('utf-8'))
        # ----- option request of Admin -----
        elif data[0] == 'request'and clist[client][1]=='a':
            for data in Request():
                client.send("print('id:{} userpost:{} :::>>>{}')".format(data[0],data[1],data[2]).encode('utf-8'))
            client.send(userlogininput.format(clist[client][2]).encode('utf-8'))

        ########################### Register ###########################
        if data[0] == 'register' :
            if clist[client][1]==0:
                print("mas from client{}>>>{}".format(addr,data))
                client.send(register.encode('utf-8'))
            else :
                client.send("print('You are already logged in')".encode('utf-8'))
                client.send(userlogininput.format(clist[client][2]).encode('utf-8'))
        ########################### Option Register ###########################
        # insert data from register
        elif data[0] == "insertUser" :
            insertUser(data[1],data[2],data[3])
            client.send("print('your insert register success')".encode('utf-8'))
            client.send(userinput.encode('utf-8'))

    client.close()

# start server
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) #Set Socket Option ให้ Socket ใช้ Port เดียวกัน
server.bind((serverip,port))
server.listen(5)

print('server waiting ...')

while True:
    client, addr = server.accept()
    clist[client] = [addr,0,NULL,NULL]
    # display menu.
    client.send("print('1. Login\\n2. Register\\n3. Exit')".encode('utf-8'))
    client.send(userinput.encode('utf-8'))
    # display client and show status amount user online.
    print(client)
    print('กำลังออนไลน์',len(clist),'คน')
    task = threading.Thread(target=client_msg,args=(client,addr))
    task.start()