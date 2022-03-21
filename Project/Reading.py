import pymysql
    
# Check Login
def Reading():
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    myCursor.execute("SELECT postID,userID,content FROM post WHERE status != 'w' ")
    nameAndPassword = myCursor.fetchall()
    mySql.close()
    myCursor.close()
    return nameAndPassword