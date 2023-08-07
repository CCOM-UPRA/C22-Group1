from ...models.backend.accountModel import *
from ...models.frontend.loginModel import *
from ...models.frontend.authModel import *
import hashlib

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