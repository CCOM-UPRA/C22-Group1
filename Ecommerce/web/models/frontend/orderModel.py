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
    cursor.execute('UPDATE orders SET Order_Number = %s, Order_Date = %s, Arrival_Date = %s, Order_Status = %s, Street_number = %s, Street_name = %s, zipCode = %s, C_City = %s, C_State = %s, Tracking_Number = %s, Invoice_Number = %s WHERE CustomerID = %s ', (number[0], number[1], number[2], number[4], user[5], user[6], user[7], user[8], user[9], number[4], number[5], id,)) 
    database.commit()