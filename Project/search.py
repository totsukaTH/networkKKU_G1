# Import 
import pymysql

# Input postId for searching content by User.
inputPostid = '''
def postId():
    print("\\n== Search ==\\nInsert your post id that you want to find.")
    postId = input('>>>')
    client.send(str_to(['searchPostId',postId]).encode('utf-8'))
postId()
'''

# Search Post by User.
def searchPost(postId):
    # Connect database.
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    # Select post by postId from database.
    myCursor.execute("SELECT content FROM post WHERE status != 'w' and postId = (%s)",(postId))
    RequestPost = myCursor.fetchall()
    if bool(RequestPost) == True : 
        #  postId has a content.
        mySql.commit()
        mySql.close()
        myCursor.close()
        #  Return content.
        return RequestPost
    else :
        #  postId hasn't a content.
        mySql.commit()
        mySql.close()
        myCursor.close()
        #  Return boolean is False that postId hasn't data.
        return False