from ..models.usermodel import Cart
from .productsControler import getTelescopeById
from .. import dataBase
from flask_login import current_user
from sqlalchemy import text
import json


def CreateCart():
    items = []
    items = json.dumps(items)
    cart = Cart(items=items, total_price=0,
                total_items=0, user_id=current_user.id)
    dataBase.session.add(cart)
    dataBase.session.commit()


def getCart():
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    return cart


def incertToCart(item):
    cart = getCart()
    items = json.loads(cart.items)

    product = getTelescopeById(item['product']['id'])
    if item['quantity'] > product.stock:
        item['quantity'] = product.stock
    items.append(item)
    cart.items = json.dumps(items)
    cart.total_items = cart.total_items + item['quantity']
    sum = (item['quantity'] * item['product']['price'])
    cart.total_price = float(cart.total_price) + sum
    dataBase.session.commit()


def deleteItem(itemid):
    cart = getCart()
    items = json.loads(cart.items)
    for listitem in items:
        if listitem['product']['id'] == int(itemid):
            cart.total_price = float(cart.total_price) - \
                (listitem['quantity'] * listitem['product']['price'])
            cart.total_items = cart.total_items - listitem['quantity']
            items.pop(items.index(listitem))
            break
    cart.items = json.dumps(items)
    dataBase.session.commit()


def editCart(itemid, newValue):
    newValue = int(newValue)
    cart = getCart()
    items = json.loads(cart.items)
    for item in items:
        print(item)
        if item['product']['id'] == int(itemid):
            print(True)
            if newValue > 0:
                cart.total_price = float(cart.total_price) - \
                    (item['quantity'] * item['product']['price'])
                cart.total_items = cart.total_items - item['quantity']

                cart.total_price = float(cart.total_price) + \
                    (newValue * item['product']['price'])
                cart.total_items = cart.total_items + newValue

                item['quantity'] = newValue
            else:
                deleteItem(itemid=itemid)
                return None
    cart.items = json.dumps(items)
    dataBase.session.commit()
