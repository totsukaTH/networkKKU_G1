import pymysql

# Text option insert data of delete

# input data of 'post' for deleting.
deletepost ='''
print('Insert post id to delete post.')
data = input('>>>')
client.send(str_to(['-d',data]).encode('utf-8'))
'''

# input data of 'user' for deleting.
deleteuser ='''
print('Insert user id to delete user.')
data = input('>>>')
client.send(str_to(['-D',data]).encode('utf-8'))
'''

# delete 'post' by Admin.
def Delpost(postId):
    # connect database
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    myCursor.execute("SELECT content FROM post WHERE postId = (%s)",(postId))
    RequestPost = myCursor.fetchall()
    if len(RequestPost) == 1 :
        myCursor.execute("DELETE FROM post WHERE postID = {}".format(postId))
        mySql.commit()
        mySql.close()
        myCursor.close()
        return True
    else :
        mySql.commit()
        mySql.close()
        myCursor.close()
        return False

# delete 'user' by Admin.
def Deluser(userId):
    # connect database
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    myCursor.execute("SELECT type_user FROM user WHERE userId = (%s)",(userId))
    RequestPost = myCursor.fetchall()
    if len(RequestPost) == 1 :
        myCursor.execute("DELETE FROM post WHERE userId = {}".format(userId))
        myCursor.execute("DELETE FROM user WHERE userId = {}".format(userId))
        mySql.commit()
        mySql.close()
        myCursor.close()
        return True
    else :
        mySql.commit()
        mySql.close()
        myCursor.close()
        return False
    