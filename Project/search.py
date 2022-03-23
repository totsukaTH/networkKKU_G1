# import 
import pymysql

# input postId for searching content.
inputPostid = '''
def postId():
    print("\\n== Search ==\\nInsert your post id that you want to find.")
    postId = input('>>>')
    client.send(str_to(['searchPostId',postId]).encode('utf-8'))
postId()
'''

def searchPost(postId):
    # connect database.
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    # select post from post.
    myCursor.execute("SELECT content FROM post WHERE status != 'W' and postId = (%s)",(postId))
    RequestPost = myCursor.fetchall()
    if bool(RequestPost) == True :
        mySql.commit()
        mySql.close()
        myCursor.close()
        return RequestPost
    else :
        mySql.commit()
        mySql.close()
        myCursor.close()
        return False