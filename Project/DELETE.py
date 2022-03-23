# Import 
import pymysql

# ===== Text option insert data of delete =====
# Input data of post for deleting.
deletepost ='''
print('Insert post id to delete post.')
data = input('>>>')
client.send(str_to(['-d',data]).encode('utf-8'))
'''
# Input data of User for deleting.
deleteuser ='''
print('Insert user id to delete user.')
data = input('>>>')
client.send(str_to(['-D',data]).encode('utf-8'))
'''

# Delete post by Admin.
def Delpost(postId):
    # Connect database.
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    # Select content of post by postId.
    myCursor.execute("SELECT content FROM post WHERE postId = (%s)",(postId))
    RequestPost = myCursor.fetchall()
    # Check has postId a content ?
    if len(RequestPost) == 1 : 
        # postId has a content.
        # Delete post by postId.
        myCursor.execute("DELETE FROM post WHERE postID = {}".format(postId))
        mySql.commit()
        mySql.close()
        myCursor.close()
        # Return Boolean is True that delete post is success.
        return True
    else : 
        # postId hasn't a content.
        mySql.commit()
        mySql.close()
        myCursor.close()
        # Return Boolean is False that delete post is fail.
        return False

# Delete User by Admin.
def Deluser(userId):
    # Connect database.
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    # Select type_user of user by userId.
    myCursor.execute("SELECT type_user FROM user WHERE userId = (%s)",(userId))
    RequestPost = myCursor.fetchall()
    # Check has userId in database ?
    if len(RequestPost) == 1 : 
        # userId has a data in database.
        # Delete post and User in database by userId.
        # Detele post of userId before delete User of userId.
        myCursor.execute("DELETE FROM post WHERE userId = {}".format(userId))
        myCursor.execute("DELETE FROM user WHERE userId = {}".format(userId))
        mySql.commit()
        mySql.close()
        myCursor.close()
        # Return Boolean is True that it is success to delete User.
        return True
    else :
        # userId hasn't a data in database.
        mySql.commit()
        mySql.close()
        myCursor.close()
        # Return Boolean is False that it is fail to delete User.
        return False
    