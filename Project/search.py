# import 
import pymysql

def searchPost(postId):
    # connect database.
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    # select post from post.
    myCursor.execute("SELECT content FROM post WHERE status != 'W' and postId = (%s)",(postId))
    RequestPost = myCursor.fetchall()
    mySql.close()
    myCursor.close()
    return RequestPost