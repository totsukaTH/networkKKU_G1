# import 
import pymysql
import database

# Check Login
def checkUser():
    # connect database.
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    # select data in database of user for checking login.
    myCursor.execute("SELECT userName,password,userId FROM user ")
    detailLogin = myCursor.fetchall()
    mySql.close()
    myCursor.close()
    return detailLogin