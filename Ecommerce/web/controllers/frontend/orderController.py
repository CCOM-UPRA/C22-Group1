from ...models.frontend.orderModel import *
from ...models.frontend.shopModel import *
import datetime

import random
from flask import session

def order_number():
    number = []
    number.append(random.randrange(100000, 999999)) #order number
    number.append((datetime.datetime.now()).date()) #order date
    business_days = 5 
    number.append((number[1] + datetime.timedelta(days=business_days))) #arrival date
    number.append('Received') #order status
    number.append(random.randrange(10000, 99999))  #tracking number
    number.append(random.randrange(10000, 99999))  #invoice number
  
    return number

def getOrderItems():
    orderId = session['cart']
    products = GetCartData(orderId)
    productsList = []
    for x in products:
        product = {
            'id': x[0],
            'name': x[1],
            'price': x[2],
            'cost': x[3],
            'brand': x[4],
            'description': x[5],
            'image': x[6],
            'stock': x[7],
            'status': x[8],
            'type': x[9],
            'mount': x[10],
            'focal_distance': x[11],
            'aperture': x[12],
            'quantity': x[15]
        }
        productsList.append(product)
    return productsList
     