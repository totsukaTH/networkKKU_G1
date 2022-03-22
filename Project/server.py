# import important
import socket
import threading
import time
from pymysql import NULL

# import file 
import delete
import allow
import login
import post
import home
import register
import reading
import request
import search

serverip = 'localhost'
port = 3000

clist = {}

# display option of client 'admin' and 'client'.
def logSuccess(data):
    if data[3] == 'a':
        client.send("print('==== Option of Admin ====\\n1. Request\\n2. Allow\\n3. Delete\\n4. DeleteUser\\n5. Reading\\n6. logout')".encode('utf-8'))
        # data[0] is username .
        # data[1] is userId.
        # addr is ip other.
        clist[client] = [addr,'a',data[0],data[2]]
    else :
        clist[client] = [addr,'u',data[0],data[2]]
        client.send(home.displayUser.encode('utf-8'))

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
            break

        ########################### Client ###########################
        # ----- login -----
        if data[0].upper() == 'login'.upper() :
            if clist[client][1] == 0:
                print("mas from client{}>>>{}".format(addr,data))
                client.send(login.inputLogin.encode('utf-8'))
            else :
                client.send("print('You are already logged in')".encode('utf-8'))
                client.send(login.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
        # ----- action login-----
        elif data[0] == 'checkUser':
            # for loop for checking username and passwork of user with data in database,
            check = False
            detailLogin = login.checkUser()
            for dataIndatabase in detailLogin :
                if dataIndatabase[0] == data[1] and dataIndatabase[1] == data[2] :
                    # username and password is correct.
                    check = True
                    client.send("print('Your login Successful :)\\n')".encode('utf-8'))
                    time.sleep(0.5)
                    # dataIndatabase is data of user that login to success 
                    # dataIndatabase is about userName, Password, userId
                    logSuccess(dataIndatabase)
            if check == True : 
                # success
                client.send(login.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
            else :
                # fail
                client.send("print('Your login fail :(\\n')".encode('utf-8'))
                # Come back home.
                time.sleep(0.2)
                client.send(home.displayHome.encode('utf-8'))
                client.send(home.inputChoice.encode('utf-8'))
        
        # ----- register -----
        elif data[0] == 'register' :
            if clist[client][1]==0:
                print("mas from client{}>>>{}".format(addr,data))
                client.send(register.inputRegister.encode('utf-8'))
            else :
                client.send("print('You are already logged in')".encode('utf-8'))
                client.send(login.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
        # ----- action register -----
        elif data[0] == "insertUser" :
            register.insertUser(data[1],data[2],data[3])
            client.send("print('your register success :)\\n')".encode('utf-8'))
            # Come back home.
            time.sleep(1.5)
            client.send(home.displayHome.encode('utf-8'))
            client.send(home.inputChoice.encode('utf-8'))
        
        # ----- post -----
        elif data[0].upper() == 'post'.upper() and clist[client][1]=='u':
            print("mas from client{}>>>{}".format(addr,data))
            client.send(post.inputPost.encode('utf-8'))
            time.sleep(0.2)
            client.send("print('You post success:)\\n')".encode('utf-8'))
            # come back menu user
            time.sleep(1.5)
            client.send(home.displayUser.format(clist[client][2]).encode('utf-8'))
            client.send(login.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
        # ----- action post -----
        elif data[0] == 'upPost':
            post.insertPost(data,clist[client][3])

        # ----- search -----
        elif data[0].upper() == 'search'.upper():
            client.send(post.inputPostid.encode('utf-8'))
        # ----- action search ------
        elif data[0] == 'searchPostId' :
            RequestPost = search.searchPost(data[1])
            if len(RequestPost) == 1:
                for text in RequestPost :
                    client.send("print('ข้อความ : {}')".format(text[0]).encode('utf-8'))
                time.sleep(0.2)
                client.send("print('You search success:)\\n')".encode('utf-8'))
                # come back menu user
                time.sleep(1.5)
                client.send(home.displayUser.format(clist[client][2]).encode('utf-8'))
                client.send(login.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
            else:
                client.send("print('ไม่พบข้อความ')".encode('utf-8'))
                time.sleep(0.2)
                client.send("print('You search fail:(\\n')".encode('utf-8'))
                # come back menu user
                time.sleep(1.5)
                client.send(home.displayUser.format(clist[client][2]).encode('utf-8'))
                client.send(login.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))

        # ----- reading -----
        elif data[0].upper() == 'reading'.upper() and clist[client][1]!=0:
            for data in reading.Reading():
                time.sleep(0.2)
                client.send("print('PostId {} UserId {} >>> {}')".format(data[0],data[1],data[2]).encode('utf-8'))
            time.sleep(0.2)
            client.send("print('You read phrase finished.\\n')".encode('utf-8'))
            time.sleep(1.5)
            client.send(home.displayUser.format(clist[client][2]).encode('utf-8'))
            client.send(login.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
        
        ########################### Admin ###########################
        # ----- equest -----
        elif data[0].upper() == 'request'.upper() and clist[client][1]=='a':
            client.send("print('There are {} recases.')".format(len(request.Request())).encode('utf-8'))
            for data in request.Request():
                time.sleep(0.2)
                client.send("print('id:{} userpost:{} :::>>>{}')".format(data[0],data[1],data[2]).encode('utf-8'))
            client.send(login.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))

        # ----- allow -----
        elif data[0].upper() == 'Allow'.upper() and clist[client][1]=='a':
            client.send(allow.inputDataForAllow.encode('utf-8'))
        elif data[0] == '-A' and clist[client][1]=='a':
            allow.Allow(data[1])
            client.send(login.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))

        # ----- delete -----
        elif data[0].upper() == 'delete'.upper() and clist[client][1]=='a':
            client.send(delete.deletepost.encode('utf-8'))
        elif data[0] == '-d' and clist[client][1]=='a':
            delete.Delpost(data[1])
            client.send(login.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))

        # ----- delete user -----
        elif data[0].upper() == 'deleteuser'.upper() and clist[client][1]=='a':
            client.send(delete.deleteuser.encode('utf-8'))
        elif data[0] == '-D' and clist[client][1]=='a':
            delete.Deluser(data[1])
            client.send(login.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))

        # ----- logout user and admin -----
        elif data[0].upper() == 'logout'.upper() and clist[client][1] != 0:
            print("mas from client{}>>>{}".format(addr,data))
            clist[client] = [addr,0,NULL,NULL]
            client.send("print('logout Successful\\n')".encode('utf-8'))
            # Come back home.
            time.sleep(1.5)
            client.send(home.displayHome.encode('utf-8'))
            client.send(home.inputChoice.encode('utf-8'))
        else :
            if clist[client][1] == 0:
                client.send("print('command error\\n')".encode('utf-8'))
                # Come back home.
                time.sleep(1.5)
                client.send(home.displayHome.encode('utf-8'))
                client.send(home.inputChoice.encode('utf-8'))
            elif clist[client][1] == 'u' :
                client.send("print('command error\\n')".encode('utf-8'))
                time.sleep(1.5)
                client.send(home.displayUser.format(clist[client][2]).encode('utf-8'))
                client.send(login.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
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
    client.send(home.displayHome.encode('utf-8'))
    client.send(home.inputChoice.encode('utf-8'))
    # display client and show status amount user online.
    print(client)
    print('กำลังออนไลน์',len(clist),'คน')
    task = threading.Thread(target=client_msg,args=(client,addr))
    task.start()