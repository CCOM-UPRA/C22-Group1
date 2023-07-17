from ...models.frontend.orderModel import *
import random
from flask import session

def order_number():
    number = []
    number.append(random.randrange(10000, 99999))  
    number.append(random.randrange(10000, 99999))  
    return number
     