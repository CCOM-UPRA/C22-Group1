from flask import session

thisDict = {
    "email": "nebula@gmail.com",
    "password": "pass1234",
    "user": "Nebula"
}


def loginmodel(email, password):
    if email in thisDict.values() and password in thisDict.values():
        session['admin'] = thisDict['user']
        return "true"
    else:
        return "false"
