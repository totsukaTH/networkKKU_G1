# import important
#from curses.ascii import NULL
import socket
import threading
import time
from pymysql import NULL

# import option
from register import insertUser
from login import checkUser
from post import insertPost
from Reading import Reading
from register import insertUser
from Request import Request
from Allowmsg import Allow
from DELETE import Delpost ,Deluser
import optionText
import search

serverip = 'localhost'
port = 3000

clist = {}

# display option of client.
def logSuccess(data):
    if data[3] == 'a':
        client.send("print('1. Request\\n2. Allow\\n3. Delete\\n4. DeleteUser\\n5. Reading\\n6. logout')".encode('utf-8'))
        clist[client] = [addr,'a',data[0],data[2]]
    else :
        clist[client] = [addr,'u',data[0],data[2]]
        client.send("print('1. Post\\n2. Search\\n3. Reading\\n4. logout')".encode('utf-8'))

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
        
        # exit
        if data[0].upper() == 'exit'.upper() and clist[client][1] == 0:
            client.send("data = exit".encode('utf-8'))
            break


        ########################### Client ###########################
        if data[0].upper() == 'login'.upper() :
            if clist[client][1]==0:
                print("mas from client{}>>>{}".format(addr,data))
                client.send(optionText.inputLogin.encode('utf-8'))
            else :
                client.send("print('You are already logged in')".encode('utf-8'))
                client.send(optionText.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))

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
                    time.sleep(0.5)
                    logSuccess(dataIndatabase)
            if check == True : 
                # success
                client.send(optionText.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
            else :
                # fail
                client.send("print('The name or password is incorrect.')".encode('utf-8'))
                client.send(optionText.inputChoice.encode('utf-8'))

        # ----- option post -----
        elif data[0].upper() == 'post'.upper() and clist[client][1]=='u':
            print("mas from client{}>>>{}".format(addr,data))
            client.send(optionText.inputPost.encode('utf-8'))
            client.send(optionText.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
        # ----- action post -----
        elif data[0] == 'upPost':
            insertPost(data,clist[client][3])
        # ----- option search -----
        elif data[0].upper() == 'search'.upper():
            client.send(optionText.inputPostid.encode('utf-8'))
        # ----- action search ------
        elif data[0] == 'searchPostId' :
            RequestPost = search.searchPost(data[1])
            if len(RequestPost) ==1:
                for text in RequestPost :
                    client.send("print('ข้อความ : {}')".format(text[0]).encode('utf-8'))
            else:
                client.send("print('ไม่พบข้อความ')".encode('utf-8'))
            client.send(optionText.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
        # ----- option reading -----
        elif data[0].upper() == 'reading'.upper() and clist[client][1]!=0:
            for data in Reading():
                time.sleep(0.2)
                client.send("print('id:{} userpost:{} :::>>>{}')".format(data[0],data[1],data[2]).encode('utf-8'))
            client.send(optionText.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
        # ----- option request of Admin -----
        elif data[0].upper() == 'request'.upper() and clist[client][1]=='a':
            client.send("print('There are {} recases.')".format(len(Request())).encode('utf-8'))
            for data in Request():
                time.sleep(0.2)
                client.send("print('id:{} userpost:{} :::>>>{}')".format(data[0],data[1],data[2]).encode('utf-8'))
            client.send(optionText.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
        ##################################################################################
        elif data[0].upper() == 'Allow'.upper() and clist[client][1]=='a':
            client.send(optionText.inputallow.encode('utf-8'))
        elif data[0] == '-A' and clist[client][1]=='a':
            Allow(data[1])
            client.send(optionText.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
        ##################################################################################
        elif data[0].upper() == 'delete'.upper() and clist[client][1]=='a':
            client.send(optionText.inputdelete.encode('utf-8'))
        elif data[0] == '-d' and clist[client][1]=='a':
            Delpost(data[1])
            client.send(optionText.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
        ##################################################################################
        elif data[0].upper() == 'deleteuser'.upper() and clist[client][1]=='a':
            client.send(optionText.inputdeleteuser.encode('utf-8'))
        elif data[0] == '-D' and clist[client][1]=='a':
            Deluser(data[1])
            client.send(optionText.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))




        ########################### Register ###########################
        elif data[0] == 'register' :
            if clist[client][1]==0:
                print("mas from client{}>>>{}".format(addr,data))
                client.send(optionText.inputRegister.encode('utf-8'))
            else :
                client.send("print('You are already logged in')".encode('utf-8'))
                client.send(optionText.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
        ########################### Option Register ###########################
        # insert data from register
        elif data[0] == "insertUser" :
            insertUser(data[1],data[2],data[3])
            client.send("print('your insert register success')".encode('utf-8'))
            client.send(optionText.inputChoice.encode('utf-8'))
        elif data[0].upper() == 'logout'.upper() and clist[client][1] != 0:
            print("mas from client{}>>>{}".format(addr,data))
            clist[client] = [addr,0,NULL,NULL]
            # display menu.
            client.send("print('logout Successful\\n1. Login\\n2. Register\\n3. Exit')".encode('utf-8'))
            client.send(optionText.inputChoice.encode('utf-8'))
        else :
            if clist[client][1] == 0:
                client.send("print('command error')".encode('utf-8'))
                client.send(optionText.inputChoice.encode('utf-8'))
            else :
                client.send("print('command error')".encode('utf-8'))
                client.send(optionText.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
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
    client.send(optionText.inputChoice.encode('utf-8'))
    # display client and show status amount user online.
    print(client)
    print('กำลังออนไลน์',len(clist),'คน')
    task = threading.Thread(target=client_msg,args=(client,addr))
    task.start()