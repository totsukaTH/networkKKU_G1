import pymysql

# Show all user in database by Admin.
def showUser():
    # Connect database.
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    # Select data of all user.
    myCursor.execute("SELECT userId,userName FROM user")
    dataUser = myCursor.fetchall()
    mySql.close()
    myCursor.close()
    # return all User from database.
    return dataUser