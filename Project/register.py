import database 

# register
def registerUser():
    # insert data of register
    email = input('Email : ')
    phone = input('Phone : ')
    userName = input('Username : ')
    passWord = input('Password : ')

    # sent data of register to database.
    database.insertUser(email,phone,userName,passWord)

def insertUser(email,phone,userName,passWord):
    ip = '127.0.0.1'
    userId = 'u003'
    status = 'a'
    getData = database.myCursor.execute("INSERT INTO user (userId,ip,name,password,email,phone,status) VALUES (%s,%s,%s,%s,%s,%s,%s)",(userId,ip,userName,passWord,email,phone,status))
    database.mySql.commit()
    database.myCursor.close()
    database.mySql.close()