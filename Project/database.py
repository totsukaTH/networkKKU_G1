# connect database by natthanan 
# 21/02/2022 we use phpMyadmin

# import 
from pickle import FALSE, TRUE
import pymysql

# connect database in phpMyadin
mySql = pymysql.connect(
    user = 'root',
    host = 'localhost',
    database = 'network'
)
myCursor = mySql.cursor()