# connect database by natthanan 
# 21/02/2022 we use phpMyadmin

# import 
import pymysql

# connect database in phpMyadim
mySql = pymysql.connect(
    user = 'root',
    host = 'localhost',
    database = 'network'
)
myCursor = mySql.cursor()