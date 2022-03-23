# Import 
import pymysql

# Check Request of Post by Admin.
def Request():
    # Connect database.
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    # Select all post of user that it is status 'w'.
    myCursor.execute("SELECT postID,userID,content FROM post WHERE status = 'w' ")
    RequestPost = myCursor.fetchall()
    mySql.close()
    myCursor.close()
    # return all Post from database.
    return RequestPost