from flask import session

# This is a very basic dictionary with information for logging in
# Simulating our database
thisDict = {
    "email": ['jean@upr.edu', 'user@gmail.com', 'nebula@gmail.com'],
    "password": ['pass1234', '1234', 'pass1234'],
    "user": ['Jean', 'User', 'Nebula']
}


def loginmodel(email, password):
    # Receive email and password to check in the "database"
    if email in thisDict['email'] and password in thisDict['password']:
        if thisDict['email'].index(email) == thisDict['password'].index(password):
            # If it found the email and pass in the dictionary
            session['customer'] = thisDict['user'][thisDict['email'].index(email)]
            # Create the session['customer']
            return "true"
        else:
            return 'false'
    else:
        # If it didn't find user
        return "false"
