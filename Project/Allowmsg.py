import pymysql

def Allow(poatid):
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    myCursor.execute(UPDATE.format(poatid))
    mySql.commit()
    mySql.close()
    myCursor.close()



UPDATE = '''UPDATE post SET status = 'P' WHERE postID={}'''