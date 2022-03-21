import database 

# register
register = '''
def registerUser():
    # insert data of register
    email = input('Email : ')
    userName = input('Username : ')
    passWord = input('Password : ')

    # sent data of register to database.
    database.insertUser(email,phone,userName,passWord)
registerUser()
'''
def insertUser(email,userName,passWord):
    status = 'u'
    getData = database.myCursor.execute("INSERT INTO user (userName,password,e_mail,type_user) VALUES (%s,%s,%s,%s)",(userName,passWord,email,status))
    database.mySql.commit()
    database.myCursor.close()
    database.mySql.close()