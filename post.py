import database

def insertPost():
    count = database.myCursor.execute("INSERT INTO post (postId,userId,title,content,date) VALUES ('p004, 'u001', 'สวัสดีครับ','ทักไปทุกวัน ความสัมพันธ์แค่เพื่อน','2020-12-15')")
    database.mySql.commit()
    database.myCursor.close()
    database.mySql.close()