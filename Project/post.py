# import 
import pymysql
from datetime import datetime

# input post after user to login.
inputPost = '''
def post():
    print("\\n== Post ==\\nInsert your message.")
    message = input('>>>')
    client.send(str_to(['upPost',message]).encode('utf-8'))
post()
'''

# input postId for searching content.
inputPostid = '''
def postId():
    print("\\n== Search ==\\nInsert your post id that you want to find.")
    postId = int(input('>>>'))
    client.send(str_to(['searchPostId',postId]).encode('utf-8'))
postId()
'''

def insertPost(data,userId):
    # connect database
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    # insert data of post to database
    myCursor.execute("INSERT INTO post (userId,content,DatePost,status) VALUES (%s,%s,%s,%s)",(userId,data[1],datetime.today(),'W'))
    mySql.commit()
    myCursor.close()
    mySql.close()