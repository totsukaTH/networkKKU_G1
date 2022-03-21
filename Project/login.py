import pymysql
    
# Check Login
def checkUser(userName,passWord):
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    myCursor.execute("SELECT userName,password FROM user ")
    nameAndPassword = myCursor.fetchall()
    mySql.close()
    myCursor.close()
    for data in nameAndPassword :
        if data[0] == userName and data[1] == passWord :
            # username and password is correct.
            return True
    # username and password is incorrect.
    return False