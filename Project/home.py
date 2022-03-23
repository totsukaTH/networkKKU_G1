# DisplayHome is menu of home.
displayHome = "print('==== Home ====\\n1. Login\\n2. Register\\n3. Exit')"
# DisplayUser is menu after User logged.
displayUser = "print('==== Option of User ====\\n1. Post\\n2. Reading\\n3. Search\\n4. logout')"
# DisplayAdmin is menu after Admin logged.
displayAdmin = "print('==== Option of Admin ====\\n1. Request\\n2. Allow\\n3. Reading\\n4. Delete\\n5. Delete User\\n6. logout')"

# Input choice in home.
inputChoice = '''
data = input('Enter your choice (Text or Number): ')
client.send(str_to([data]).encode('utf-8'))
'''