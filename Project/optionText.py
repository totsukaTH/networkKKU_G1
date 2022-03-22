# input postId for searching content.
inputPostid = '''
def postId():
    postId = int(input('Insert Post Id for seaching : '))
    client.send(str_to(['searchPostId',postId]).encode('utf-8'))
postId()
'''

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

# input choice in home.
inputChoice = '''
data = input('Enter your choice : ')
client.send(str_to([data]).encode('utf-8'))
'''

inputallow = '''
data = input('>>>')
client.send(str_to(['-A',data]).encode('utf-8'))
'''

inputdelete ='''
data = input('>>>')
client.send(str_to(['-d',data]).encode('utf-8'))
'''

inputdeleteuser ='''
data = input('>>>')
client.send(str_to(['-D',data]).encode('utf-8'))
'''



