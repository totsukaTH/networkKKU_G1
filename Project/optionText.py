# input login of user.
inputLogin = '''
def login():
    print("Your login")
    userName = input('Username : ')
    passWord = input('Password : ')
    client.send(str_to(['checkUser',userName,passWord]).encode('utf-8'))
login()
'''

# input register of new user.
inputRegister = '''
def registerUser():
    # insert data of register
    email = input('Email : ')
    userName = input('Username : ')
    passWord = input('Password : ')
    client.send(str_to(['insertUser',email,userName,passWord]).encode('utf-8'))
registerUser()
'''

# input post after user to login.
inputPost = '''
def post():
    print("Enter the message you want to post.")
    message = input('>>>')
    client.send(str_to(['upPost',message]).encode('utf-8'))
post()
'''

# reading 
Readingstr = """
def Reading():
    print("Enter '>>' or '<<'")
    #message = input('>>>')
    #client.send(str_to([message]).encode('utf-8'))
post()
"""
# input choice after user to login.
inputChoiceAfterLogin = '''
data = input('user name is "{}" >>> ')
client.send(str_to([data]).encode('utf-8'))
'''

inputChoice = '''
data = input('Enter your choice : ')
client.send(str_to([data]).encode('utf-8'))
'''