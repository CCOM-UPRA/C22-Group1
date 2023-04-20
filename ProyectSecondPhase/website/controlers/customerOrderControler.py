from .. import dataBase
from sqlalchemy import text
from ..models.curtomerOrderModel import customerOrder

def getOrderId():
    return dataBase.session.execute(text('SELECT order_id FROM customer_order'))

def getUserId():
    return dataBase.session.execute(text('SELECT user_id FROM customer_order'))

def getAllOrders():
    return dataBase.session.execute(text('SELECT * FROM customer_order'))

def getStatus():
    return dataBase.session.execute(text('SELECT status FROM customer_order'))

def getOrderDate():
    return dataBase.session.execute(text('SELECT order_date FROM customer_order'))

def getPaymentMethod():
    return dataBase.session.execute(text('SELECT payment_method FROM customer_order'))

def getTotal():
    return dataBase.session.execute(text('SELECT total FROM customer_order'))