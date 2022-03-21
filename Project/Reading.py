# import
import pymysql
import database

# Check Login
def Reading():
    # connect database.
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    # select data of post is not 'w' in database.
    myCursor.execute("SELECT postID,userID,content FROM post WHERE status != 'W' ")
    detailPostForReading = myCursor.fetchall()
    mySql.close()
    myCursor.close()
    # return detail of post for reading.
    return detailPostForReading