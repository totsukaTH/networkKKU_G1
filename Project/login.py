import database

# Login
def loginUser():
    # insert user and password for login.
    userName = input('Username : ')
    passWord = input('Password : ')
    check = checkUser(userName,passWord)

    # Check user and password
    if check == True :
        return "success"
    return "fail"

# Check Login
def checkUser(userName,passWord):
    database.myCursor.execute("SELECT name,password FROM user ")
    nameAndPassword = database.myCursor.fetchall()
    for data in nameAndPassword :
        if data[0] == userName and data[1] == passWord :
            # username and password is correct.
            return True
    # username and password is incorrect.
    return False
