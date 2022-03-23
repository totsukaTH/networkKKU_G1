# Import 
import pymysql
from datetime import datetime

# Input content of post by User.
inputPost = '''
def post():
    print("\\n== Post ==")
    print("Insert your message.")
    message = input('>>>')
    client.send(str_to(['upPost',message]).encode('utf-8'))
post()
'''
# Insert content of User to database by User.
def insertPost(data,userId):
    # Connect database.
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    # Insert content of post to database.
    myCursor.execute("INSERT INTO post (userId,content,DatePost,status) VALUES (%s,%s,%s,%s)",(userId,data[1],datetime.today(),'w'))
    mySql.commit()
    myCursor.close()
    mySql.close()