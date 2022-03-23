# Import 
import pymysql

# Input data of 'postId' for Admin check to allow or not allow.
inputDataForAllow = '''
print('Allow post by PostId (insert)')
data = input('>>> ')
client.send(str_to(['-A',data]).encode('utf-8'))
'''

# Update from status 'w' to 'p' by Admin.
def Allow(postId):
    # Connect database.
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    # Select content of post that status is 'w' by postId.
    # 'w' is waiting for admin allow.
    myCursor.execute("SELECT content FROM post WHERE status = 'w' and postId = (%s)",(postId))
    requestPost = myCursor.fetchall()
    if len(requestPost) == 1 : 
        # postId has a data in database and status of post is 'w'.
        # Update status of post form 'w' to 'p'.
        # 'p' is pass for admin allows post.
        myCursor.execute("UPDATE post SET status = 'p' WHERE postID={}".format(postId))
        mySql.commit()
        mySql.close()
        myCursor.close()
        # Return boolean True that it sets status of post to success.
        return True
    else :
        # postId hasn't a data in database or data isn't status 'w'.
        mySql.commit()
        mySql.close()
        myCursor.close()
        # Return boolean False that it sets status of post to fail.
        return False