# import 
import socket
import login
import register

serverip = '127.0.0.1'
port = 3000

# client
while True:
    
    # connect server
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server.connect((serverip,port))
    
    # home 
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    # check condition
    checkLogin = ''
    if choice == 1 : 
       checkLogin = login.loginUser()
    elif choice == 2 :
       checkLogin = register.registerUser()
    
    # send massage to server.
    server.send(checkLogin.encode('utf-8'))
    # get massage from server.
    data_server = server.recv(1024).decode('utf-8')
    # display massage from server
    print('Data from Server: ', data_server)
    server.close()
