# import important
import socket
import threading
import time
from pymysql import NULL

# import file 
import DELETE
import allow
import login
import post
import home
import register
import Reading
import Request
import search
import showuser

serverip = 'localhost'
port = 3000
clist = {}

# Come back home.
def comeBackHome():
    time.sleep(0.2)
    client.send(home.displayHome.encode('utf-8'))
    client.send(home.inputChoice.encode('utf-8'))

# Come back menu user.
def comeBackMenuUser():
    client.send(home.displayUser.format(clist[client][2]).encode('utf-8'))
    client.send(login.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))

# Come back menu admin.    
def comeBackMenuAdmin():
    client.send(home.displayAdmin.format(clist[client][2]).encode('utf-8'))
    client.send(login.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))

# Login success.
def logSuccess(data):
    # Addr is ip and about data of client other.
    # Data[0] is username .
    # Data[2] is userId.
    if data[3] == 'a':
        # Insert data to clist
        clist[client] = [addr,'a',data[0],data[2]]
        # User is admin.
        # Show option of Admin.
        client.send(home.displayAdmin.encode('utf-8'))
    else :
        # Insert data to clist
        clist[client] = [addr,'u',data[0],data[2]]
        # User is admin.
        # Show option of User.
        client.send(home.displayUser.encode('utf-8'))

