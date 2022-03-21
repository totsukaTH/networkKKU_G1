# import 
import pymysql
import database 

# Check Request Post by Admin.
def Request():
    # connect database.
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    # select post from post.
    myCursor.execute("SELECT postID,userID,content FROM post WHERE status = 'W' ")
    RequestPost = myCursor.fetchall()
    mySql.close()
    myCursor.close()
    # return value from database of Post.
    return RequestPost