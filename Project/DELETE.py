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
    myCursor.execute(Delusersql1.format(userid))
    myCursor.execute(Delusersql2.format(userid))
    mySql.commit()
    mySql.close()
    myCursor.close()




Delusersql1 = '''DELETE FROM post WHERE userId = {} ;'''
Delusersql2 = '''DELETE FROM user WHERE userId = "{}" ;'''

Delpostsql = '''DELETE FROM post WHERE postID = {} ;'''