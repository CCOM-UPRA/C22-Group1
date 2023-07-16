from ...dbConnection import *

@DBConnection
def order_info(id, database): #selecciona informacion del usuario deacuerdo al id
    cursor = database.cursor()
    cursor.execute('SELECT Order_ID, CustomerID, PaymentID, Order_Number, Order_Date, Arrival_Date, Order_Status, Street_number, Street_name, zipCode, C_City, C_State, Tracking_Number, Invoice_Number FROM orders WHERE CustomerID = %s', (id,))
    result = cursor.fetchone()
    return result