from ...dbConnection import *

@DBConnection
def getAllOrders(database):
    cursor = database.cursor()
    cursor.execute('SELECT * FROM orders')
    return cursor.fetchall()

@DBConnection
def getTotalOrder(database):
    cursor = database.cursor()
    cursor.execute('SELECT * from (SELECT ALL CustomerID, contains.OrderID, sum(Product_Quantity) as Total_Products, sum(Product_Price*Product_Quantity) as Total_Price from orders join contains on contains.OrderID = orders.Order_ID group by contains.OrderID) as Orders_data')
    return cursor.fetchall()

@DBConnection
def getAllUsers(database):
    cursor = database.cursor()
    cursor.execute('SELECT * from customers')
    return cursor.fetchall()

@DBConnection
def updateArrival(id, arrival, database):
    cursor = database.cursor()
    cursor.execute('UPDATE orders set Arrival_Date = %s where Order_ID = %s', (arrival, id,))
    database.commit()
    
@DBConnection
def updateStatus(id, status, database):
    cursor = database.cursor()
    cursor.execute('UPDATE orders set Order_Status = %s where Order_ID = %s', (status, id,))
    database.commit()

@DBConnection
def setTracking(id, tracking, database):
    cursor = database.cursor()
    cursor.execute('UPDATE orders set Tracking_Number = %s where Order_ID = %s', (tracking, id,))
    database.commit()