# Massage
def client_msg(client,addr):
    while True:
        data = NULL
        try:
            # Get data from client.
            data  = eval(client.recv(4096).decode('utf-8'))
        except:
            clist.pop(client)
            break
        # Show data from client.
        print(data)
        
        # ----- exit ------
        if data[0].upper() == 'exit'.upper() or data[0] == '3' and clist[client][1] == 0:
            # data[0] == '3' or data[0] == 'exit' in home.
            break

        ########################### Client ###########################

        # ----- login -----
        if data[0].upper() == 'login'.upper() or data[0] == '1' and clist[client][1] == 0 :
            if clist[client][1] == 0:
                # User is in Home.
                print("mas from client{}>>>{}".format(addr,data))
                # User choose login.
                client.send(login.inputLogin.encode('utf-8'))
            else :
                # User logined.
                client.send("print('You are already logined in')\n".encode('utf-8'))
                client.send(login.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
        # ----- action login-----
        elif data[0] == 'checkUser':
            # for loop for checking username and passwork of user with data in database.
            check = False
            detailLogin = login.checkUser()
            for dataIndatabase in detailLogin :
                if dataIndatabase[0] == data[1] and dataIndatabase[1] == data[2] :
                    # username and password is correct.
                    check = True
                    client.send("print('Your login Successful :)'\n)".encode('utf-8'))
                    time.sleep(0.5)
                    # dataIndatabase is data of user that login to success 
                    # dataIndatabase is about userName, Password, userId
                    logSuccess(dataIndatabase)
            if check == True : 
                # success
                client.send(login.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
            else :
                # Login fail.
                client.send("print('Your login fail :(')\n".encode('utf-8'))
                # Come back home.
                comeBackHome()

        # ----- register -----
        elif data[0] == 'register' or data[0] == '2' and clist[client][1] == 0 :
            if clist[client][1]==0:
                # User is in Home.
                print("mas from client{}>>>{}".format(addr,data))
                # User choose register.
                client.send(register.inputRegister.encode('utf-8'))
            else :
                client.send("print('You are already logined in')\n".encode('utf-8'))
                # User logined.
                client.send(login.inputChoiceAfterLogin.format(clist[client][2]).encode('utf-8'))
        # ----- action register -----
        elif data[0] == "insertUser" :
            # Insert data of user that user to database.
            register.insertUser(data[1],data[2],data[3])
            client.send("print('your register success :)')\n".encode('utf-8'))
            # Come back home.
            comeBackHome()
        
        # ----- post -----
        elif data[0].upper() == 'post'.upper() or data[0] == '1' and clist[client][1]=='u':
            print("mas from client{}>>>{}".format(addr,data))
            # User choose post.
            # User input content.
            client.send(post.inputPost.encode('utf-8'))
        # ----- action post -----
        elif data[0] == 'upPost':
            post.insertPost(data,clist[client][3])
            time.sleep(0.2)
            # User insert data of content to success.
            client.send("print('You post success :)')\n".encode('utf-8'))
            # Come back menu user.
            comeBackMenuUser()

        # ----- search -----
        elif data[0].upper() == 'search'.upper() or data[0] == '3' and clist[client][1]=='u':
            # User input post id to search.
            client.send(search.inputPostid.encode('utf-8'))
        # ----- action search ------
        elif data[0] == 'searchPostId' :
            # Return value boolean for checking data in database.
            # True, It has data of postId.
            # False, It hasn't data of postId.
            RequestPost = search.searchPost(data[1])
            if bool(RequestPost) == True:
                # postId has database.
                for text in RequestPost :
                    # display content by post id.
                    client.send("print('ข้อความ : {}')".format(text[0]).encode('utf-8'))
                time.sleep(0.2)
                # It has a postId in database.
                client.send("print('You search success :)')\n".encode('utf-8'))
                # Come back menu user.
                comeBackMenuUser()
            else:
                # It hasn't data of postId in database.
                client.send("print('ไม่พบข้อความ')".encode('utf-8'))
                time.sleep(0.2)
                client.send("print('You search fail :(')\n".encode('utf-8'))
                # Come back menu user.
                comeBackMenuUser()

        # ----- reading -----
        elif data[0].upper() == 'reading'.upper() or (data[0] == '2' and clist[client][1] == 'u') or (data[0] == '3' and clist[client][1] == 'a') :
            client.send("print('\\n== Reading ==')".encode('utf-8'))
            # Display all content that allow by Admin.
            for data in reading.Reading():
                time.sleep(0.2)
                client.send("print('PostId {} UserId {} >>> {}')".format(data[0],data[1],data[2]).encode('utf-8'))
            time.sleep(0.2)
            # Reading success.
            client.send("print('You read phrase finished :)')\n".encode('utf-8'))
            if clist[client][1]=='a' :
                # Come back menu admin.
                comeBackMenuAdmin()
            else :
                # Come back menu user.
                comeBackMenuUser()
        
        ########################### Admin ###########################
        # ----- request -----
        elif data[0].upper() == 'request'.upper() or (data[0] == '1' and clist[client][1] == 'a') :
            client.send("print('\\n== Request ==')".encode('utf-8'))
            client.send("print('There are {} phrase.')".format(len(request.Request())).encode('utf-8'))
            # Display content of user isn't allow by Admin.
            for data in request.Request():
                time.sleep(0.2)
                client.send("print('id:{} userId:{} date:{} : {}')".format(data[0],data[1],data[2],data[3]).encode('utf-8'))
            time.sleep(0.2)
            # request is success.
            client.send("print('You request to success :)')\n".encode('utf-8'))
            # Come back menu admin.
            comeBackMenuAdmin()

        # ----- allow -----
        elif data[0].upper() == 'Allow'.upper() or (data[0] == '2' and clist[client][1] == 'a'):
            client.send("print('\\n== Allow ==')".encode('utf-8'))
            # Input postid to allow.
            client.send(allow.inputDataForAllow.encode('utf-8'))
        elif data[0] == '-A' and clist[client][1]=='a':
            # Return boolean for checking.
            checkAllow = allow.Allow(data[1])
            if checkAllow == True :
                # Allow success.
                client.send("print('You allow to success :)')\n".encode('utf-8'))
                # Come back menu admin.
                comeBackMenuAdmin()
            else :
                # Allow unsuccess.
                client.send("print('You allow to unsuccess.\\nTry again :(')\n".encode('utf-8'))
                # Come back menu admin.
                comeBackMenuAdmin()

        # ----- delete -----
        elif data[0].upper() == 'delete'.upper() or (data[0] == '4' and clist[client][1] == 'a'):
            client.send("print('\\n== Delete Post ==')".encode('utf-8'))
            # input post id for deleting.
            client.send(delete.deletepost.encode('utf-8'))
        elif data[0] == '-d' and clist[client][1]=='a':
            # Check data of postId in database.
            checkPost = delete.Delpost(data[1])
            if checkPost == True :
                # True, It has a data of postid in database.
                client.send("print('You delete post to success :)')\n".encode('utf-8'))
                # Come back menu admin.
                comeBackMenuAdmin()
            else :
                # False, It has a data of postid in database.
                client.send("print('You delete post to fail.\\nTry again:(')\n".encode('utf-8'))
                # Come back menu admin.
                comeBackMenuAdmin()

        # ----- delete user -----
        elif data[0].upper() == 'deleteuser'.upper() or (data[0] == '5' and clist[client][1] == 'a'):
            client.send("print('\\n== Delete User ==')".encode('utf-8'))
            # Get data of all user.
            dataUser = showuser.showUser()
            # Show data of all user.
            for user in dataUser :
                client.send("print('User ID : {} User Name : {}')".format(user[0],user[1]).encode('utf-8'))
                time.sleep(0.3)
            # Input userId for deleting.
            client.send(delete.deleteuser.encode('utf-8'))
        elif data[0] == '-D' and clist[client][1]=='a':
            # Get boolean for checking data in database.
            checkDeleteUser = delete.Deluser(data[1])
            if checkDeleteUser == True :
                # It has a data of userId in database it can delete.
                client.send("print('You delete user to success :)')\n".encode('utf-8'))
                # Come back menu admin.
                comeBackMenuAdmin()
            else :
                # It hasn't a data of userId in database.
                client.send("print('You delete user to fail.\\nTry again :(')\n".encode('utf-8'))
                # Come back menu admin.
                comeBackMenuAdmin()

        # ----- logout user and admin -----
        elif data[0].upper() == 'logout'.upper() or (data[0] == '4' and clist[client][1] == 'u') or (data[0] == '6' and clist[client][1] == 'a'):
            print("mas from client{}>>>{}".format(addr,data))
            # Reset addr,status(user,admin),username,userid.
            clist[client] = [addr,0,NULL,NULL]
            client.send("print('logout Successful :)')\n".encode('utf-8'))
            # Come back home.
            comeBackHome()
        else :
            # input error.
            if clist[client][1] == 0 :
                # User is in Home.
                client.send("print('command error :(')\n".encode('utf-8'))
                # Come back home.
                comeBackHome()
            elif clist[client][1] == 'u' :
                # User is logned.
                client.send("print('command error :(')\n".encode('utf-8'))
                comeBackMenuUser()
            elif clist[client][1] == 'a' :
                # Admin is logned.
                client.send("print('command error :(')\n".encode('utf-8'))
                comeBackMenuAdmin()
    client.close()

# start server
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) #Set Socket Option that Socket use same Port.
server.bind((serverip,port))
server.listen(5)

print('server waiting ...')

while True:
    client, addr = server.accept()
    clist[client] = [addr,0,NULL,NULL]
    # display menu.
    comeBackHome()
    # display client and show status amount user online.
    print(client)
    print('กำลังออนไลน์',len(clist),'คน')
    task = threading.Thread(target=client_msg,args=(client,addr))
    task.start()