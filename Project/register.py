# Import 
import pymysql

# Input data to register.
inputRegister = '''
def registerUser():
    print('\\n==== Register ====')
    email = input('Email : ')
    userName = input('Username : ')
    passWord = input('Password : ')
    client.send(str_to(['insertUser',email,userName,passWord]).encode('utf-8'))
registerUser()
'''

# Insert data that User registers to database by User.
def insertUser(email,userName,passWord):
    # Connect database
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    status = 'u'
    # Insert data's register of User to database.
    getData = myCursor.execute("INSERT INTO user (userName,password,e_mail,type_user) VALUES (%s,%s,%s,%s)",(userName,passWord,email,status))
    mySql.commit()
    mySql.close()
    myCursor.close()