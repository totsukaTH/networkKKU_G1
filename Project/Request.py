import pymysql
    
# Check Login
def Request():
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    myCursor.execute("SELECT postID,userID,content FROM post WHERE status = 'W' ")
    nameAndPassword = myCursor.fetchall()
    mySql.close()
    myCursor.close()
    return nameAndPassword