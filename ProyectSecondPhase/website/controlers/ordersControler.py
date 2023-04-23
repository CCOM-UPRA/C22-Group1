from ..models.ordersModel import Orders
from ..models.curtomerOrderModel import customerOrder
from ..controlers.cartcontroler import *
from .. import dataBase
from sqlalchemy import text
from flask_login import current_user
import datetime
import random

order_date = datetime.datetime.strptime('2023-04-17 10:30:00', '%Y-%m-%d %H:%M:%S')


#para obtener los order id de ordenes de el usuario
def getUserOrders():
    Uorders =  dataBase.session.execute(text(f"SELECT * FROM orders WHERE user_id = {current_user.id}"))
    return Uorders


# para contar cuantas order tiene un usuario


def countORders():
    result = dataBase.session.execute(text(f"SELECT COUNT(order_id) FROM orders WHERE user_id = {current_user.id}"))
    order_count = result.fetchone()[0]
    return order_count

#para obatener los items de la ordenes
def getOrderItems():
    items = dataBase.session.execute(
        text(f'SELECT order_prods FROM orders WHERE user_id = {current_user.id}'))
    items = list(map(lambda item: json.loads(json.loads(item[0])), items))
    return items

#para obatener los items de la ordenes
def getOrderItemsByNumber(id):
    items = dataBase.session.execute(
        text(f'SELECT order_prods FROM orders WHERE tracking_num = {id}'))
    items = list(map(lambda item: json.loads(json.loads(item[0])), items))
    return items

# def getUPayMethod():
    


def getOrderDate():
    return dataBase.session.execute(text('SELECT order_date FROM customer_order'))


def getorderid():
    return dataBase.session.execute(text('SELECT DISTINCT order_id FROM orders'))

# SQL para cambiar el total de la orden usando el id de la orden


def uptd_ordert():
    return dataBase.session.execute(text('UPDATE orders SET c_total = total_c WHERE id = order_id'))

# Escoger una orden especifico de un usuario


def sel_user_Ord():
    # Añadir el user que se quieren ver las ordenes
    return dataBase.session.execute(text('SELECT * FROM orders where user_id = user_id'))

# Escoger Ordenes dentro un rango de tiempo


def esp_range_orders():
    return dataBase.session.execute(text('SELECT * FROM orders WHERE order_date BETWEEN date1 AND date2'))
# Anadir los ranges a los cuales se les quiere buscar tales ordenes


def get_trackingnum():
    return dataBase.session.execute(text('SELECT DISTINCT tracking_num FROM orders')).fetchone()


def generar_tracking_fedex():
    # Generar número de seguimiento de 12 dígitos o 15 dígitos
    longitud = random.choice([12, 15])
    digitos = [random.randint(0, 9) for _ in range(longitud)]
    
    # Unir los dígitos en una cadena
    tracking_number = "".join(str(d) for d in digitos)
    
    return tracking_number

   

def create_order():
    cart = getCart()
    new_Order = Orders( user_id = current_user.id,
                        tracking_num = generar_tracking_fedex(),
                        order_date = order_date,
                        arrival_date = order_date,
                        address_line_1 = current_user.Address,
                        address_line_2 = current_user.Street,
                        total  = float(cart.total_price),
                        amount = 5,
                        payment_method = "credit card",
                        # amount = getAmount(),
                        # payment_method = getPayMethod(),
                        status = 'Pending',
                        order_prods =  json.dumps(cart.items)
                        )
    dataBase.session.add(new_Order)
    print(new_Order)
    dataBase.session.commit()
    return new_Order

def testdata():
    new_Order = Orders(     user_id = '4',    
                            order_id = '1210',
                            tracking_num = '12121213',
                            order_date = order_date,
                            arrival_date = order_date,
                            address_line_1 = 'barceloneta Puerto Rico ',
                            address_line_2 = 'barceloneta Puerto Rico',
                            total = 400,
                            amount = '400',
                            payment_method = 'Visa',
                            status = 'Pending',
                            order_prods = 1)

    dataBase.session.add(new_Order)
    print(new_Order)
    dataBase.session.commit()
