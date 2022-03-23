# Import 
import pymysql

# Input data to login of User.
inputLogin = '''
def login():
    print("\\nYour login")
    userName = input('Username : ')
    passWord = input('Password : ')
    client.send(str_to(['checkUser',userName,passWord]).encode('utf-8'))
login()
'''

# Input choice after User to login.
inputChoiceAfterLogin = '''
data = input('"{}" (Insert option Text or Number) : ')
client.send(str_to([data]).encode('utf-8'))
'''

# Check Login of User.
def checkUser():
    # Connect database.
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    # Select data in database of user for checking login.
    myCursor.execute("SELECT userName,password,userId,type_user FROM user ")
    detailLogin = myCursor.fetchall()
    mySql.close()
    myCursor.close()
    # Return data of userName,password,userId,type_user.
    return detailLogin