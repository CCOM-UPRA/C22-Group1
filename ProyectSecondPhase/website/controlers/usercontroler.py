from .. import dataBase
from sqlalchemy import text
from flask_login import login_user
from werkzeug.security import generate_password_hash
from ..models.usermodel import User


def checkForCustomer(email):
    user = dataBase.session.execute(text(
        f'SELECT IF(EXISTS (SELECT Email FROM user WHERE Email = "{email}"), TRUE, FALSE)'))
    user = user.fetchone()
    print(user)
    return user


def getUser(email):
    user = dataBase.session.execute(
        text(f'SELECT * FROM user WHERE Email = "{email}" LIMIT 1'))
    return user.fetchone()


def setLoginUser(user):
    login_user(User.query.filter_by(id=user.id).first())


def CreateAccount(fname, lname, email, password):
    new_user = User(
        Fname=fname,
        Lname=lname,
        Email=email,
        Password=generate_password_hash(password, method='sha256')
    )
    dataBase.session.add(new_user)
    dataBase.session.commit()
    setLoginUser(new_user)
