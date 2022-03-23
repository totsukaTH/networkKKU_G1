# input choice in home.
inputChoice = '''
data = input('Enter your choice (Text or Number): ')
client.send(str_to([data]).encode('utf-8'))
'''

displayHome = "print('==== Home ====\\n1. Login\\n2. Register\\n3. Exit')"

displayUser = "print('==== Option of User ====\\n1. Post\\n2. Reading\\n3. Search\\n4. logout')"

displayAdmin = "print('==== Option of Admin ====\\n1. Request\\n2. Allow\\n3. Reading\\n4. Delete\\n5. Delete User\\n6. logout')"