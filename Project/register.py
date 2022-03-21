import pymysql

# insert data of register to database
def insertUser(email,userName,passWord):
    # connect database
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    status = 'u'
    # insert data of register to database.
    getData = myCursor.execute("INSERT INTO user (userName,password,e_mail,type_user) VALUES (%s,%s,%s,%s)",(userName,passWord,email,status))
    mySql.commit()
    mySql.close()
    myCursor.close()