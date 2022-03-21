import pymysql
from datetime import datetime

idp = 100

def insertPost(data,user):
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()

    myCursor.execute("INSERT INTO post (userID,content,DatePost,status) VALUES (%s,%s,%s,%s)",(user,data[1],datetime.today(),'w'))
    
    mySql.commit()
    myCursor.close()
    mySql.close()
    
