# import 
import pymysql
from datetime import datetime

def insertPost(data,userId):
    # connect database
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    # insert data of post to database
    myCursor.execute("INSERT INTO post (userId,content,DatePost,status) VALUES (%s,%s,%s,%s)",(userId,data[1],datetime.today(),'W'))
    mySql.commit()
    myCursor.close()
    mySql.close()
    
