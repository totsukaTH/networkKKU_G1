# import 
import pymysql

# input data to login of user.
inputLogin = '''
def login():
    print("\\nYour login")
    userName = input('Username : ')
    passWord = input('Password : ')
    client.send(str_to(['checkUser',userName,passWord]).encode('utf-8'))
login()
'''

# input choice after user to login.
inputChoiceAfterLogin = '''
data = input('"{}" (insert option) : ')
client.send(str_to([data]).encode('utf-8'))
'''

# Check Login
def checkUser():
    # connect database
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    # select data in database of user for checking login.
    myCursor.execute("SELECT userName,password,userId,type_user FROM user ")
    detailLogin = myCursor.fetchall()
    mySql.close()
    myCursor.close()
    return detailLogin