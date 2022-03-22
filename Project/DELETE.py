import pymysql

def Delpost(poatid):
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    myCursor.execute(Delpostsql.format(poatid))
    mySql.commit()
    mySql.close()
    myCursor.close()

def Deluser(userid):
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    myCursor.execute(Delusersql.format(userid))
    mySql.commit()
    mySql.close()
    myCursor.close()





Delusersql = '''DELETE FROM user WHERE userId = "{}" ;'''

Delpostsql = '''DELETE FROM post WHERE postID = {} ;'''