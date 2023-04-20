from ..models.ordersModel import Orders
from .. import dataBase
from sqlalchemy import text
from flask_login import current_user

#para obtener los order id de ordenes de el usuario
def getAllOrders():
    return dataBase.session.execute(text(f"SELECT * FROM orders WHERE user_id == {current_user.id}"))

# para contar cuantas order tiene un usuario
def countORders():
    return dataBase.session.execute(text(f"SELECT DISTINCT COUNT(order_id) FROM orders WHERE user_id == {current_user.id} ")).fetchall()



def getorderid():
    return dataBase.session.execute(text('SELECT DISTINCT order_id FROM orders'))

# SQL para cambiar el total de la orden usando el id de la orden
def uptd_ordert():
    return dataBase.session.execute(text('UPDATE orders SET c_total = total_c WHERE id = order_id'))
                                         
# Escoger una orden especifico de un usuario
def sel_user_Ord():
    return dataBase.session.execute(text('SELECT * FROM orders where user_id = user_id')) #Añadir el user que se quieren ver las ordenes

# Escoger Ordenes dentro un rango de tiempo
def esp_range_orders():
    return dataBase.session.execute(text('SELECT * FROM orders WHERE order_date BETWEEN date1 AND date2')) 
# Anadir los ranges a los cuales se les quiere buscar tales ordenes

def get_trackingnum():
    return dataBase.session.execute(text('SELECT DISTINCT tracking_num FROM orders')).fetchone()

def testdata():
    new_Order = Orders(     user_id = '1',    
                            order_id = '1233',
                               tracking_num = '12121213',
                            #    order_date = 'order_date_obj',
                            #    arrival_date = 'order_date_obj',
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






