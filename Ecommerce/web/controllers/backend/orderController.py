from ...models.backend.ordersModel import *
from ..frontend.orderController import getOrderItensByID
import time, random
from flask import session

def getAllOrdersItems():
    
    if 'BackfilterStatus' in session:
        AllOrders = getAllOrdersByStatus(session['BackfilterStatus'])
    else:
        AllOrders = getAllOrders()
    Totals = getTotalOrder()
    users = getAllUsers()
    AllOrdersItems = []
    
    for order in AllOrders:
        if order[3] != 0:
            OrderTotal = 0
            TotalItems = 0
            userEmail = ''
            for total in Totals:
                if total[1] == order[0]:
                    OrderTotal = total[3]
                    TotalItems = total[2]
                    break
            
            for user in users:
                if user[0] == order[1]:
                    userEmail = user[3]
                    break
            OrderData = {
                'order':order,
                'items':getOrderItensByID(order[0]),
                'TotalPrice':OrderTotal,
                'TotalItems':TotalItems,
                'Email':userEmail
                }
            AllOrdersItems.append(OrderData)
    return AllOrdersItems

def orderUpdate(id, arrival,prevArrival, status, prevStatus, tracking):
    
    if tracking == 0 or tracking == '0':
        random.seed(time.time())
        setTracking(id, random.randrange(10000000, 99999999))
    
    if status != prevStatus and status != "":
        updateStatus(id, status)
    
    if arrival != prevArrival and arrival != "":
        updateArrival(id, arrival)

def getOrderCount():
    count = orderCount()[0]
    if count == None:
        count = 0
    
    return count