import pymysql

# Text option insert data of delete

# input data of 'post' for deleting.
deletepost ='''
data = input('>>>')
client.send(str_to(['-d',data]).encode('utf-8'))
'''

# input data of 'user' for deleting.
deleteuser ='''
data = input('>>>')
client.send(str_to(['-D',data]).encode('utf-8'))
'''

# delete 'post' by Admin.
def Delpost(poatid):
    # connect database
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    myCursor.execute("DELETE FROM post WHERE postID = {}".format(poatid))
    mySql.commit()
    mySql.close()
    myCursor.close()

# delete 'user' by Admin.
def Deluser(userid):
    # connect database
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    myCursor.execute("DELETE FROM post WHERE userId = {}".format(userid))
    myCursor.execute("DELETE FROM user WHERE userId = {}".format(userid))
    mySql.commit()
    mySql.close()
    myCursor.close()