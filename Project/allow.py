# import 
import pymysql

# input data of 'postId' for allow.
inputDataForAllow = '''
print('Allow post by PostId (insert)')
data = input('>>> ')
client.send(str_to(['-A',data]).encode('utf-8'))
'''

# function for update from status 'w' to 'p'.
def Allow(poatid):
    # connect database
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    # update status of post from 'w' to 'p' by postId.
    myCursor.execute("UPDATE post SET status = 'p' WHERE postID={}".format(poatid))
    mySql.commit()
    mySql.close()
    myCursor.close()