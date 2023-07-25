from ...dbConnection import *


@DBConnection
def order_info(id, database): 
    cursor = database.cursor()
    cursor.execute('SELECT Order_ID, CustomerID, PaymentID, Order_Number, Order_Date, Arrival_Date, Order_Status, Street_number, Street_name, zipCode, C_City, C_State, Tracking_Number, Invoice_Number FROM orders WHERE CustomerID = %s', (id,))
    result = cursor.fetchone()
    return result

@DBConnection
def order_update(id, user, number, database):
    cursor = database.cursor()
    cursor.execute('UPDATE orders SET Order_Number = %s, Order_Date = %s, Arrival_Date = %s, Order_Status = %s, Street_number = %s, Street_name = %s, zipCode = %s, C_City = %s, C_State = %s, Tracking_Number = %s, Invoice_Number = %s WHERE CustomerID = %s ', (number[0], number[1], number[2], number[3], user[5], user[6], user[7], user[8], user[9], number[4], number[5], id,)) 
    database.commit()
    
@DBConnection
def order_count(id, database):
    cursor = database.cursor()
    cursor.execute('SELECT COUNT(CustomerID) as Total from orders WHERE CustomerID = %s and Order_Number != 0', (id,))
    data = cursor.fetchone()
    
    if data[0] == None:
        return 0
    return data[0]

@DBConnection
def getAllOrders(id, database):
    cursor = database.cursor()
    cursor.execute('SELECT * FROM orders WHERE CustomerID = %s', (id,))   
    return cursor.fetchall()

@DBConnection
def getTotalOrder(id, database):
    cursor = database.cursor()
    cursor.execute('SELECT * from (SELECT ALL CustomerID, contains.OrderID, sum(Product_Quantity) as Total_Products, sum(Product_Price*Product_Quantity) as Total_Price from orders join contains on contains.OrderID = orders.Order_ID group by contains.OrderID) as Orders_data WHERE CustomerID = %s',(id,))
    return cursor.fetchall()


# customerid, order id, el precio total de la orden[total price], total de articulos  [total products]
#SELECT OrderID, sum(Product_Price) as Total_Products, sum(Product_Quantity) as Total_Price from contains group by OrderID

@DBConnection
def getOrderbyStatus(id, status, database):
    cursor = database.cursor()
    cursor.execute('SELECT * from orders WHERE Order_Status = %s and CustomerID = %s', (status, id, ))
    return cursor.fetchall()