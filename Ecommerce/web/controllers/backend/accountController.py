from ...models.backend.accountModel import *
from ...models.frontend.loginModel import *
from ...models.frontend.authModel import *

def UsersList():
    users = all_accounts()
    userList = []
    for i in users:
        user = {
            'id': i[0],
            'name': i[1],
            'Lname': i[2],
            'Email': i[3],
            'phone': i[4],
            'status': i[5],
            'pass': i[6]
        }  
        userList.append(user)
        
    return userList

def addaccount(fname, lname, email, pass1, pass2):
    
    if not fname or not lname or not email or not pass1 or not pass2:
        return 'fill all the blanks'
    
    if pass1 != pass2:
        return 'Password dont match!'
    
    if email_exists(email):
        return 'Email already exists!'
    print(fname, lname, email, pass1, pass2)
    # insert_user(fname, lname, email, pass1)
    return 'Cuenta Creada!'