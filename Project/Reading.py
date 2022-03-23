# Import
import pymysql

# User or Admin reads content of all post.
def Reading():
    # Connect database.
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    # Select content of post is 'p' in database.
    # 'p' is content of post that Admin allows.
    myCursor.execute("SELECT postID,userID,content FROM post WHERE status != 'w' ")
    detailPostForReading = myCursor.fetchall()
    mySql.close()
    myCursor.close()
    # Return detail of post for reading.
    return detailPostForReading