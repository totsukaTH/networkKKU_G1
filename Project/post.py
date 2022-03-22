# import 
import pymysql
from datetime import datetime

# input post after user to login.
inputPost = '''
def post():
    print("Enter the message you want to post.")
    message = input('>>>')
    client.send(str_to(['upPost',message]).encode('utf-8'))
post()
'''

# input postId for searching content.
inputPostid = '''
def postId():
    postId = int(input('Insert Post Id for seaching : '))
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