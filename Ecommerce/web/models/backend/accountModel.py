from ...dbConnection import *

@DBConnection
def all_accounts(database): #get all the accounts of the ussers 
    cursor = database.cursor()
    cursor.execute('SELECT CustomerID, C_Fname, C_Lname, C_Email, C_Phone, C_status, C_Password from customers')
    result = cursor.fetchall()
    return result

@DBConnection #update the accounts for the backend
def update_account(fname, lname, pass1, email, phone, status, id, database):
    cursor = database.cursor()
    cursor.execute('UPDATE customers SET C_Fname = %s, C_Lname = %s, C_Email = %s, c_Password = %s, C_Phone = %s, C_status = %s WHERE CustomerID =%s', (fname, lname, email, pass1, phone, status, id))
    database.commit()