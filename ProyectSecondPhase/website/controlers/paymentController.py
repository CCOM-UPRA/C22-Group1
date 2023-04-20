from ..models.paymentModel import payment
from flask_login import current_user

from .. import dataBase
from sqlalchemy import text


def CreateCard():
    card = payment(user_id=current_user.id)
    dataBase.session.add(card)
    dataBase.session.commit()


def getCardName():
    name = dataBase.session.execute(
        text(f"SELECT name FROM payment WHERE id = {current_user.id}")).fetchone()
    return name


def getCardNumber():
    return dataBase.session.execute(text(f"SELECT number FROM payment WHERE id = {current_user.id}")).fetchone()


def getCardType():
    return dataBase.session.execute(text(f"SELECT type FROM payment WHERE id = {current_user.id}")).fetchone()


def getMonth():
    return dataBase.session.execute(text(f"SELECT month FROM payment WHERE id = {current_user.id}")).fetchone()


def getYear():
    return dataBase.session.execute(text(f"SELECT year FROM payment WHERE id = {current_user.id}")).fetchone()
