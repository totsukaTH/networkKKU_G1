# import 
import pymysql
from datetime import datetime

# input post after user to login.
inputPost = '''
def post():
    print("\\n== Post ==")
    print("Insert your message.")
    message = input('>>>')
    client.send(str_to(['upPost',message]).encode('utf-8'))
post()
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