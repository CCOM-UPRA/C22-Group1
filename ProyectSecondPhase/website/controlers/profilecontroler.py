from .. import dataBase
from flask_login import current_user
from .paymentController import *


def setFname(fname):
    dataBase.session.execute(
        text(f"UPDATE user SET Fname = '{fname}' WHERE id = {current_user.id}"))


def setLname(lname):
    dataBase.session.execute(
        text(f"UPDATE user SET Lname = '{lname}' WHERE id = {current_user.id}"))


def setEmail(email):
    dataBase.session.execute(
        text(f"UPDATE User SET Email = '{email}' WHERE id = {current_user.id}"))


def setNumber(number):
    dataBase.session.execute(
        text(f"UPDATE user SET Phone = '{number}' WHERE id = {current_user.id}"))


def setAline1(aline1):
    dataBase.session.execute(
        text(f"UPDATE user SET Address = '{aline1}' WHERE id = {current_user.id}"))


def setAline2(aline2):
    dataBase.session.execute(
        text(f"UPDATE user SET Street = '{aline2}' WHERE id = {current_user.id}"))


def setCity(city):
    dataBase.session.execute(
        text(f"UPDATE user SET City = '{city}' WHERE id = {current_user.id}"))


def setState(state):
    dataBase.session.execute(
        text(f"UPDATE user SET State = '{state}' WHERE id = {current_user.id}"))


def setZipCode(zipcode):
    dataBase.session.execute(
        text(f"UPDATE user SET ZipCode = '{zipcode}' WHERE id = {current_user.id}"))
