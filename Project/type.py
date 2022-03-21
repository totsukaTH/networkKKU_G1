import pymysql

def checktype(userName):
    mySql = pymysql.connect(user = 'root',host = 'localhost',database = 'network')
    myCursor = mySql.cursor()
    myCursor.execute("SELECT userName,type_user FROM user ")
    name = myCursor.fetchall()
    mySql.close()
    myCursor.close()
    for data in name :
        if data[0] == userName :
            return data[1]